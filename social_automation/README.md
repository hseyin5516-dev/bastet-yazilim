# 🚀 Bastet Yazılım Sosyal Medya Carousel & Paylaşım Otomasyonu

Bastet Yazılım resmi kurumsal web sitesindeki 7 ana hizmeti, her gün için 1080x1080 piksel çözünürlüğünde, 5 slaytlık eğitici ve satış odaklı Instagram/Facebook carousel görsellerine ve açıklama metinlerine dönüştüren tam otomatik sistem.

---

## 📅 Haftalık İçerik Takvimi

| Gün | Hizmet | Fiyat / Model | Klasör |
| :--- | :--- | :--- | :--- |
| **Pazartesi** | Kurumsal Web Tasarım | 3.450 TL / 3 Günde Teslim | `output/01_web_tasarim/` |
| **Salı** | Randevu Yönetim Sistemi | 10.000 TL Tek Seferlik | `output/02_randevu/` |
| **Çarşamba** | Klinik Yönetim Sistemi | 10.000 TL Tek Seferlik | `output/03_klinik/` |
| **Perşembe** | Sade Ön Muhasebe & Kasa | 10.000 TL Tek Seferlik | `output/04_muhasebe/` |
| **Cuma** | Müşteri & CRM Takibi | 10.000 TL Tek Seferlik | `output/05_crm/` |
| **Cumartesi**| Oto Servis & Tamir Takip | 10.000 TL Tek Seferlik | `output/06_oto_servis/` |
| **Pazar** | Emlak & Portföy Yönetimi| 10.000 TL Tek Seferlik | `output/07_emlak/` |

---

## 🖼️ 5 Slaytlık Carousel Mimarisi

1. **Slayt 1 (Kanca & Kapak):** Sektörel problem sorusu, dikkat çekici başlık, değer kutusu ve "Detaylar için kaydırın" çağrısı.
2. **Slayt 2 (Acı Noktalar / Problem):** İşletmenin yaşadığı 3 kritik kayıp ve ciro kaçağı (Numaralandırılmış kartlar).
3. **Slayt 3 (Bastet Çözümü):** 4 somut çözüm özelliği, rahatlama ve verimlilik (Vektörel yeşil onay tikleri).
4. **Slayt 4 (Neden Bastet & Fiyat):** Büyük şeffaf fiyat kutusu + Klasik Ajanslar vs Bastet Yazılım karşılaştırması.
5. **Slayt 5 (Güçlü Satış CTA):** WhatsApp butonu (0551 514 95 11), web sitesi ve DM çağrısı.

---

## 💻 Kullanım Komutları

### 1. Haftalık Durumu İnceleme
```bash
python social_automation/daily_runner.py --status
```

### 2. Bugünün İçeriğini Otomatik Üretme ve Paylaşıma Hazırlama
```bash
python social_automation/daily_runner.py --today
```

### 3. Tüm Haftayı (35 Slaytı) Tek Seferde Üretme
```bash
python social_automation/daily_runner.py --all
```

### 4. Belirli Bir Hizmeti Üretme
```bash
python social_automation/daily_runner.py --service klinik --publish
```

---

## 📲 Paylaşım Yöntemleri

### Yöntem A: 1-Tıkla Meta Business Suite ile Manuel / Planlı Paylaşım
1. İlgili günün klasörünü açın (örn: `output/01_web_tasarim/`).
2. `slayt_1.png`'den `slayt_5.png`'ye kadar olan 5 görseli seçin.
3. [Meta Business Suite](https://business.facebook.com) > **Gönderi Oluştur** ekranına sürükleyin.
4. Klasördeki `caption.txt` içeriğini yapıştırın.
5. Hem Instagram hem Facebook için aynı anda "Yayınla" veya "Planla" butonuna basın.

### Yöntem B: Meta Graph API ile %100 Otomatik Paylaşım
1. `.env.example` dosyasını `.env` olarak kopyalayın.
2. Meta Developers portalından aldığınız token ve sayfa ID'lerinizi girin:
   ```env
   META_ACCESS_TOKEN=your_token
   INSTAGRAM_ACCOUNT_ID=your_id
   FACEBOOK_PAGE_ID=your_page_id
   ```
3. `python publisher.py` komutuyla doğrudan API üzerinden otomatik yayınlayın.
