"""
Bastet Yazılım Sosyal Medya Tasarım Motoru (360° - 4:5 Dikey Portre Sürümü)
- 1080x1350 (4:5 Portre) 5 Slaytlık Carousel Görselleri (Instagram & Facebook için tam ekran)
- 1080x1350 (4:5 Portre) Web Tasarım Tek Görsel (Afiş / Poster)
- 1080x1920 (9:16 Dikey) Sabah ve Akşam Hikayeleri (Instagram & Facebook Stories)
"""

import os
import sys
import json
import textwrap

# Windows terminal UTF-8 uyumluluğu
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from PIL import Image, ImageDraw, ImageFont
try:
    from .content_data import SERVICES_DATA
except ImportError:
    from content_data import SERVICES_DATA

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
LOGO_PATH = os.path.join(PROJECT_DIR, "logo.png")
LOGO_NEON_PATH = os.path.join(BASE_DIR, "logo_neon.png")
BY_SYMBOL_PATH = os.path.join(BASE_DIR, "by_symbol.png")

# Boyutlar: 4:5 Dikey Portre (1080 x 1350)
WIDTH = 1080
HEIGHT = 1350

# Hikaye Boyutları: 9:16 Dikey (1080 x 1920)
STORY_WIDTH = 1080
STORY_HEIGHT = 1920

# Renk Paleti (Bastet Neon / Koyu Uzay Teması)
COLOR_BG_DARK = (10, 15, 29)
COLOR_CARD_BG = (17, 24, 39, 235)
COLOR_CYAN = (6, 182, 212)
COLOR_BLUE = (59, 130, 246)
COLOR_PURPLE = (147, 51, 234)
COLOR_WHITE = (255, 255, 255)
COLOR_GRAY = (156, 163, 175)
COLOR_LIGHT_GRAY = (209, 213, 219)
COLOR_GREEN = (34, 197, 94)
COLOR_YELLOW = (250, 204, 21)
COLOR_RED = (239, 68, 68)


def get_font(size, bold=False):
    """Windows ve Linux sistem fontlarını kullanarak temiz font döndürür."""
    font_names = [
        "segoeuib.ttf" if bold else "segoeui.ttf", 
        "arialbd.ttf" if bold else "arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    ]
    for font_name in font_names:
        try:
            return ImageFont.truetype(font_name, size)
        except Exception:
            continue
    return ImageFont.load_default()


def draw_checkmark(draw, cx, cy, size=14, color=COLOR_GREEN, width=4):
    """Net ve pürüzsüz vektörel onay tik ikonu çizer."""
    p1 = (cx - size, cy)
    p2 = (cx - size // 3, cy + int(size * 0.75))
    p3 = (cx + size, cy - int(size * 0.85))
    draw.line([p1, p2], fill=color, width=width)
    draw.line([p2, p3], fill=color, width=width)


def draw_crossmark(draw, cx, cy, size=12, color=COLOR_RED, width=4):
    """Net ve pürüzsüz vektörel çarpı (X) ikonu çizer."""
    draw.line([(cx - size, cy - size), (cx + size, cy + size)], fill=color, width=width)
    draw.line([(cx - size, cy + size), (cx + size, cy - size)], fill=color, width=width)


def ensure_brand_assets():
    """Arka plana uyumlu beyaz/cyan logo ve 'by' amblemini hazırlar."""
    if not os.path.exists(BY_SYMBOL_PATH) and os.path.exists(LOGO_PATH):
        try:
            logo = Image.open(LOGO_PATH).convert("RGBA")
            by_crop = logo.crop((55, 30, 235, 170))
            by_crop.save(BY_SYMBOL_PATH)
        except Exception:
            pass


def draw_background(draw, height=HEIGHT):
    """Koyu neon uzay ızgara ve parlama efektleri çizer."""
    for y in range(height):
        ratio = y / height
        r = int(9 + ratio * 8)
        g = int(14 + ratio * 11)
        b = int(27 + ratio * 18)
        draw.line([(0, y), (WIDTH, y)], fill=(r, g, b))

    # Dekoratif neon halkalar
    draw.arc([-160, -160, 680, 680], start=0, end=90, fill=(6, 182, 212, 85), width=3)
    draw.arc([540, height - 700, 1380, height + 140], start=180, end=270, fill=(59, 130, 246, 85), width=3)
    draw.arc([WIDTH - 320, -120, WIDTH + 220, 420], start=90, end=180, fill=(147, 51, 234, 50), width=3)

    # Arka plan nokta matrisi (Grid)
    for x in range(65, WIDTH - 50, 65):
        for y in range(65, height - 50, 65):
            draw.point((x, y), fill=(255, 255, 255, 22))


def add_header(img, draw, slide_num, total_slides=5):
    """Carousel üst header: Yatay Logo + Slayt Sayacı + İlerleme Çizgisi"""
    ensure_brand_assets()
    
    logo_drawn = False
    if os.path.exists(BY_SYMBOL_PATH):
        try:
            by_sym = Image.open(BY_SYMBOL_PATH).convert("RGBA")
            h = 56
            w = int(by_sym.width * (h / by_sym.height))
            by_resized = by_sym.resize((w, h), Image.Resampling.LANCZOS)
            img.paste(by_resized, (70, 52), by_resized)
            
            font_b = get_font(25, bold=True)
            font_y = get_font(16, bold=True)
            draw.text((70 + w + 15, 53), "BASTET", fill=COLOR_WHITE, font=font_b)
            draw.text((70 + w + 15, 80), "YAZILIM", fill=COLOR_CYAN, font=font_y)
            logo_drawn = True
        except Exception:
            pass
            
    if not logo_drawn:
        font_bastet = get_font(30, bold=True)
        draw.text((70, 62), "BASTET YAZILIM", fill=COLOR_WHITE, font=font_bastet)

    badge_text = f"{slide_num} / {total_slides}"
    font_badge = get_font(22, bold=True)
    draw.rounded_rectangle([WIDTH - 170, 54, WIDTH - 70, 108], radius=27, fill=(30, 41, 59, 230), outline=(51, 65, 85), width=2)
    draw.text((WIDTH - 138, 66), badge_text, fill=COLOR_CYAN, font=font_badge)

    # İlerleme Çubuğu
    draw.rounded_rectangle([70, 130, WIDTH - 70, 134], radius=2, fill=(30, 41, 59))
    prog_w = int((WIDTH - 140) * (slide_num / total_slides))
    draw.rounded_rectangle([70, 130, 70 + prog_w, 134], radius=2, fill=COLOR_CYAN)


# ================= 4:5 CAROUSEL SLAYTLARI (1080 x 1350) =================

def create_slide_1_cover(topic):
    img = Image.new("RGBA", (WIDTH, HEIGHT), COLOR_BG_DARK)
    draw = ImageDraw.Draw(img)
    draw_background(draw)
    add_header(img, draw, 1)

    # Kategori Rozeti
    draw.rounded_rectangle([70, 185, 480, 240], radius=26, fill=(6, 182, 212, 35), outline=COLOR_CYAN, width=2)
    draw.text((95, 198), f"{topic['category']}", fill=COLOR_CYAN, font=get_font(20, bold=True))

    # Başlıklar (4:5 formatında geniş ve ferah)
    font_title = get_font(52, bold=True)
    draw.text((70, 275), topic['cover_title_1'], fill=COLOR_WHITE, font=font_title)
    draw.text((70, 350), topic['cover_title_2'], fill=COLOR_CYAN, font=font_title)
    if topic.get('cover_title_3'):
        draw.text((70, 428), topic['cover_title_3'], fill=COLOR_YELLOW, font=get_font(44, bold=True))

    # Büyük Kart Alanı
    box_top = 535
    box_height = 490
    draw.rounded_rectangle([70, box_top, WIDTH - 70, box_top + box_height], radius=32, fill=COLOR_CARD_BG, outline=(55, 65, 81), width=2)
    
    draw.text((110, box_top + 45), topic['cover_highlight_badge'], fill=COLOR_YELLOW, font=get_font(28, bold=True))
    draw.text((110, box_top + 105), topic['cover_highlight_text'], fill=COLOR_WHITE, font=get_font(34, bold=True))
    
    # Alt Açıklama
    sub_lines = textwrap.wrap(topic['cover_subtext'], width=48)
    for l_idx, line in enumerate(sub_lines):
        draw.text((110, box_top + 175 + (l_idx * 36)), line, fill=COLOR_LIGHT_GRAY, font=get_font(24, bold=False))
    
    # Aksiyon Çağrısı Butonu
    cta_y = box_top + box_height - 110
    draw.rounded_rectangle([110, cta_y, WIDTH - 110, cta_y + 70], radius=22, fill=(6, 182, 212, 35), outline=COLOR_CYAN, width=2)
    draw.text((140, cta_y + 20), "Detaylar ve net çözümler için kaydırın  →", fill=COLOR_CYAN, font=get_font(23, bold=True))

    # Alt Kaydırma İpucu
    draw.text((WIDTH // 2 - 130, HEIGHT - 110), "Sola Kaydırın  »", fill=COLOR_GRAY, font=get_font(28, bold=True))
    return img


def create_slide_2_problem(topic):
    img = Image.new("RGBA", (WIDTH, HEIGHT), COLOR_BG_DARK)
    draw = ImageDraw.Draw(img)
    draw_background(draw)
    add_header(img, draw, 2)

    draw.text((70, 180), "• SIK KARŞILAŞILAN PROBLEM", fill=COLOR_RED, font=get_font(24, bold=True))
    draw.text((70, 230), topic['problem_headline'], fill=COLOR_WHITE, font=get_font(44, bold=True))

    y_start = 340
    for idx, prob in enumerate(topic['problems']):
        card_y = y_start + (idx * 250)
        draw.rounded_rectangle([70, card_y, WIDTH - 70, card_y + 215], radius=26, fill=COLOR_CARD_BG, outline=(75, 85, 99), width=2)
        
        # Numara Rozeti
        draw.ellipse([100, card_y + 45, 180, card_y + 125], fill=(239, 68, 68, 40), outline=COLOR_RED, width=2)
        draw.text((126, card_y + 60), str(idx + 1), fill=COLOR_RED, font=get_font(38, bold=True))
        
        draw.text((210, card_y + 40), prob['title'], fill=COLOR_WHITE, font=get_font(28, bold=True))
        lines = textwrap.wrap(prob['desc'], width=48)
        for line_idx, line in enumerate(lines[:3]):
            draw.text((210, card_y + 88 + (line_idx * 34)), line, fill=COLOR_LIGHT_GRAY, font=get_font(22, bold=False))

    draw.text((WIDTH // 2 - 130, HEIGHT - 110), "Çözüm İçin Kaydır  »", fill=COLOR_CYAN, font=get_font(28, bold=True))
    return img


def create_slide_3_solution(topic):
    img = Image.new("RGBA", (WIDTH, HEIGHT), COLOR_BG_DARK)
    draw = ImageDraw.Draw(img)
    draw_background(draw)
    add_header(img, draw, 3)

    draw.text((70, 180), "• DOĞRU VE HIZLI ÇÖZÜM", fill=COLOR_GREEN, font=get_font(24, bold=True))
    draw.text((70, 230), topic['solution_headline'], fill=COLOR_WHITE, font=get_font(44, bold=True))

    y_start = 340
    for idx, sol in enumerate(topic['solutions']):
        card_y = y_start + (idx * 250)
        draw.rounded_rectangle([70, card_y, WIDTH - 70, card_y + 215], radius=26, fill=COLOR_CARD_BG, outline=COLOR_CYAN, width=2)
        
        # Onay Kutusu
        draw.rounded_rectangle([100, card_y + 55, 160, card_y + 115], radius=18, fill=(34, 197, 94, 40), outline=COLOR_GREEN, width=2)
        draw_checkmark(draw, 130, card_y + 85, size=13, color=COLOR_GREEN, width=4)
        
        draw.text((190, card_y + 42), sol['title'], fill=COLOR_WHITE, font=get_font(28, bold=True))
        lines = textwrap.wrap(sol['desc'], width=52)
        for line_idx, line in enumerate(lines[:3]):
            draw.text((190, card_y + 90 + (line_idx * 34)), line, fill=COLOR_LIGHT_GRAY, font=get_font(22, bold=False))

    draw.text((WIDTH // 2 - 130, HEIGHT - 110), "Maliyeti Görün  »", fill=COLOR_CYAN, font=get_font(28, bold=True))
    return img


def create_slide_4_advantage(topic):
    img = Image.new("RGBA", (WIDTH, HEIGHT), COLOR_BG_DARK)
    draw = ImageDraw.Draw(img)
    draw_background(draw)
    add_header(img, draw, 4)

    draw.text((70, 180), "• BASTET YAZILIM AVANTAJI", fill=COLOR_YELLOW, font=get_font(24, bold=True))
    draw.text((70, 230), topic['advantage_headline'], fill=COLOR_WHITE, font=get_font(44, bold=True))

    # Fiyat / Paket Kutusu
    draw.rounded_rectangle([70, 335, WIDTH - 70, 690], radius=32, fill=(30, 41, 59, 240), outline=COLOR_CYAN, width=3)
    draw.text((115, 380), topic['price_title'], fill=COLOR_YELLOW, font=get_font(26, bold=True))
    draw.text((115, 435), topic['price_amount'], fill=COLOR_WHITE, font=get_font(72, bold=True))
    draw.text((115, 545), topic['price_subtext'], fill=COLOR_CYAN, font=get_font(28, bold=True))
    draw.text((115, 605), "Taahhüt yok · Gizli masraf yok · Anahtar teslim kullanım", fill=COLOR_LIGHT_GRAY, font=get_font(23, bold=False))

    # Karşılaştırma Kutusu
    draw.rounded_rectangle([70, 730, WIDTH - 70, 1070], radius=28, fill=COLOR_CARD_BG, outline=(75, 85, 99), width=2)
    draw.text((115, 770), topic['comparison_title'], fill=COLOR_WHITE, font=get_font(28, bold=True))
    
    bad_txt = topic['comparison_bad']
    draw.rounded_rectangle([110, 835, 148, 873], radius=10, fill=(239, 68, 68, 30), outline=COLOR_RED, width=2)
    draw_crossmark(draw, 129, 854, size=9, color=COLOR_RED, width=3)
    draw.text((165, 838), bad_txt, fill=(248, 113, 113), font=get_font(24, bold=False))
    
    good_txt = topic['comparison_good']
    draw.rounded_rectangle([110, 930, 148, 968], radius=10, fill=(34, 197, 94, 30), outline=COLOR_GREEN, width=2)
    draw_checkmark(draw, 129, 949, size=10, color=COLOR_GREEN, width=3)
    draw.text((165, 933), good_txt, fill=COLOR_GREEN, font=get_font(24, bold=True))

    draw.text((WIDTH // 2 - 130, HEIGHT - 110), "İletişime Geçin  »", fill=COLOR_CYAN, font=get_font(28, bold=True))
    return img


def create_slide_5_cta(topic):
    img = Image.new("RGBA", (WIDTH, HEIGHT), COLOR_BG_DARK)
    draw = ImageDraw.Draw(img)
    draw_background(draw)
    add_header(img, draw, 5)

    draw.text((70, 185), "• İŞLETMENİZİ BUGÜN BÜYÜTÜN", fill=COLOR_CYAN, font=get_font(24, bold=True))
    draw.text((70, 240), topic['cta_title'], fill=COLOR_WHITE, font=get_font(44, bold=True))
    draw.text((70, 325), topic['cta_subtext'], fill=COLOR_LIGHT_GRAY, font=get_font(25, bold=False))

    # Dev Yeşil WhatsApp Butonu
    btn_y = 425
    btn_h = 150
    draw.rounded_rectangle([70, btn_y, WIDTH - 70, btn_y + btn_h], radius=34, fill=COLOR_GREEN, outline=(34, 197, 94), width=2)
    
    wa_text = "WhatsApp: 0551 514 95 11  →"
    font_wa = get_font(42, bold=True)
    bbox = draw.textbbox((0, 0), wa_text, font=font_wa)
    text_w = bbox[2] - bbox[0]
    draw.text(((WIDTH - text_w) // 2, btn_y + 48), wa_text, fill=COLOR_WHITE, font=font_wa)

    # İletişim Kartı
    box_y = 625
    box_h = 420
    draw.rounded_rectangle([70, box_y, WIDTH - 70, box_y + box_h], radius=30, fill=COLOR_CARD_BG, outline=(55, 65, 81), width=2)
    
    draw.text((115, box_y + 45), "• Web Sitemiz:", fill=COLOR_CYAN, font=get_font(24, bold=True))
    draw.text((115, box_y + 90), "bastetyazilim.com", fill=COLOR_WHITE, font=get_font(38, bold=True))
    
    draw.text((115, box_y + 180), "• DM & Doğrudan Mesaj:", fill=COLOR_CYAN, font=get_font(24, bold=True))
    draw.text((115, box_y + 225), "Instagram & Facebook üzerinden hemen yazabilirsiniz.", fill=COLOR_WHITE, font=get_font(25, bold=False))
    draw.text((115, box_y + 280), "15 dakikada sektörünüze özel canlı demo sunulur.", fill=COLOR_YELLOW, font=get_font(23, bold=True))

    draw.text((WIDTH // 2 - 165, HEIGHT - 110), "Bastet Yazılım · Şeffaf & Hızlı", fill=(100, 116, 139), font=get_font(24, bold=True))
    return img


# ================= 4:5 TEK GÖRSEL POSTER / AFİŞ (1080 x 1350) =================

def create_single_poster(post_data):
    """1080x1350 (4:5 Dikey) Web Sitesi Odaklı Vurucu Tek Post / Afiş Tasarımı"""
    img = Image.new("RGBA", (WIDTH, HEIGHT), COLOR_BG_DARK)
    draw = ImageDraw.Draw(img)
    draw_background(draw)

    ensure_brand_assets()
    if os.path.exists(BY_SYMBOL_PATH):
        try:
            by_sym = Image.open(BY_SYMBOL_PATH).convert("RGBA")
            h = 68
            w = int(by_sym.width * (h / by_sym.height))
            by_resized = by_sym.resize((w, h), Image.Resampling.LANCZOS)
            img.paste(by_resized, (70, 70), by_resized)
            draw.text((70 + w + 18, 72), "BASTET", fill=COLOR_WHITE, font=get_font(28, bold=True))
            draw.text((70 + w + 18, 105), "YAZILIM", fill=COLOR_CYAN, font=get_font(20, bold=True))
        except Exception:
            pass

    # Lansman Rozeti
    draw.rounded_rectangle([WIDTH - 300, 75, WIDTH - 70, 135], radius=28, fill=(6, 182, 212, 35), outline=COLOR_CYAN, width=2)
    draw.text((WIDTH - 270, 90), "• Lansmana Özel", fill=COLOR_CYAN, font=get_font(22, bold=True))

    # Dev Başlık
    draw.text((70, 200), post_data["title_line1"], fill=COLOR_WHITE, font=get_font(50, bold=True))
    draw.text((70, 275), post_data["title_line2"], fill=COLOR_CYAN, font=get_font(56, bold=True))

    # Büyük Fiyat Kutusu
    draw.rounded_rectangle([70, 375, WIDTH - 70, 485], radius=26, fill=(30, 41, 59, 240), outline=COLOR_YELLOW, width=2)
    draw.text((110, 408), post_data["price_badge"], fill=COLOR_YELLOW, font=get_font(38, bold=True))

    # 4 Madde Kutuları (4:5 boyutta çok ferah)
    y_start = 525
    for idx, feat in enumerate(post_data["features"]):
        card_y = y_start + (idx * 135)
        draw.rounded_rectangle([70, card_y, WIDTH - 70, card_y + 115], radius=22, fill=COLOR_CARD_BG, outline=(55, 65, 81), width=2)
        draw.rounded_rectangle([95, card_y + 26, 155, card_y + 86], radius=16, fill=(34, 197, 94, 35), outline=COLOR_GREEN, width=2)
        draw_checkmark(draw, 125, card_y + 56, size=12, color=COLOR_GREEN, width=3)
        draw.text((185, card_y + 36), feat, fill=COLOR_WHITE, font=get_font(28, bold=True))

    # Dev WhatsApp Butonu
    btn_y = 1115
    draw.rounded_rectangle([70, btn_y, WIDTH - 70, btn_y + 130], radius=32, fill=COLOR_GREEN, outline=(34, 197, 94), width=2)
    cta_text = post_data["footer_cta"] + "  →"
    font_cta = get_font(40, bold=True)
    bbox = draw.textbbox((0, 0), cta_text, font=font_cta)
    btn_w = bbox[2] - bbox[0]
    draw.text(((WIDTH - btn_w) // 2, btn_y + 38), cta_text, fill=COLOR_WHITE, font=font_cta)
    return img


# ================= HİKAYE (STORY 1080x1920) =================

def create_story_graphic(story_data, day_name, is_morning=True):
    """1080x1920 (9:16 Dikey) Instagram & Facebook Story Tasarımı"""
    img = Image.new("RGBA", (STORY_WIDTH, STORY_HEIGHT), COLOR_BG_DARK)
    draw = ImageDraw.Draw(img)
    draw_background(draw, height=STORY_HEIGHT)

    ensure_brand_assets()
    if os.path.exists(BY_SYMBOL_PATH):
        try:
            by_sym = Image.open(BY_SYMBOL_PATH).convert("RGBA")
            h = 80
            w = int(by_sym.width * (h / by_sym.height))
            by_resized = by_sym.resize((w, h), Image.Resampling.LANCZOS)
            img.paste(by_resized, ((STORY_WIDTH - w) // 2 - 90, 160), by_resized)
            draw.text(((STORY_WIDTH - w) // 2 + 30, 165), "BASTET", fill=COLOR_WHITE, font=get_font(36, bold=True))
            draw.text(((STORY_WIDTH - w) // 2 + 30, 208), "YAZILIM", fill=COLOR_CYAN, font=get_font(24, bold=True))
        except Exception:
            pass

    # Üst Zaman Rozeti
    time_label = f"• {day_name.upper()} GÜNDEMİ"
    draw.rounded_rectangle([STORY_WIDTH // 2 - 180, 290, STORY_WIDTH // 2 + 180, 350], radius=30, fill=(30, 41, 59, 230), outline=COLOR_CYAN, width=2)
    draw.text((STORY_WIDTH // 2 - 140, 305), time_label, fill=COLOR_CYAN, font=get_font(24, bold=True))

    # Ana Hikaye Kartı
    box_top = 440
    box_h = 1000
    draw.rounded_rectangle([80, box_top, STORY_WIDTH - 80, box_top + box_h], radius=40, fill=COLOR_CARD_BG, outline=(55, 65, 81), width=3)

    # Başlık
    title = story_data["title"]
    title_color = COLOR_YELLOW if is_morning else COLOR_CYAN
    draw.text((130, box_top + 90), title, fill=title_color, font=get_font(36, bold=True))

    # Gövde Metni
    text_content = story_data["text"]
    paragraphs = text_content.split("\n\n")
    y_text = box_top + 180
    for para in paragraphs:
        lines = textwrap.wrap(para, width=32)
        for line in lines:
            draw.text((130, y_text), line, fill=COLOR_WHITE, font=get_font(38, bold=False))
            y_text += 58
        y_text += 30

    # Alt Buton
    cta_btn_y = box_top + box_h - 180
    cta_bg = COLOR_GREEN if not is_morning else (6, 182, 212, 40)
    cta_outline = COLOR_GREEN if not is_morning else COLOR_CYAN
    draw.rounded_rectangle([130, cta_btn_y, STORY_WIDTH - 130, cta_btn_y + 110], radius=30, fill=cta_bg, outline=cta_outline, width=2)
    cta_txt = story_data["cta"]
    font_cta = get_font(32, bold=True)
    bbox = draw.textbbox((0, 0), cta_txt, font=font_cta)
    btn_w = bbox[2] - bbox[0]
    draw.text(((STORY_WIDTH - btn_w) // 2, cta_btn_y + 35), cta_txt, fill=COLOR_WHITE, font=font_cta)

    # Alt Footer
    draw.text((STORY_WIDTH // 2 - 170, STORY_HEIGHT - 180), "bastetyazilim.com · 0551 514 95 11", fill=COLOR_GRAY, font=get_font(24, bold=True))
    return img


# ================= KAYIT & ÜRETİM FONKSİYONLARI =================

def save_image_atomic(img, file_path):
    """Görseli geçici dosyaya kaydedip atomik olarak hedef yola taşır."""
    tmp_path = file_path + ".tmp"
    rgb_img = Image.new("RGB", img.size, (10, 15, 29))
    if img.mode == "RGBA":
        rgb_img.paste(img, mask=img.split()[3])
    else:
        rgb_img.paste(img)
    rgb_img.save(tmp_path, "PNG")
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception:
        pass
    os.replace(tmp_path, file_path)


def generate_day(day_id):
    """Belirtilen günün tüm içeriklerini (4:5 Carousel + 4:5 Tek Görsel + 9:16 2 Hikaye) üretir."""
    if day_id not in SERVICES_DATA:
        raise ValueError(f"Geçersiz gün ID'si: {day_id}")

    topic = SERVICES_DATA[day_id]
    folder = os.path.join(OUTPUT_DIR, day_id)
    os.makedirs(folder, exist_ok=True)

    # 1. 4:5 Carousel Slaytları (1080x1350)
    carousel_slides = [
        create_slide_1_cover(topic),
        create_slide_2_problem(topic),
        create_slide_3_solution(topic),
        create_slide_4_advantage(topic),
        create_slide_5_cta(topic),
    ]
    carousel_paths = []
    for i, slide in enumerate(carousel_slides, 1):
        fpath = os.path.join(folder, f"slayt_{i}.png")
        save_image_atomic(slide, fpath)
        carousel_paths.append(fpath)

    # Carousel Caption
    caption_path = os.path.join(folder, "caption.txt")
    cap = topic["caption"]
    full_caption_text = f"{cap['title']}\n\n{cap['body']}\n\n{cap['cta']}\n\n{cap['hashtags']}"
    with open(caption_path, "w", encoding="utf-8") as f:
        f.write(full_caption_text)

    # 2. 4:5 Tek Görsel (Afiş) - Eğer varsa
    single_post_path = None
    if topic.get("has_single_post") and topic.get("single_post"):
        poster_img = create_single_poster(topic["single_post"])
        single_post_path = os.path.join(folder, "tek_gorsel_web.png")
        save_image_atomic(poster_img, single_post_path)
        
        poster_cap_path = os.path.join(folder, "tek_gorsel_caption.txt")
        with open(poster_cap_path, "w", encoding="utf-8") as f:
            f.write(topic["single_post"]["caption"])

    # 3. 9:16 Hikayeler (Stories - 1080x1920)
    story_morning_path = os.path.join(folder, "hikaye_sabah.png")
    story_m_img = create_story_graphic(topic["story_morning"], topic["day"], is_morning=True)
    save_image_atomic(story_m_img, story_morning_path)

    story_evening_path = os.path.join(folder, "hikaye_aksam.png")
    story_e_img = create_story_graphic(topic["story_evening"], topic["day"], is_morning=False)
    save_image_atomic(story_e_img, story_evening_path)

    # 4. Metadata JSON
    metadata_path = os.path.join(folder, "metadata.json")
    meta_info = {
        "id": topic["id"],
        "name": topic["name"],
        "day": topic["day"],
        "day_num": topic["day_num"],
        "type": topic["type"],
        "format": "4:5 (1080x1350)",
        "folder": folder,
        "carousel_slides": carousel_paths,
        "caption_file": caption_path,
        "single_post": single_post_path,
        "story_morning": story_morning_path,
        "story_evening": story_evening_path
    }
    with open(metadata_path, "w", encoding="utf-8") as f:
        json.dump(meta_info, f, ensure_ascii=False, indent=2)

    has_poster_str = " + 4:5 Tek Görsel Afiş" if single_post_path else ""
    print(f"✅ [{topic['day']}] {topic['name']} Tamamlandı: 5 Slayt 4:5 Carousel{has_poster_str} + 2 Hikaye")
    return folder, meta_info


def generate_all():
    """Tüm 7 günün 4:5 Carousel, 4:5 Afiş ve Hikayelerini üretir."""
    print("\n🚀 BASTET YAZILIM 4:5 PORTRE SOSYAL MEDYA MOTORU ÇALIŞTIRILIYOR...\n")
    results = {}
    for day_id in SERVICES_DATA:
        folder, meta = generate_day(day_id)
        results[day_id] = meta
    print(f"\n🎉 Toplam {len(results)} Günün tüm 4:5 Carousel, Afiş ve Hikayeleri üretildi!")
    return results


if __name__ == "__main__":
    generate_all()
