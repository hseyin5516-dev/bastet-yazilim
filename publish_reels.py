"""
Reels Doğrudan (Direct Resumable) Yayınlama Aracı:
Hiçbir 3. parti siteye ihtiyaç duymadan, reels/reels1.mp4 videosunu
doğrudan Meta'nın resmi rupload sunucusuna ikili (binary) akışla yükler ve yayınlar.
"""

import os
import sys
import json
import time
import requests

# Windows terminal UTF-8
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from social_automation.publisher import load_env, MetaPublisher

VIDEO_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "reels", "reels1.mp4")

CAPTION = """Pazar akşamı saat 21:00... Ahmet de dinleniyor, Veli de. ☕

İkisi de aynı işi yapıyor ama aralarında çok sessiz, büyük bir fark var. 
Ahmet’in kepenkleri kapalı; sosyal medyasında sadece bir telefon numarası var. Müşteri gece bu saatte aramak istemiyor, çekiniyor ve ekranı kapatıp gidiyor. ❌

Veli’nin dükkanı da kapalı ama onun yerine 7/24 çalışan modern bir kurumsal web sitesi var. Müşteri hizmetleri inceliyor, çekinmeden tek tıkla talebini bırakıyor. Veli ise çayını yudumluyor. ⚡

Biri sabah dükkanı açtığında sinek avlarken, diğeri gece gelen yeni işlerle güne başlıyor.

Peki siz dinlenirken... İşletmeniz müşteri kaybediyor mu, yoksa kazanıyor mu?

🔗 İşletmenizin dijital vitrinini 3 günde açmak için profilimizdeki linke tıklayın veya WhatsApp'tan yazın: 0551 514 95 11
🌐 bastetyazilim.com

#bastetyazilim #webtasarım #dijitaldönüşüm #esnaf #girişimcilik #müşterikazanımı #websitesi #yazılım #küçükİşletmeler #reelsviral #satışstratejisi"""


def publish_instagram_direct_reels(pub, filepath, caption):
    """Instagram'a doğrudan binary resumable upload ile Reels yükler."""
    print("\n📸 [1/2] Instagram Reels Doğrudan Yükleme Başlatılıyor...")
    file_size = os.path.getsize(filepath)
    print(f"   Dosya Boyutu: {file_size / (1024*1024):.1f} MB")

    # 1. Resumable Container Aç
    url_init = f"https://graph.facebook.com/{pub.api_version}/{pub.ig_user_id}/media"
    init_data = {
        "media_type": "REELS",
        "upload_type": "resumable",
        "caption": caption,
        "share_to_feed": "true",
        "access_token": pub.access_token
    }
    r = requests.post(url_init, data=init_data, timeout=30)
    init_res = r.json()
    if "id" not in init_res:
        raise RuntimeError(f"Instagram container açılamadı: {init_res}")

    container_id = init_res["id"]
    upload_uri = init_res.get("uri", f"https://rupload.facebook.com/ig-api-upload/v21.0/{container_id}")
    print(f"   Container ID: {container_id}")
    print("   Meta rupload sunucusuna doğrudan video akışı aktarılıyor...")

    # 2. Videoyu Meta'nın rupload sunucusuna doğrudan yükle
    with open(filepath, "rb") as f:
        video_data = f.read()

    upload_headers = {
        "Authorization": f"OAuth {pub.access_token}",
        "offset": "0",
        "file_size": str(file_size),
        "Content-Type": "application/octet-stream"
    }

    r_upload = requests.post(upload_uri, headers=upload_headers, data=video_data, timeout=180)
    print(f"   Video akışı yüklendi, yanıt kodu: {r_upload.status_code}")

    # 3. Meta Transcoding (İşleme) Durumunu Bekle
    print("⏳ Meta video işleme (transcoding) bekleniyor...")
    for attempt in range(1, 20):
        time.sleep(8)
        status_url = f"https://graph.facebook.com/{pub.api_version}/{container_id}?fields=status_code&access_token={pub.access_token}"
        try:
            s_res = requests.get(status_url, timeout=20).json()
            status = s_res.get("status_code")
            print(f"   [{attempt * 8} sn] Durum: {status}")
            if status == "FINISHED":
                break
            elif status == "ERROR":
                raise RuntimeError(f"Meta video işleme hatası: {s_res}")
        except Exception as e:
            print(f"   Durum kontrol uyarısı: {e}")

    # 4. Yayına Al
    print("🚀 Instagram Reels yayına alınıyor (media_publish)...")
    pub_url = f"https://graph.facebook.com/{pub.api_version}/{pub.ig_user_id}/media_publish"
    r_pub = requests.post(pub_url, data={"creation_id": container_id, "access_token": pub.access_token}, timeout=30)
    pub_res = r_pub.json()
    ig_post_id = pub_res.get("id")
    print(f"🎉 INSTAGRAM REELS YAYINLANDI! Post ID: {ig_post_id}")
    return ig_post_id


def publish_facebook_direct_video(pub, filepath, caption):
    """Facebook Sayfasına doğrudan binary multipart ile Reels/Video yükler."""
    print("\n📢 [2/2] Facebook Sayfasına Doğrudan Video Yükleniyor...")
    url = f"https://graph-video.facebook.com/{pub.api_version}/{pub.page_id}/videos"
    
    with open(filepath, "rb") as f:
        files = {
            "source": ("reels1.mp4", f, "video/mp4")
        }
        data = {
            "access_token": pub.access_token,
            "title": "Ahmet vs Veli: Pazar Akşamı 21:00",
            "description": caption
        }
        r = requests.post(url, files=files, data=data, timeout=240)
        fb_res = r.json()

    fb_id = fb_res.get("id")
    if fb_id:
        print(f"🎉 FACEBOOK REELS/VİDEO YAYINLANDI! Video ID: {fb_id}")
    else:
        print(f"❌ Facebook Video Hatası: {fb_res}")
    return fb_id


def main():
    if not os.path.exists(VIDEO_PATH):
        print(f"❌ Video dosyası bulunamadı: {VIDEO_PATH}")
        return

    pub = MetaPublisher()
    if not pub.is_configured():
        print("❌ Meta API yapılandırılmamış!")
        return

    print("=" * 65)
    print("🎬 BASTET YAZILIM REELS DOĞRUDAN (DIRECT) YAYINLAMA")
    print("=" * 65)
    print(f"📁 Video: {VIDEO_PATH}")
    print(f"⚖️ Boyut: {os.path.getsize(VIDEO_PATH) / (1024*1024):.1f} MB")

    # 1. Instagram Reels
    if pub.ig_user_id:
        try:
            publish_instagram_direct_reels(pub, VIDEO_PATH, CAPTION)
        except Exception as e:
            print(f"❌ Instagram Reels Hatası: {e}")

    # 2. Facebook Reels / Video
    if pub.page_id:
        try:
            publish_facebook_direct_video(pub, VIDEO_PATH, CAPTION)
        except Exception as e:
            print(f"❌ Facebook Video Hatası: {e}")

    print("\n✅ TÜM İŞLEMLER TAMAMLANDI!\n")


if __name__ == "__main__":
    main()
