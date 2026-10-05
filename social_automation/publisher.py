"""
Bastet Yazılım Sosyal Medya Meta Graph API Otomasyon Motoru
Instagram ve Facebook sayfalarında %100 otomatik (başsız) Carousel ve gönderi paylaşımı yürütür.
"""

import os
import sys
import json
import base64
import time
import argparse
import urllib.request
import urllib.parse
import urllib.error

# Windows terminal UTF-8 uyumluluğu
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)
ENV_FILE = os.path.join(BASE_DIR, ".env")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")


def load_env():
    """Çalışma dizinindeki .env dosyasını okur."""
    env_vars = {}
    if os.path.exists(ENV_FILE):
        with open(ENV_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    env_vars[k.strip()] = v.strip().strip('"').strip("'")
    return env_vars


def save_env(key_value_dict):
    """Verilen anahtarları .env dosyasına yazar."""
    current = load_env()
    current.update(key_value_dict)
    with open(ENV_FILE, "w", encoding="utf-8") as f:
        f.write("# Bastet Yazılım Meta Graph API Yapılandırması\n")
        f.write("META_API_VERSION=v21.0\n")
        for k, v in current.items():
            if k != "META_API_VERSION":
                f.write(f"{k}={v}\n")
    print(f"✅ Yapılandırma kaydedildi: {ENV_FILE}")


def upload_image_to_public_cdn(filepath, imgbb_key=None):
    """
    Yerel PNG görselini Meta Graph API'nin erişebileceği genel bir HTTPS linkine dönüştürür.
    """
    if imgbb_key:
        try:
            url = "https://api.imgbb.com/1/upload"
            with open(filepath, "rb") as f:
                b64_data = base64.b64encode(f.read()).decode("utf-8")
            data = urllib.parse.urlencode({"key": imgbb_key, "image": b64_data}).encode("utf-8")
            req = urllib.request.Request(url, data=data)
            with urllib.request.urlopen(req, timeout=20) as resp:
                res = json.loads(resp.read().decode("utf-8"))
                return res["data"]["url"]
        except Exception:
            pass

    # Yüksek hızlı doğrudan HTTPS CDN (freeimage.host API)
    url = "https://freeimage.host/api/1/upload"
    with open(filepath, "rb") as f:
        b64_data = base64.b64encode(f.read()).decode("utf-8")
    data = urllib.parse.urlencode({
        "key": "6d207e02198a847aa98d0a2a901485a5",
        "action": "upload",
        "source": b64_data,
        "format": "json"
    }).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"User-Agent": "BastetAutomation/1.0"})
    with urllib.request.urlopen(req, timeout=25) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        return res["image"]["url"]


class MetaPublisher:
    """Instagram Graph API & Facebook Page Graph API ile Carousel paylaşımı."""

    def __init__(self):
        env = load_env()
        self.access_token = env.get("META_ACCESS_TOKEN", os.getenv("META_ACCESS_TOKEN", ""))
        self.ig_user_id = env.get("INSTAGRAM_ACCOUNT_ID", os.getenv("INSTAGRAM_ACCOUNT_ID", ""))
        self.page_id = env.get("FACEBOOK_PAGE_ID", os.getenv("FACEBOOK_PAGE_ID", ""))
        self.imgbb_key = env.get("IMGBB_API_KEY", os.getenv("IMGBB_API_KEY", ""))
        self.api_version = env.get("META_API_VERSION", "v21.0")
        self.base_url = f"https://graph.facebook.com/{self.api_version}"

    def is_configured(self):
        return bool(self.access_token and (self.ig_user_id or self.page_id))

    def _make_request(self, endpoint, data=None, method="POST"):
        url = f"{self.base_url}/{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        encoded_data = urllib.parse.urlencode(data).encode("utf-8") if data else None
        req = urllib.request.Request(url, data=encoded_data, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8")
            try:
                err_json = json.loads(err_body)
                msg = err_json.get("error", {}).get("message", err_body)
                code = err_json.get("error", {}).get("code", "")
                raise RuntimeError(f"Meta Graph API Hatası (Kod: {code}): {msg}")
            except Exception:
                raise RuntimeError(f"HTTP Hatası {e.code}: {err_body}")

    def test_connection(self):
        """Erişim token'ını ve bağlı sayfaları kontrol eder."""
        if not self.access_token:
            return False, "META_ACCESS_TOKEN bulunamadı."
        try:
            res = self._make_request("me?fields=id,name", method="GET")
            user_name = res.get("name", "Bilinmeyen Kullanıcı")
            msg = f"Bağlantı başarılı! Meta Kullanıcı Adı: {user_name}"
            
            # Instagram kontrolü
            if self.ig_user_id:
                try:
                    ig_res = self._make_request(f"{self.ig_user_id}?fields=username", method="GET")
                    msg += f" | Instagram Hesabı: @{ig_res.get('username')}"
                except Exception as e:
                    msg += f" | (Instagram Uyarısı: {e})"
            
            # Facebook kontrolü
            if self.page_id:
                try:
                    fb_res = self._make_request(f"{self.page_id}?fields=name", method="GET")
                    msg += f" | Facebook Sayfası: {fb_res.get('name')}"
                except Exception as e:
                    msg += f" | (Facebook Uyarısı: {e})"

            return True, msg
        except Exception as e:
            return False, str(e)

    def publish_instagram_carousel(self, local_slide_paths, caption):
        """5 slaytlık carousel'ı Instagram'da yayınlar."""
        if not self.ig_user_id:
            raise ValueError("INSTAGRAM_ACCOUNT_ID yapılandırılmamış!")

        print("\n☁️ Slaytlar genel HTTPS CDN'e yükleniyor...")
        public_urls = []
        for idx, path in enumerate(local_slide_paths, 1):
            cdn_url = upload_image_to_public_cdn(path, self.imgbb_key)
            public_urls.append(cdn_url)
            print(f"   [{idx}/{len(local_slide_paths)}] Yüklendi: {cdn_url}")

        print("\n📸 Meta Instagram slayt containerları oluşturuluyor...")
        item_ids = []
        for idx, img_url in enumerate(public_urls, 1):
            data = {
                "image_url": img_url,
                "is_carousel_item": "true",
            }
            res = self._make_request(f"{self.ig_user_id}/media", data)
            item_ids.append(res["id"])
            print(f"   [{idx}/{len(public_urls)}] Container ID: {res['id']}")

        print("\n📦 Ana Carousel paketi hazırlanıyor...")
        carousel_data = {
            "media_type": "CAROUSEL",
            "children": ",".join(item_ids),
            "caption": caption
        }
        res_car = self._make_request(f"{self.ig_user_id}/media", carousel_data)
        creation_id = res_car["id"]

        print(f"⏳ Carousel container hazırlandı ({creation_id}). Meta işlemesi bekleniyor (5 sn)...")
        time.sleep(5)

        print("🚀 Instagram'da yayınlanıyor (media_publish)...")
        pub_res = self._make_request(f"{self.ig_user_id}/media_publish", {"creation_id": creation_id})
        post_id = pub_res.get("id")
        print(f"🎉 INSTAGRAM CAROUSEL YAYINLANDI! Post ID: {post_id}")
        return post_id

    def publish_facebook_photos(self, local_slide_paths, message):
        """Facebook Sayfasında 5 fotoğraflı albüm/gönderi paylaşır."""
        if not self.page_id:
            raise ValueError("FACEBOOK_PAGE_ID yapılandırılmamış!")

        print("\n📢 Facebook fotoğrafları yükleniyor...")
        photo_ids = []
        for idx, path in enumerate(local_slide_paths, 1):
            cdn_url = upload_image_to_public_cdn(path, self.imgbb_key)
            data = {
                "url": cdn_url,
                "published": "false"  # Feed'e tek paket olarak basmak için henüz yayınlama
            }
            res = self._make_request(f"{self.page_id}/photos", data)
            photo_ids.append(res["id"])
            print(f"   [{idx}/{len(local_slide_paths)}] Fotoğraf ID: {res['id']}")

        print("\n📰 Facebook akışında birleşik gönderi yayınlanıyor...")
        attached_media_list = [{"media_fbid": pid} for pid in photo_ids]
        feed_data = {
            "message": message,
            "attached_media": json.dumps(attached_media_list)
        }

        res_feed = self._make_request(f"{self.page_id}/feed", feed_data)
        post_id = res_feed.get("id")
        print(f"🎉 FACEBOOK GÖNDERİSİ YAYINLANDI! Post ID: {post_id}")
        return post_id

    def publish_facebook_carousel(self, local_slide_paths, message):
        """
        Facebook Sayfasında kaydırmalı Carousel paylaşır (child_attachments ile).
        Eğer child_attachments API'si sayfa için desteklenmiyorsa fotoğraflı albüm feed'ine döner.
        """
        if not self.page_id:
            raise ValueError("FACEBOOK_PAGE_ID yapılandırılmamış!")

        print("\n📢 Facebook Carousel için görseller CDN'e yükleniyor...")
        card_items = []
        for idx, path in enumerate(local_slide_paths, 1):
            cdn_url = upload_image_to_public_cdn(path, self.imgbb_key)
            card_items.append({
                "link": "https://bastetyazilim.com",
                "picture": cdn_url,
                "name": f"Bastet Yazılım | {idx}. Adım"
            })
            print(f"   [{idx}/{len(local_slide_paths)}] Carousel Kartı: {cdn_url}")

        # 1. Yöntem: Facebook child_attachments ile doğrudan kaydırmalı Carousel
        try:
            feed_data = {
                "message": message,
                "link": "https://bastetyazilim.com",
                "child_attachments": json.dumps(card_items)
            }
            res_feed = self._make_request(f"{self.page_id}/feed", feed_data)
            post_id = res_feed.get("id")
            print(f"🎉 FACEBOOK CAROUSEL YAYINLANDI! Post ID: {post_id}")
            return post_id
        except Exception as e:
            print(f"⚠️ Facebook child_attachments uyarısı ({e}), standart albüm feed'ine geçiliyor...")
            return self.publish_facebook_photos(local_slide_paths, message)

    def publish_facebook_story(self, local_image_path):
        """9:16 Hikayeyi Facebook Sayfasında yayınlar (photo_stories endpoint)."""
        if not self.page_id:
            raise ValueError("FACEBOOK_PAGE_ID yapılandırılmamış!")

        print(f"\n☁️ Facebook Hikaye görseli CDN'e yükleniyor: {os.path.basename(local_image_path)}...")
        cdn_url = upload_image_to_public_cdn(local_image_path, self.imgbb_key)
        print(f"   CDN URL: {cdn_url}")

        print("📸 Facebook fotoğrafı hazırlanıyor (published=false)...")
        data = {
            "url": cdn_url,
            "published": "false"
        }
        res_photo = self._make_request(f"{self.page_id}/photos", data)
        photo_id = res_photo["id"]

        print(f"🚀 Facebook Hikayesi yayınlanıyor (photo_stories, ID: {photo_id})...")
        res_story = self._make_request(f"{self.page_id}/photo_stories", {"photo_id": photo_id})
        story_id = res_story.get("id", photo_id)
        print(f"🎉 FACEBOOK HİKAYESİ YAYINLANDI! Story ID: {story_id}")
        return story_id

    def publish_instagram_story(self, local_image_path):
        """9:16 Hikayeyi Instagram'da yayınlar (media_type=STORIES)."""
        if not self.ig_user_id:
            raise ValueError("INSTAGRAM_ACCOUNT_ID yapılandırılmamış!")

        print(f"\n☁️ Instagram Hikaye görseli CDN'e yükleniyor: {os.path.basename(local_image_path)}...")
        cdn_url = upload_image_to_public_cdn(local_image_path, self.imgbb_key)
        print(f"   CDN URL: {cdn_url}")

        print("📸 Meta Instagram Hikaye containerı oluşturuluyor...")
        data = {
            "image_url": cdn_url,
            "media_type": "STORIES"
        }
        res = self._make_request(f"{self.ig_user_id}/media", data)
        creation_id = res["id"]
        print(f"⏳ Hikaye container hazırlandı ({creation_id}). Bekleniyor (5 sn)...")
        time.sleep(5)

        print("🚀 Instagram Hikayesi yayınlanıyor...")
        pub_res = self._make_request(f"{self.ig_user_id}/media_publish", {"creation_id": creation_id})
        story_id = pub_res.get("id")
        print(f"🎉 INSTAGRAM HİKAYESİ YAYINLANDI! Story ID: {story_id}")
        return story_id

    def publish_single_post(self, local_image_path, caption):
        """Tekil gönderiyi hem Instagram hem Facebook akışında paylaşır."""
        res_ids = {}
        cdn_url = None

        if self.ig_user_id:
            print(f"\n☁️ Tek görsel CDN'e yükleniyor: {os.path.basename(local_image_path)}...")
            cdn_url = upload_image_to_public_cdn(local_image_path, self.imgbb_key)
            print(f"   CDN URL: {cdn_url}")

            print("📸 Instagram tek görsel containerı oluşturuluyor...")
            data = {
                "image_url": cdn_url,
                "caption": caption
            }
            res = self._make_request(f"{self.ig_user_id}/media", data)
            creation_id = res["id"]
            print(f"⏳ Container hazırlandı ({creation_id}). Bekleniyor (5 sn)...")
            time.sleep(5)

            print("🚀 Instagram'da yayınlanıyor...")
            pub_res = self._make_request(f"{self.ig_user_id}/media_publish", {"creation_id": creation_id})
            res_ids["instagram"] = pub_res.get("id")
            print(f"🎉 INSTAGRAM TEK GÖRSEL YAYINLANDI! Post ID: {res_ids['instagram']}")

        if self.page_id:
            print("\n📢 Facebook tek fotoğraf gönderisi paylaşılıyor...")
            if not cdn_url:
                cdn_url = upload_image_to_public_cdn(local_image_path, self.imgbb_key)
            fb_data = {
                "url": cdn_url,
                "message": caption
            }
            fb_res = self._make_request(f"{self.page_id}/photos", fb_data)
            res_ids["facebook"] = fb_res.get("id")
            print(f"🎉 FACEBOOK TEK GÖRSEL YAYINLANDI! Post ID: {res_ids['facebook']}")

        return res_ids


def setup_wizard():
    """Kullanıcının token ve ID bilgilerini girmesi için sihirbaz."""
    print("\n" + "=" * 65)
    print("🔑 BASTET YAZILIM - META GRAPH API KURULUM SİHİRBAZI")
    print("=" * 65)
    print("Meta Developers (developers.facebook.com) üzerinden aldığınız")
    print("erişim anahtarlarını girin (İptal için Ctrl+C):\n")

    token = input("1. META_ACCESS_TOKEN (Sayfa Erişim Tokenı): ").strip()
    if not token:
        print("❌ Token boş bırakılamaz!")
        return

    ig_id = input("2. INSTAGRAM_ACCOUNT_ID (İsteğe bağlı, örn: 178414...): ").strip()
    fb_id = input("3. FACEBOOK_PAGE_ID (İsteğe bağlı, örn: 10452...): ").strip()
    imgbb = input("4. IMGBB_API_KEY (İsteğe bağlı, boş bırakılırsa ücretsiz cdn kullanılır): ").strip()

    data = {"META_ACCESS_TOKEN": token}
    if ig_id:
        data["INSTAGRAM_ACCOUNT_ID"] = ig_id
    if fb_id:
        data["FACEBOOK_PAGE_ID"] = fb_id
    if imgbb:
        data["IMGBB_API_KEY"] = imgbb

    save_env(data)
    
    pub = MetaPublisher()
    ok, msg = pub.test_connection()
    if ok:
        print(f"\n🎉 {msg}")
        print("Artık tek komutla Instagram & Facebook'ta canlı paylaşım yapabilirsiniz!\n")
    else:
        print(f"\n⚠️ Doğrulama Uyarısı: {msg}")


def publish_or_export(service_dir):
    """Paylaşılacak gönderi paketini doğrular ve özetler."""
    metadata_path = os.path.join(service_dir, "metadata.json")
    caption_path = os.path.join(service_dir, "caption.txt")
    
    if not os.path.exists(metadata_path) or not os.path.exists(caption_path):
        raise FileNotFoundError(f"Klasörde gerekli dosyalar bulunamadı: {service_dir}")

    with open(metadata_path, "r", encoding="utf-8") as f:
        meta = json.load(f)

    with open(caption_path, "r", encoding="utf-8") as f:
        caption = f.read()

    slides = [os.path.join(service_dir, f"slayt_{i}.png") for i in range(1, 6)]
    valid_slides = [s for s in slides if os.path.exists(s)]

    pub = MetaPublisher()
    print("\n" + "=" * 65)
    print(f"📌 BASTET YAZILIM SOSYAL MEDYA: [{meta.get('day')}] {meta.get('name')}")
    print("=" * 65)
    print(f"📁 Klasör: {service_dir}")
    print(f"🖼️ Slayt Sayısı: {len(valid_slides)} adet görsel (1080x1080)")
    
    if pub.is_configured():
        print("🔑 Meta Graph API Anahtarları Tespit Edildi.")
    else:
        print("💡 Meta API henüz yapılandırılmadı. 'python publisher.py --setup' ile ekleyebilirsiniz.")

    print("\n📝 AÇIKLAMA METNİ:")
    print("-" * 65)
    print(caption)
    print("-" * 65 + "\n")
    return {
        "meta": meta,
        "slides": valid_slides,
        "caption": caption
    }


def publish_service_folder(folder_path):
    """Belirtilen klasördeki carousel'ı Meta API ile paylaşır."""
    metadata_path = os.path.join(folder_path, "metadata.json")
    caption_path = os.path.join(folder_path, "caption.txt")
    
    if not os.path.exists(metadata_path) or not os.path.exists(caption_path):
        raise FileNotFoundError(f"Klasörde gerekli dosyalar bulunamadı: {folder_path}")

    with open(metadata_path, "r", encoding="utf-8") as f:
        meta = json.load(f)

    with open(caption_path, "r", encoding="utf-8") as f:
        caption = f.read()

    slides = [os.path.join(folder_path, f"slayt_{i}.png") for i in range(1, 6)]
    valid_slides = [s for s in slides if os.path.exists(s)]

    if len(valid_slides) < 5:
        raise ValueError(f"Klasörde 5 slayt bulunamadı, bulunan: {len(valid_slides)}")

    pub = MetaPublisher()
    
    print("\n" + "=" * 65)
    print(f"🚀 CANLI YAYINLAMA BAŞLATILIYOR: [{meta.get('day')}] {meta.get('name')}")
    print("=" * 65)

    if not pub.is_configured():
        print("❌ Meta API anahtarları henüz yapılandırılmamış!")
        print("Kurulum için şu komutu çalıştırın:")
        print("   python social_automation/publisher.py --setup")
        print("\nVeya .env dosyanıza META_ACCESS_TOKEN ve INSTAGRAM_ACCOUNT_ID ekleyin.")
        return

    # Instagram
    if pub.ig_user_id:
        try:
            pub.publish_instagram_carousel(valid_slides, caption)
        except Exception as e:
            print(f"❌ Instagram Paylaşım Hatası: {e}")

    # Facebook
    if pub.page_id:
        try:
            pub.publish_facebook_carousel(valid_slides, caption)
        except Exception as e:
            print(f"❌ Facebook Paylaşım Hatası: {e}")

    print("\n✅ İşlem tamamlandı!\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bastet Yazılım Meta Graph API Yayınlama Motoru")
    parser.add_argument("--setup", action="store_true", help="API token ve sayfa ID kurulum sihirbazını başlatır.")
    parser.add_argument("--check-token", action="store_true", help="Kayıtlı token'ın geçerliliğini test eder.")
    parser.add_argument("--folder", type=str, help="Paylaşılacak klasör yolu.")
    parser.add_argument("--today", action="store_true", help="Bugünün klasörünü tespit edip yayınlar.")
    
    args = parser.parse_args()

    if args.setup:
        setup_wizard()
    elif args.check_token:
        pub = MetaPublisher()
        ok, msg = pub.test_connection()
        print(f"Durum: {'✅ BAŞARILI' if ok else '❌ BAŞARISIZ'}")
        print(f"Detay: {msg}")
    elif args.folder:
        publish_service_folder(args.folder)
    elif args.today:
        from daily_runner import get_today_service_id, SERVICES_DATA
        tid = get_today_service_id()
        topic = SERVICES_DATA[tid]
        folder = os.path.join(OUTPUT_DIR, f"{topic['day_num']:02d}_{tid}")
        publish_service_folder(folder)
    else:
        # Default help
        parser.print_help()
