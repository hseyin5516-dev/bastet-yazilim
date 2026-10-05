"""
Bastet Yazılım Sosyal Medya Günlük Otomasyon Yöneticisi (Daily Runner 360°)
Haftanın 7 gününe özel planlanmış içerikleri (Carousel + Web Tek Görsel Afiş + 2 Hikaye)
otomatik üretir ve Meta Graph API ile canlı yayınlar.

Takvim ve İçerik Döngüsü:
- Pazartesi: [Satış] Kurumsal Web Tasarım + [Tek Post] Web Tasarım Afişi + 2 Hikaye (Sabah/Akşam)
- Salı: [Eğitici] Google SEO & Yerel Haritalar + 2 Hikaye
- Çarşamba: [Satış] Randevu & Klinik Sistemleri + [Tek Post] Web Tasarım Afişi + 2 Hikaye
- Perşembe: [Eğitici] Meta Reklamları (WhatsApp Lead) + 2 Hikaye
- Cuma: [Satış] Sade Ön Muhasebe & CRM + [Tek Post] Web Tasarım Afişi + 2 Hikaye
- Cumartesi: [Eğitici] 2026 Web Güvenlik ve Hız Standartları + [Tek Post] Web Tasarım Afişi + 2 Hikaye
- Pazar: [Satış] Oto Servis & Emlak Portföy Sistemleri + 2 Hikaye
"""

import os
import sys
import json
import argparse
from datetime import datetime

# Windows terminal UTF-8 uyumluluğu
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from content_data import SERVICES_DATA
from generator import generate_day, generate_all
from publisher import publish_or_export, publish_service_folder, MetaPublisher

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

# Haftanın günleri haritası (Python weekday: 0=Pazartesi ... 6=Pazar)
WEEKDAY_TO_SERVICE = {
    0: "01_pazartesi_web_tasarim",
    1: "02_sali_google_seo",
    2: "03_carsamba_randevu_klinik",
    3: "04_persembe_meta_reklamlari",
    4: "05_cuma_muhasebe_crm",
    5: "06_cumartesi_web_guvenlik_hiz",
    6: "07_pazar_oto_servis_emlak"
}


def get_today_service_id():
    """Bugünün gününe karşılık gelen hizmet ID'sini döndürür."""
    weekday = datetime.now().weekday()
    return WEEKDAY_TO_SERVICE.get(weekday, "01_pazartesi_web_tasarim")


def show_status():
    """Tüm hizmetlerin durumunu, slaytları, tekil afişi ve hikayeleri listeler."""
    print("\n" + "=" * 75)
    print("📊 BASTET YAZILIM SOSYAL MEDYA 360° HAFTALIK İÇERİK PLANI")
    print("=" * 75)
    today_id = get_today_service_id()

    for sid, sdata in SERVICES_DATA.items():
        is_today = " [BUGÜN 🌟]" if sid == today_id else ""
        folder_path = os.path.join(OUTPUT_DIR, sid)
        
        slide_count = 0
        has_single = False
        has_morning_story = False
        has_evening_story = False

        if os.path.exists(folder_path):
            slides = [f for f in os.listdir(folder_path) if f.startswith("slayt_") and f.endswith(".png")]
            slide_count = len(slides)
            has_single = os.path.exists(os.path.join(folder_path, "tek_gorsel_web.png"))
            has_morning_story = os.path.exists(os.path.join(folder_path, "hikaye_sabah.png"))
            has_evening_story = os.path.exists(os.path.join(folder_path, "hikaye_aksam.png"))

        c_status = f"{slide_count}/5 Carousel"
        s_status = "Tek Post: VAR" if has_single else "Tek Post: YOK"
        story_status = "2/2 Story" if (has_morning_story and has_evening_story) else "0/2 Story"

        type_tag = "[SATIŞ]" if sdata.get("type") == "sales" else "[EĞİTİM]"
        print(f"[{sdata['day']:<9}] {type_tag:<8} {sdata['name']:<30} | {c_status} | {s_status} | {story_status}{is_today}")

    print("=" * 75 + "\n")


def run_today(publish_carousel=False, publish_single=False, publish_stories=False):
    """Bugünün içeriğini yürütür ve seçilen bileşenleri canlı yayınlar."""
    today_id = get_today_service_id()
    topic = SERVICES_DATA[today_id]
    print(f"\n🌟 BUGÜNÜN İÇERİK PLANI: [{topic['day']}] {topic['name']} ({topic['type'].upper()})")
    
    # 1. Klasörü hazırla / üret
    folder, meta_info = generate_day(today_id)
    
    pub = MetaPublisher()
    configured = pub.is_configured()

    # Carousel
    if publish_carousel:
        if configured:
            print("\n🚀 [1/3] Carousel Yayınlanıyor...")
            publish_service_folder(folder)
        else:
            print("⚠️ Meta API yapılandırılmadı, Carousel yayınlanamadı.")
    else:
        publish_or_export(folder)

    # 2 Günde 1 Web Tasarım Tek Görsel Postu
    if topic.get("has_single_post"):
        single_img = os.path.join(folder, "tek_gorsel_web.png")
        single_caption_path = os.path.join(folder, "tek_gorsel_caption.txt")
        if os.path.exists(single_img) and os.path.exists(single_caption_path):
            with open(single_caption_path, "r", encoding="utf-8") as f:
                single_caption = f.read()

            if publish_single:
                if configured:
                    print("\n🚀 [2/3] Web Tasarım Tek Görsel Afiş Yayınlanıyor...")
                    pub.publish_single_post(single_img, single_caption)
                else:
                    print("⚠️ Meta API yapılandırılmadı, Tek Görsel yayınlanamadı.")
            else:
                print(f"💡 Bugünün Web Tasarım Tek Görsel Afişi hazır: {single_img}")

    # Günlük 2 Hikaye (Instagram & Facebook Stories)
    story_morning = os.path.join(folder, "hikaye_sabah.png")
    story_evening = os.path.join(folder, "hikaye_aksam.png")

    if publish_stories:
        if configured:
            print("\n🚀 [3/3] Günlük 2 Hikaye Yayınlanıyor (Instagram & Facebook)...")
            if os.path.exists(story_morning):
                print("☀️ Sabah Hikayesi yükleniyor...")
                if pub.ig_user_id:
                    try:
                        pub.publish_instagram_story(story_morning)
                    except Exception as e:
                        print(f"⚠️ Instagram Sabah Hikayesi Hatası: {e}")
                if pub.page_id:
                    try:
                        pub.publish_facebook_story(story_morning)
                    except Exception as e:
                        print(f"⚠️ Facebook Sabah Hikayesi Hatası: {e}")

            if os.path.exists(story_evening):
                print("🌙 Akşam Hikayesi yükleniyor...")
                if pub.ig_user_id:
                    try:
                        pub.publish_instagram_story(story_evening)
                    except Exception as e:
                        print(f"⚠️ Instagram Akşam Hikayesi Hatası: {e}")
                if pub.page_id:
                    try:
                        pub.publish_facebook_story(story_evening)
                    except Exception as e:
                        print(f"⚠️ Facebook Akşam Hikayesi Hatası: {e}")
        else:
            print("⚠️ Meta API yapılandırılmadı, hikayeler yayınlanamadı.")
    else:
        print(f"💡 Günlük 2 Hikaye görseli hazır: {story_morning} & {story_evening}")


def main():
    parser = argparse.ArgumentParser(description="Bastet Yazılım Sosyal Medya Otomasyon Motoru (360°)")
    parser.add_argument("--today", action="store_true", help="Bugüne ait içerikleri üretir.")
    parser.add_argument("--all", action="store_true", help="Tüm 7 günün içeriklerini (Carousel, Afiş, Hikayeler) üretir.")
    parser.add_argument("--status", action="store_true", help="Haftalık içerik durumunu listeler.")
    parser.add_argument("--service", type=str, choices=list(SERVICES_DATA.keys()), help="Belirli bir günü/hizmeti seçerek üretir.")
    parser.add_argument("--publish", action="store_true", help="Carousel gönderisini Meta API ile canlı yayınlar.")
    parser.add_argument("--publish-single", action="store_true", help="Bugün geçerli ise tek görsel afişi canlı yayınlar.")
    parser.add_argument("--publish-stories", action="store_true", help="Bugünün sabah ve akşam hikayelerini canlı yayınlar.")
    parser.add_argument("--publish-all", action="store_true", help="Bugün için planlanan TÜM içerikleri (Carousel + Tek Görsel + 2 Hikaye) canlı yayınlar.")

    args = parser.parse_args()

    if args.status:
        show_status()
    elif args.all:
        generate_all()
        show_status()
    elif args.service:
        folder, meta_info = generate_day(args.service)
        pub = MetaPublisher()
        if (args.publish or args.publish_all) and pub.is_configured():
            publish_service_folder(folder)
        else:
            publish_or_export(folder)
    else:
        # Varsayılan veya --today
        p_car = args.publish or args.publish_all
        p_single = args.publish_single or args.publish_all
        p_story = args.publish_stories or args.publish_all
        run_today(publish_carousel=p_car, publish_single=p_single, publish_stories=p_story)


if __name__ == "__main__":
    main()
