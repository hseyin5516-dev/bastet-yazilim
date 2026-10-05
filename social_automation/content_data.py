"""
Bastet Yazılım Sosyal Medya İçerik ve Kampanya Veritabanı (Genişletilmiş 360° Sürüm)
Haftalık Sonsuz Döngü:
- Pazartesi: [Satış] Kurumsal Web Tasarım + [Tek Post] Web Tasarım Afişi + 2 Hikaye
- Salı: [Eğitici/Kamu Hizmeti] Google SEO & Yerel Haritalar + 2 Hikaye
- Çarşamba: [Satış] Randevu & Klinik Yönetim Sistemleri + [Tek Post] Web Tasarım Afişi + 2 Hikaye
- Perşembe: [Eğitici/Kamu Hizmeti] Meta Reklamları (WhatsApp Lead) + 2 Hikaye
- Cuma: [Satış] Sade Ön Muhasebe & CRM Takibi + [Tek Post] Web Tasarım Afişi + 2 Hikaye
- Cumartesi: [Eğitici/Kamu Hizmeti] 2026 Web Güvenlik ve Hız Standartları + [Tek Post] Web Tasarım Afişi + 2 Hikaye
- Pazar: [Satış] Oto Servis & Emlak Portföy Sistemleri + 2 Hikaye
"""

SERVICES_DATA = {
    # ================= 1. PAZARTESİ =================
    "01_pazartesi_web_tasarim": {
        "id": "01_pazartesi_web_tasarim",
        "day": "Pazartesi",
        "day_num": 1,
        "type": "sales",
        "name": "Kurumsal Web Tasarım",
        "category": "WEB & DİJİTAL DÖNÜŞÜM",
        "has_single_post": True,
        # Carousel Slayt 1 (Kapak)
        "cover_badge": "• 3 GÜNDE TESLİMAT",
        "cover_title_1": "MÜŞTERİLERİNİZ SİZİ",
        "cover_title_2": "GOOGLE'DA BULAMIYOR MU?",
        "cover_title_3": "3.450 TL'DEN BAŞLAYAN FİYATLARLA",
        "cover_highlight_badge": "• GOOGLE CORE VITALS: 99/100 HIZ",
        "cover_highlight_text": "Mobil Uyumlu & WhatsApp Sipariş Butonlu",
        "cover_subtext": "Ajanslara servet ödemeden profesyonel kurumsal vitrin.",
        # Carousel Slayt 2 (Problem)
        "problem_headline": "Web Siteniz Yoksa veya Yavaşsa...",
        "problems": [
            {
                "title": "Müşteriler Rakiplerinize Gidiyor",
                "desc": "Google'da arayan potansiyel müşterilerin %84'ü kurumsal web sitesi olmayana güvenmiyor."
            },
            {
                "title": "Sosyal Medya Tek Başına Yetmiyor",
                "desc": "Profil linkinizde güven veren bir web sayfası veya ürün kataloğu yoksa satış kaçıyor."
            },
            {
                "title": "Eski Siteler Mobilde Açılmıyor",
                "desc": "3 saniyeden geç açılan siteleri kullanıcıların %53'ü hemen terk ediyor."
            }
        ],
        # Carousel Slayt 3 (Çözüm)
        "solution_headline": "Bastet Yazılım ile 3 Günde Çözüm!",
        "solutions": [
            {
                "title": "Yüksek Hızlı Modern Tasarım",
                "desc": "Google Hız Skoru 99/100 olan, telefonda anında açılan temiz kodlama."
            },
            {
                "title": "WhatsApp Doğrudan Sipariş Butonu",
                "desc": "Ziyaretçiyi formlarla yormadan tek tıkla doğrudan WhatsApp hattınıza bağlar."
            },
            {
                "title": ".com Alan Adı + 1 Yıl Hosting Dahil",
                "desc": "Gizli ek masraf yok; alan adı, kurumsal e-posta ve SSL güvenliği hazır teslim."
            },
            {
                "title": "1 Ay Ücretsiz Revizyon & Destek",
                "desc": "Site tesliminden sonra yalnız değilsiniz, doğrudan WhatsApp teknik destek."
            }
        ],
        # Carousel Slayt 4 (Fiyat & Neden Bastet)
        "advantage_headline": "Şeffaf Fiyat, Sıfır Sürpriz",
        "price_title": "BAŞLANGIÇ WEB PAKETİ",
        "price_amount": "3.450 TL",
        "price_subtext": "Tek Seferlik Kurulum · 3 İş Gününde Hızlı Teslim",
        "comparison_title": "Piyasa Ajansları vs Bastet Yazılım",
        "comparison_bad": "Klasik Ajanslar: 25.000 TL+ teklifler ve haftalarca süren gecikme",
        "comparison_good": "Bastet Yazılım: 3.450 TL net fiyat, 3 günde teslim, doğrudan destek",
        # Carousel Slayt 5 (CTA)
        "cta_title": "Web Sitenizi Bu Hafta Canlıya Alalım!",
        "cta_subtext": "Sektörünüze özel hazır demolarımızı ve ücretsiz analizimizi WhatsApp'tan hemen inceleyin.",
        # Carousel Açıklama Metni
        "caption": {
            "title": "🌐 Müşterileriniz Google'da sizi arattığında kimi buluyor? Rakiplerinizi mi?",
            "body": """İşletmenizin kurumsal bir web sitesi yoksa veya siteniz cep telefonunda yavaş açılıyorsa her gün onlarca potansiyel müşteri kaybediyorsunuz.

Klasik ajansların haftalarca bekletip fahiş fiyatlar çıkardığı devir kapandı!

Bastet Yazılım olarak:
✅ Google Core Web Vitals 99/100 şimşek hızında altyapı
✅ %100 Mobil uyumlu & modern arayüz
✅ WhatsApp doğrudan sipariş ve teklif butonu
✅ .com Alan adı + Kurumsal hosting dahil
✅ 3 iş gününde anahtar teslim

💰 Sadece 3.450 TL'den başlayan şeffaf fiyatlarla! Sürpriz masraf, gizli ücret yok.""",
            "cta": """📲 Canlı demolarımızı görmek ve işletmenize özel ücretsiz teklif almak için profildeki linke tıklayın veya WhatsApp'tan yazın:
WhatsApp: 0551 514 95 11
Web: bastetyazilim.com""",
            "hashtags": "#webtasarım #bastetyazilim #kurumsalsite #kobilereözel #dijitaldönüşüm #websitesi #yazılım #eticaret #ankarayazılım #istanbulyazılım #küçükişletme"
        },
        # Tek Görsel (Afiş)
        "single_post": {
            "title_line1": "KURUMSAL WEB SİTESİ",
            "title_line2": "3 GÜNDE TESLİM",
            "price_badge": "3.450 TL'DEN BAŞLAYAN FİYATLARLA",
            "features": [
                "Google Core Web Vitals 99/100 Hız Skoru",
                ".com Alan Adı ve 1 Yıl Hosting Dahil",
                "WhatsApp Doğrudan Sipariş Entegrasyonu",
                "Mobil Uyumlu & Güvenli SSL Sertifikalı"
            ],
            "footer_cta": "WhatsApp: 0551 514 95 11",
            "caption": """🚀 İşletmenizi internete taşımanın en hızlı ve ekonomik yolu!

3 günde anahtar teslim kurumsal web sitesi sadece 3.450 TL'den başlayan fiyatlarla.

✅ Google hız skoru 99/100
✅ .com alan adı ve hosting dahil
✅ WhatsApp doğrudan sipariş butonu

📲 Detaylar ve canlı demolar için hemen WhatsApp'tan yazın: 0551 514 95 11
Web: bastetyazilim.com

#webtasarım #bastetyazilim #kurumsalsite #kobi #esnaf #dijitalpazarlama"""
        },
        # Günlük Hikayeler
        "story_morning": {
            "title": "GÜNÜN DİJİTAL İPUCU 💡",
            "text": "Sitenizin cep telefonunda 3 saniyeden geç açılması, potansiyel müşterilerin %53'ünün sayfayı terk etmesine neden olur.\n\nSizinki ne kadar hızlı?",
            "cta": "Hız testi için profilimize göz atın ➔"
        },
        "story_evening": {
            "title": "CANLI DEMO ZAMANI 🚀",
            "text": "Bugün yeni bir sektörel web sitesi demosu hazırladık!\n\nKendi sektörünüze özel tasarımı canlı incelemek ister misiniz?",
            "cta": "DM'den 'DEMO' yazın iletelim 📲"
        }
    },

    # ================= 2. SALI =================
    "02_sali_google_seo": {
        "id": "02_sali_google_seo",
        "day": "Salı",
        "day_num": 2,
        "type": "educational",
        "name": "Google SEO & Harita Sıralaması",
        "category": "REKABET & ARAMA MOTORU OPTİMİZASYONU",
        "has_single_post": False,
        # Carousel Slayt 1 (Kapak)
        "cover_badge": "• ÜCRETSİZ MÜŞTERİ ÇEKME REHBERİ",
        "cover_title_1": "GOOGLE HARİTALAR'DA",
        "cover_title_2": "1. SIRAYA ÇIKMANIN",
        "cover_title_3": "5 ALTIN KURALI",
        "cover_highlight_badge": "• REKLAMSIZ DOĞAL MÜŞTERİ AKIŞI",
        "cover_highlight_text": "Bütçe Harcamadan İlk Sırada Yer Alın",
        "cover_subtext": "Yakınınızdaki müşterileri dükkanınıza ve sitenize çekin.",
        # Carousel Slayt 2 (Problem)
        "problem_headline": "Haritalarda Görünmemenin Maliyeti",
        "problems": [
            {
                "title": "En Sıcak Müşteriyi Kaçırmak",
                "desc": "'En yakın oto servis' veya 'diş kliniği' yazanların %78'i ilk 3 işletmeyi arar."
            },
            {
                "title": "Eksik Bilgiler ve Güven Kaybı",
                "desc": "Çalışma saati, web sitesi linki veya telefon numarası güncel olmayan profile gidilmez."
            },
            {
                "title": "Yanıtsız Kalan Yorumlar",
                "desc": "Google algoritması, müşteri yorumlarına yanıt vermeyen işletmeleri geriye iter."
            }
        ],
        # Carousel Slayt 3 (Çözüm / Taktikler)
        "solution_headline": "Uygulamanız Gereken 5 Taktik",
        "solutions": [
            {
                "title": "1. İşletme Başlığına Semt Ekleyin",
                "desc": "Örn: 'Bastet Kuaför - Kadıköy'. Arama yapan bölgesel kitleyle birebir eşleşir."
            },
            {
                "title": "2. Doğru Alt Kategorileri Seçin",
                "desc": "Sadece genel kategori değil; 3-4 adet detaylı alt hizmet kategorisi tanımlayın."
            },
            {
                "title": "3. Haftalık Fotoğraf & Gönderi Yükleyin",
                "desc": "Google güncel profilleri sever. Haftada 2 yeni fotoğraf yüklemek sıralamayı uçurur."
            },
            {
                "title": "4. Web Sitenizi Profile Bağlayın",
                "desc": "Harita profilinden web sitesine yönlendirme olması harita otoritesini 2 katına çıkarır."
            }
        ],
        # Carousel Slayt 4 (Neden SEO & Değer)
        "advantage_headline": "Sürekli Reklam Ücreti Ödemeyin",
        "price_title": "ORGANİK SEO GÜCÜ",
        "price_amount": "ÖMÜR BOYU TRAFİK",
        "price_subtext": "Bir Kez Doğru Yapılandırın · Yıllarca Ücretsiz Müşteri Kazanın",
        "comparison_title": "Reklam Vermek vs Organik SEO",
        "comparison_bad": "Sadece Reklam: Bütçe bittiği gün telefonlar çalmayı anında keser.",
        "comparison_good": "Google SEO: Reklam vermeseniz bile her gün haritadan ve aramadan müşteri gelir.",
        # Carousel Slayt 5 (CTA)
        "cta_title": "İşletmenizin SEO Durumunu İnceleyelim!",
        "cta_subtext": "Sitenizin ve Google profilinizin eksiklerini öğrenmek için bize WhatsApp'tan yazabilirsiniz.",
        # Açıklama Metni
        "caption": {
            "title": "📍 Google'da semtinizdeki müşteriler arama yaptığında dükkanınız ilk 3'te çıkıyor mu?",
            "body": """İşletmeniz için yapabileceğiniz en karlı yatırım; haritalarda ve Google aramasında rakiplerinizin üstünde yer almaktır!

Çünkü haritalardan arayan müşteri 'hemen satın almaya hazır' en sıcak müşteridir.

Profilinizi 1. sıraya taşımak için bu 4 adımı uygulayın:
1️⃣ İşletme başlığınıza bulunduğunuz semti veya ana hizmeti ekleyin.
2️⃣ Müşterilerinizden mutlaka yıldızlı yorum isteyin ve her yoruma nazikçe yanıt verin.
3️⃣ Haftada en az 1-2 gerçek iş fotoğrafı paylaşarak profilinizi canlı tutun.
4️⃣ Harita profilinize mobil uyumlu hızlı bir web sitesi linki bağlayın.

Bastet Yazılım olarak web sitelerimizi Google'ın en sevdiği teknik SEO altyapısıyla teslim ediyoruz!""",
            "cta": """📲 Sitenizin Google uyumluluğunu ücretsiz kontrol ettirmek için WhatsApp'tan yazın:
WhatsApp: 0551 514 95 11
Web: bastetyazilim.com""",
            "hashtags": "#googleseo #haritalar #yerelseo #esnafrehberi #küçükişletme #dijitalpazarlama #bastetyazilim #kobi #organiktrafik #googleharitalar"
        },
        # Günlük Hikayeler
        "story_morning": {
            "title": "BİLİYOR MUYDUNUZ? 🔍",
            "text": "Google Haritalar'da yapılan aramaların %76'sı aynı gün içinde o işletmeyi ziyaret etmekle sonuçlanıyor.\n\nHarita profiliniz güncel mi?",
            "cta": "Detaylar bugünkü carousel gönderimizde!"
        },
        "story_evening": {
            "title": "ÜCRETSİZ ANALİZ FIRSATI 🎁",
            "text": "Web sitenizin Google Core Web Vitals ve yerel SEO puanını ücretsiz analiz etmemizi ister misiniz?",
            "cta": "WhatsApp'tan site linkinizi atın inceleyelim 📲"
        }
    },

    # ================= 3. ÇARŞAMBA =================
    "03_carsamba_randevu_klinik": {
        "id": "03_carsamba_randevu_klinik",
        "day": "Çarşamba",
        "day_num": 3,
        "type": "sales",
        "name": "Randevu & Klinik Sistemleri",
        "category": "REZERVASYON & SAĞLIK YÖNETİMİ",
        "has_single_post": True,
        # Carousel Slayt 1 (Kapak)
        "cover_badge": "• UNUTULAN SEANSLARA SON",
        "cover_title_1": "RANDEVULAR KARIŞIYOR,",
        "cover_title_2": "GELMEYEN HASTALAR",
        "cover_title_3": "ZARAR MI ETTİRİYOR?",
        "cover_highlight_badge": "• OTOMATİK WHATSAPP & SMS HATIRLATMA",
        "cover_highlight_text": "Hasta Kartı, Seans & Kasa Takibi",
        "cover_subtext": "Kuaför, güzellik salonu, diş ve veteriner klinikleri için.",
        # Carousel Slayt 2 (Problem)
        "problem_headline": "Defterde Randevu Tutmanın Bedeli",
        "problems": [
            {
                "title": "Gelmeyen Müşteriler (No-Show)",
                "desc": "Randevusunu unutan müşteriler yüzünden koltuğunuz ve hekim seansınız boş kalıyor."
            },
            {
                "title": "Taksit ve Ödeme Kaçakları",
                "desc": "Seanslı tedavilerde hangi hastanın ne kadar borcu kaldığı hesaplanamıyor."
            },
            {
                "title": "Mesai Dışı Randevu Kaçırma",
                "desc": "Akşam saatlerinde mesaj atan hastalar hemen yanıt alamayınca başkasına gidiyor."
            }
        ],
        # Carousel Slayt 3 (Çözüm)
        "solution_headline": "Bastet Sistemleri ile Tam Kontrol",
        "solutions": [
            {
                "title": "7/24 Online Randevu Alma",
                "desc": "Müşterileriniz profil linkinizden boş saatleri görüp 30 saniyede randevu oluşturur."
            },
            {
                "title": "Otomatik WhatsApp / SMS Bildirimi",
                "desc": "Randevudan 2 saat önce otomatik hatırlatma gider; gelmeme oranı %90 azalır."
            },
            {
                "title": "Dijital Hasta Kartı & Tedavi Planı",
                "desc": "Hasta şikayeti, seans geçmişi ve taksitli ödeme dökümü tek ekranda."
            },
            {
                "title": "Entegre Kasa & Gelir Takibi",
                "desc": "Gün sonunda hangi hizmetten ne kadar ciro yapıldığını tek tıkla görün."
            }
        ],
        # Carousel Slayt 4 (Fiyat & Neden Bastet)
        "advantage_headline": "Aylık Kira Yok, Tek Seferlik Ödeme!",
        "price_title": "LİSANS PAKETİ",
        "price_amount": "10.000 TL",
        "price_subtext": "Tek Seferlik Ödeme · Sınırsız Kullanım · Sıfır Komisyon",
        "comparison_title": "Aylık Kira Yazılımları vs Bastet Yazılım",
        "comparison_bad": "Diğerleri: Her ay 1.500 - 3.000 TL kira + randevu başı ek komisyon",
        "comparison_good": "Bastet Yazılım: Yalnızca 10.000 TL tek seferlik! Ömür boyu sınırsız kullanım.",
        # Carousel Slayt 5 (CTA)
        "cta_title": "İşletmenizi Dijitalleştirin, Zaman Kazanın!",
        "cta_subtext": "Canlı demo panelini 10 dakikada telefonunuzda test etmek için WhatsApp'tan yazın.",
        # Açıklama Metni
        "caption": {
            "title": "🗓️ Randevusuna gelmeyen müşteriler yüzünden ayda ne kadar ciro kaybediyorsunuz?",
            "body": """Kuaförler, güzellik merkezleri, diyetisyenler ve klinikler için randevu kaçırmak en büyük gizli maliyettir!

Defterde karışan saatler, WhatsApp mesajlarında kaybolan talepler ve seansını unutan hastalar...

Bastet Randevu & Klinik Yönetim Sistemi ile tüm süreci otomatiğe bağlayın:
✨ Müşterileriniz 7/24 profil linkinizden boş saati seçip anında randevu alsın.
✨ Randevudan önce otomatik WhatsApp/SMS hatırlatması gitsin.
✨ Hasta kartı, seans takvimi ve tedavi planı kayıt altında olsun.
✨ Günlük ve aylık kasa cironuz cebinize gelsin.

🔥 En iyi haber: Aylık kira veya komisyon YOK! Tek seferlik 10.000 TL ile ömür boyu kullanım.""",
            "cta": """📲 Canlı demoyu denemek için hemen WhatsApp'tan mesaj atın:
WhatsApp: 0551 514 95 11
Web: bastetyazilim.com""",
            "hashtags": "#randevusistemi #klinikyazılımı #kuaförrandevu #güzellikmerkezi #dişkliniği #bastetyazilim #esnafyazılımı #otomasyon"
        },
        # Tek Görsel (Afiş)
        "single_post": {
            "title_line1": "KURUMSAL WEB SİTESİ",
            "title_line2": "3 GÜNDE TESLİM",
            "price_badge": "3.450 TL'DEN BAŞLAYAN FİYATLARLA",
            "features": [
                "Gereksiz Ajans Masraflarına Son",
                "Google'da Rakiplerinizin Önüne Geçin",
                "Doğrudan WhatsApp Sipariş Butonu",
                "1 Ay Ücretsiz Teknik Destek"
            ],
            "footer_cta": "WhatsApp: 0551 514 95 11",
            "caption": """💎 İşletmenizin dijital dünyadaki en güçlü vitrini!

3 günde teslim, şeffaf sabit fiyat garantili modern web sitesi.

🚀 Sadece 3.450 TL'den başlayan fiyatlarla!

📲 WhatsApp: 0551 514 95 11
Web: bastetyazilim.com

#webtasarım #bastetyazilim #kobi #girişimcilik #websitesi"""
        },
        # Günlük Hikayeler
        "story_morning": {
            "title": "NO-SHOW PROBLEMİNE SON ⏰",
            "text": "Müşterilerinize randevudan 2 saat önce otomatik WhatsApp hatırlatması gitseydi bugün kaç boş seansınız dolardı?",
            "cta": "Cevap: En az %85 daha fazla verim!"
        },
        "story_evening": {
            "title": "CANLI KLİNİK DEMOSU 🩺",
            "text": "Diş hekimleri ve klinikler için hazırladığımız hasta kartı & seans takip demosunu inceleyin.",
            "cta": "Hemen DM'den yazın canlı link atalım 📲"
        }
    },

    # ================= 4. PERŞEMBE =================
    "04_persembe_meta_reklamlari": {
        "id": "04_persembe_meta_reklamlari",
        "day": "Perşembe",
        "day_num": 4,
        "type": "educational",
        "name": "Meta Reklamları & Satış Stratejisi",
        "category": "DİJİTAL PAZARLAMA & REKLAM OPTİMİZASYONU",
        "has_single_post": False,
        # Carousel Slayt 1 (Kapak)
        "cover_badge": "• BÜTÇENİZİ ÇÖPE ATMAYIN",
        "cover_title_1": "INSTAGRAM REKLAMLARINIZ",
        "cover_title_2": "NEDEN SATIŞA",
        "cover_title_3": "DÖNÜŞMÜYOR?",
        "cover_highlight_badge": "• BEĞENİ DEĞİL MÜŞTERİ KAZANIN",
        "cover_highlight_text": "Doğrudan WhatsApp Lead Reklamının Gücü",
        "cover_subtext": "Boşa harcanan reklam bütçelerine son verin.",
        # Carousel Slayt 2 (Problem)
        "problem_headline": "İşletmelerin Yaptığı 3 Büyük Reklam Hatası",
        "problems": [
            {
                "title": "'Gönderiyi Öne Çıkar' Tuzağı",
                "desc": "Mavi butona basmak sadece beğeni getirir; işletmenize gerçek alıcı kazandırmaz."
            },
            {
                "title": "Yanlış Hedef Kitle ve Bölge",
                "desc": "Lokasyon kısıtlaması yapılmayan reklamlar hizmet veremeyeceğiniz şehirlere bütçe yakar."
            },
            {
                "title": "Net Eylem Çağrısı (CTA) Eksikliği",
                "desc": "Reklamı gören müşteriye 'Hemen WhatsApp'tan yaz' gibi net bir yönlendirme verilmiyor."
            }
        ],
        # Carousel Slayt 3 (Çözüm / Taktikler)
        "solution_headline": "Dönüşümü 3 Katına Çıkaran Taktikler",
        "solutions": [
            {
                "title": "Meta Ads Manager Kullanın",
                "desc": "Kampanyanızı detaylı hedef kitle, yaş ve ilgi alanlarıyla Ads Manager'dan kurun."
            },
            {
                "title": "WhatsApp Doğrudan Mesaj Kampanyası",
                "desc": "Müşterinin form doldurmasını beklemeden tek tıkla WhatsApp sohbetinize yönlendirin."
            },
            {
                "title": "İlk 3 Saniyede Acı Noktayı Vurun",
                "desc": "Görsel veya videonuzun başında sektörün en büyük problemini kanca olarak kullanın."
            },
            {
                "title": "Şeffaf Fiyat veya Çekici Fırsat Sunun",
                "desc": "Fiyatı gizlemek güveni azaltır; '3.450 TL'den başlayan' gibi net teklif verin."
            }
        ],
        # Carousel Slayt 4 (Neden Meta Reklam Yönetimi)
        "advantage_headline": "Reklam Bütçenizi Akıllıca Yönetin",
        "price_title": "META REKLAM YÖNETİMİ",
        "price_amount": "1.990 TL / AY",
        "price_subtext": "Haftalık Raporlama · Hedef Kitle Optimizasyonu · Görsel Tasarım",
        "comparison_title": "Kendi Başına Reklam vs Profesyonel Yönetim",
        "comparison_bad": "Deneme-Yanılma: Binlerce lira bütçe harcanır, sadece boş beğeniler gelir.",
        "comparison_good": "Bastet Reklam Yönetimi: Doğrudan WhatsApp'a düşen sıcak müşteri mesajları.",
        # Carousel Slayt 5 (CTA)
        "cta_title": "Reklamlarınız Satış Getirmeye Başlasın!",
        "cta_subtext": "İşletmenizin reklam analizini yapmak ve profesyonel kampanya kurmak için bize yazın.",
        # Açıklama Metni
        "caption": {
            "title": "📈 Instagram'a her ay reklam parası yatırıp karşılığında sadece boş beğeni mi alıyorsunuz?",
            "body": """İşletme sahiplerinin en sık düştüğü hata: 'Gönderiyi Öne Çıkar' butonuna basıp reklamın satış getirmesini beklemektir!

Oysa o buton Meta algoritmasına 'bana sadece beğenecek kişileri bul' der, 'satın alacak müşteriyi bul' demez.

Gerçekten satış getiren Meta reklamı nasıl kurulur?
1️⃣ Kampanyanızı Ads Manager üzerinden 'Potansiyel Müşteri' veya 'Mesajlar' hedefiyle kurun.
2️⃣ Reklamı gören kişiyi doğrudan WhatsApp hattınıza bağlayın.
3️⃣ Reklam görselinde merak uyandıran bir kanca ve net bir fiyat avantajı verin.
4️⃣ Sadece hizmet verdiğiniz şehir ve hedef yaş grubuna bütçe ayırın.

Bastet Yazılım olarak hem web sitenizi kuruyor hem de Meta reklamlarınızı yönetiyoruz!""",
            "cta": """📲 Reklam bütçenizi kara geçirmek için hemen iletişime geçin:
WhatsApp: 0551 514 95 11
Web: bastetyazilim.com""",
            "hashtags": "#metareklamları #instagramreklam #dijitalpazarlama #satışartırma #leadreklam #reklamyönetimi #bastetyazilim #kobi #esnaf"
        },
        # Günlük Hikayeler
        "story_morning": {
            "title": "REKLAM TÜYOSU 🎯",
            "text": "Instagram'da 'Gönderiyi Öne Çıkar' butonuna basmak bütçenizi beğeniye harcar.\n\nSatış için doğrudan WhatsApp Lead reklamı kullanmalısınız!",
            "cta": "Ayrıntılar bugünkü gönderimizde ➔"
        },
        "story_evening": {
            "title": "REKLAM DANIŞMANLIĞI 📊",
            "text": "Mevcut reklamlarınızı birlikte inceleyelim. Nerede bütçe kaçağı var 15 dakikada tespit edelim.",
            "cta": "WhatsApp'tan mesaj atın görüşelim 📲"
        }
    },

    # ================= 5. CUMA =================
    "05_cuma_muhasebe_crm": {
        "id": "05_cuma_muhasebe_crm",
        "day": "Cuma",
        "day_num": 5,
        "type": "sales",
        "name": "Sade Ön Muhasebe & CRM",
        "category": "FİNANS, CARİ & SATIŞ YÖNETİMİ",
        "has_single_post": True,
        # Carousel Slayt 1 (Kapak)
        "cover_badge": "• EXCEL VE UNUTULAN TEKLİFLERE SON",
        "cover_title_1": "KİMİN NE KADAR BORCU VAR,",
        "cover_title_2": "KASADA GERÇEKTE NE KALDI",
        "cover_title_3": "BİLEMİYOR MUSUNUZ?",
        "cover_highlight_badge": "• CARİ BORÇ-ALACAK & SATIŞ PIPELINE",
        "cover_highlight_text": "PDF Teklif, Kasa & Müşteri Takibi",
        "cover_subtext": "Toptancılar, imalatçılar, B2B ve teklif usulü çalışanlar için.",
        # Carousel Slayt 2 (Problem)
        "problem_headline": "Tablolarda Kaybolan Paralar ve Satışlar",
        "problems": [
            {
                "title": "Unutulan Alacaklar & Geciken Ödemeler",
                "desc": "Müşterinin hangi faturayı ne zaman ödeyeceği takip edilemeyince nakit akışı bozulur."
            },
            {
                "title": "Takip Edilmeyen Teklifler",
                "desc": "Teklif verildikten sonra geri aranmayan müşteriler hemen rakip firmaya yönelir."
            },
            {
                "title": "Hantal Muhasebe Programları",
                "desc": "Büyük yazılımların yüzlerce gereksiz menüsü içinde personelin kafası karışır."
            }
        ],
        # Carousel Slayt 3 (Çözüm)
        "solution_headline": "Bastet Ön Muhasebe & CRM Çözümü",
        "solutions": [
            {
                "title": "Tek Tıkla Kurumsal PDF Teklif",
                "desc": "Firmanızın logosuyla dakikalar içinde şık teklif ve sipariş formu oluşturun."
            },
            {
                "title": "Net Cari Hesap & Bakiye Takibi",
                "desc": "Kimden ne kadar alacağınız var, hangi tedarikçiye borcunuz var anında görün."
            },
            {
                "title": "Görsel Satış Hattı (Pipeline)",
                "desc": "Aday, Görüşüldü, Teklif Verildi, Kazanıldı aşamalarını sürükle-bırak yönetin."
            },
            {
                "title": "Telefondan & Bilgisayardan Erişim",
                "desc": "Dükkanda değilken bile telefonunuzdan kasanızı ve cari durumunuzu inceleyin."
            }
        ],
        # Carousel Slayt 4 (Fiyat & Neden Bastet)
        "advantage_headline": "Yıllık Bakım Ücreti Yok, Net Fiyat",
        "price_title": "ÖN MUHASEBE & CRM LİSANSI",
        "price_amount": "10.000 TL",
        "price_subtext": "Tek Seferlik Kurulum · Sınırsız Cari, Teklif ve Müşteri",
        "comparison_title": "Bulut Abonelikleri vs Bastet",
        "comparison_bad": "Abonelikli Sistemler: Her yıl 15.000 TL+ kira, kullanıcı başı dolar faturası",
        "comparison_good": "Bastet Yazılım: Yalnızca 10.000 TL tek seferlik! Sınırsız cari, sınırsız teklif.",
        # Carousel Slayt 5 (CTA)
        "cta_title": "Nakit Akışınızı ve Satışlarınızı Netleştirin!",
        "cta_subtext": "Ön muhasebe ve CRM arayüzünü canlı incelemek için WhatsApp'tan yazın.",
        # Açıklama Metni
        "caption": {
            "title": "💰 Kimin size ne kadar borcu olduğunu görmek için 5 farklı Excel dosyası mı açıyorsunuz?",
            "body": """Küçük ve orta ölçekli işletmelerin yaşadığı en büyük sorun: Nakit akışının ve giden tekliflerin düzenli takip edilememesidir!

Piyasadaki muhasebe ve CRM programları hem aşırı pahalı hem de kullanıcı başına her ay dolarla fatura kesiyor.

Bastet Sade Ön Muhasebe & CRM ile:
📄 Şirket logonuzla profesyonel PDF teklifler hazırlayın.
📈 Hangi müşterinin ne kadar borcu kaldığını tek bakışta görün.
📌 Teklif verilen müşterilerin takip tarihlerini kaçırmayın.
📱 Cep telefonunuzdan anında kasanızı kontrol edin.

Yıllık abonelik yenilemesi yok! 10.000 TL tek seferlik ödeme ile işletmenize teslim.""",
            "cta": """📲 Canlı demoyu görmek için hemen WhatsApp'tan mesaj atın:
WhatsApp: 0551 514 95 11
Web: bastetyazilim.com""",
            "hashtags": "#önmuhasebe #crm #caritakip #kasahesabı #pdfteklif #bastetyazilim #esnafmuhasebe #nakitakışı #satışyönetimi #küçükişletme"
        },
        # Tek Görsel (Afiş)
        "single_post": {
            "title_line1": "KURUMSAL WEB SİTESİ",
            "title_line2": "3 GÜNDE TESLİM",
            "price_badge": "3.450 TL'DEN BAŞLAYAN FİYATLARLA",
            "features": [
                "Mobil Uyumlu & Şimşek Hızında",
                ".com Alan Adı + Kurumsal Hosting",
                "WhatsApp Doğrudan Teklif Hattı",
                "Gizli Masraf veya Yıllık Aidat Yok"
            ],
            "footer_cta": "WhatsApp: 0551 514 95 11",
            "caption": """🚀 İşinizi dijitale taşıyın, satışlarınızı artırın!

3 günde teslim kurumsal web tasarımı 3.450 TL'den başlayan fiyatlarla.

📲 WhatsApp: 0551 514 95 11
Web: bastetyazilim.com

#webtasarım #bastetyazilim #kobi #esnaf #websitesi"""
        },
        # Günlük Hikayeler
        "story_morning": {
            "title": "CUMA NAKİT KONTROLÜ 💵",
            "text": "Bu hafta hangi müşterilerden alacağınız vardı, hangileri tahsil edildi?\n\nExcel'de boğulmak yerine tek ekranda görün!",
            "cta": "Ön Muhasebe demomuz için DM atın ➔"
        },
        "story_evening": {
            "title": "HAFTA SONU KAMPANYASI 🔥",
            "text": "Web sitenizi bu hafta sonu sipariş verin, Pazartesi günü canlıya alalım!",
            "cta": "Hemen WhatsApp'tan yazın: 0551 514 95 11 📲"
        }
    },

    # ================= 6. CUMARTESİ =================
    "06_cumartesi_web_guvenlik_hiz": {
        "id": "06_cumartesi_web_guvenlik_hiz",
        "day": "Cumartesi",
        "day_num": 6,
        "type": "educational",
        "name": "Web Güvenliği & Hız Standartları",
        "category": "DİJİTAL GÜVENLİK & KULLANICI DENEYİMİ",
        "has_single_post": True,
        # Carousel Slayt 1 (Kapak)
        "cover_badge": "• 2026 DİJİTAL STANDARTLARI",
        "cover_title_1": "BİR WEB SİTESİNDE",
        "cover_title_2": "MUTLAKA OLMASI GEREKEN",
        "cover_title_3": "4 HAYATİ UNSUR",
        "cover_highlight_badge": "• MÜŞTERİ GÜVENİ VE HIZ",
        "cover_highlight_text": "Ziyaretçiyi Müşteriye Dönüştüren Detaylar",
        "cover_subtext": "Siteniz bu kriterleri karşılıyor mu? Kontrol edin.",
        # Carousel Slayt 2 (Problem)
        "problem_headline": "Ziyaretçilerin Siteyi Terk Etme Nedenleri",
        "problems": [
            {
                "title": "'Güvenli Değil' Uyarısı (SSL Yokluğu)",
                "desc": "Tarayıcıda kilit simgesi olmayan sitelerden kullanıcılar anında kaçar."
            },
            {
                "title": "Mobilde Kayan ve Bozuk Menüler",
                "desc": "Trafiğin %80'i telefondan gelir. Mobilde düzgün çalışmayan site para kaybettirir."
            },
            {
                "title": "İletişim Kurmanın İşkence Olması",
                "desc": "10 satırlı formlar yerine tek tıkla WhatsApp bağlantısı aranıyor."
            }
        ],
        # Carousel Slayt 3 (Çözüm / Standartlar)
        "solution_headline": "Modern Bir Sitede Olması Gerekenler",
        "solutions": [
            {
                "title": "1. 256-Bit SSL Sertifikası",
                "desc": "Adres çubuğunda yeşil kilit simgesi ve tam veri şifreleme güvenliği."
            },
            {
                "title": "2. Google Core Web Vitals 90+ Hız",
                "desc": "Gereksiz eklentilerden arındırılmış, hafif ve şimşek hızında kod mimarisi."
            },
            {
                "title": "3. WhatsApp Doğrudan Sipariş Butonu",
                "desc": "Sağ altta her an erişilebilir canlı iletişim butonu dönüşümü %60 artırır."
            },
            {
                "title": "4. Şeffaf Referans ve Fiyat Politikası",
                "desc": "Kullanıcıya neyi ne kadara alacağını açıkça söyleyen dürüst tasarım."
            }
        ],
        # Carousel Slayt 4 (Bastet Standartları)
        "advantage_headline": "Bastet Yazılım Tüm Sitelerinde Standart Sunar",
        "price_title": "TAM STANDART PAKET",
        "price_amount": "HER SİTEDE DAHİL",
        "price_subtext": "SSL + 99 Hız Skoru + WhatsApp + Mobil Uyum Ek Ücretsizdir",
        "comparison_title": "Eski Siteler vs Bastet Web Altyapısı",
        "comparison_bad": "Eski Siteler: Yavaş, güvenlik sertifikası eksik, mobilde bozuk görüntü.",
        "comparison_good": "Bastet Altyapısı: Bulut sunucu hızında, 256-bit güvenli, kusursuz mobil.",
        # Carousel Slayt 5 (CTA)
        "cta_title": "Sitenizi 2026 Standartlarına Taşıyalım!",
        "cta_subtext": "Mevcut sitenizin güvenlik ve hız kontrolünü ücretsiz yaptırmak için bize yazın.",
        # Açıklama Metni
        "caption": {
            "title": "🔒 Ziyaretçilerinizin web sitenizden 5 saniyede çıkıp gitmesinin sebebi ne olabilir?",
            "body": """Kullanıcıların bir web sitesine güvenip sipariş vermesi için sadece 3 saniyeniz var!

Eğer siteniz bu 4 temel kriteri karşılamıyorsa her gün müşteri kaybediyorsunuz demektir:
1️⃣ 256-bit SSL Sertifikası (Adres çubuğunda güvenli kilit simgesi)
2️⃣ Maksimum 2 saniyede açılan Google Core Web Vitals uyumlu altyapı
3️⃣ %100 kusursuz mobil uyumluluk
4️⃣ Tek tıkla doğrudan WhatsApp'a bağlanan sipariş butonu

Bastet Yazılım olarak hazırladığımız tüm web sitelerinde bu 4 standardı ek ücret talep etmeden hazır sunuyoruz!""",
            "cta": """📲 Web sitenizi 3 günde 2026 standartlarında yenilemek için yazın:
WhatsApp: 0551 514 95 11
Web: bastetyazilim.com""",
            "hashtags": "#webgüvenlik #ssl #hızlısite #kullanıcıdeneyimi #webtasarım #bastetyazilim #kobi #esnaf #googlehız"
        },
        # Tek Görsel (Afiş)
        "single_post": {
            "title_line1": "KURUMSAL WEB SİTESİ",
            "title_line2": "3 GÜNDE TESLİM",
            "price_badge": "3.450 TL'DEN BAŞLAYAN FİYATLARLA",
            "features": [
                "256-Bit SSL Güvenlik Sertifikası",
                "Google Core Web Vitals 99 Hız",
                ".com Alan Adı + Hosting Dahil",
                "WhatsApp Tek Tıkla Sipariş"
            ],
            "footer_cta": "WhatsApp: 0551 514 95 11",
            "caption": """⚡ İşletmenizin prestijini katlayacak yüksek hızlı web siteleri!

Sadece 3.450 TL'den başlayan fiyatlarla 3 iş gününde teslim.

📲 WhatsApp: 0551 514 95 11
Web: bastetyazilim.com

#webtasarım #bastetyazilim #kobi #esnaf #websitesi"""
        },
        # Günlük Hikayeler
        "story_morning": {
            "title": "GÜVENLİK TESTİ 🔒",
            "text": "Sitenizin adres çubuğunda kilit simgesi var mı yoksa 'Güvenli Değil' mi yazıyor?\n\nKullanıcıların %82'si güvensiz siteden hemen çıkar!",
            "cta": "Kontrol için linkinizi DM'den atın bakalım ➔"
        },
        "story_evening": {
            "title": "HAFTA SONU PLANLAMASI ☕",
            "text": "İşletmenizin yeni web sitesini 15 dakikalık bir WhatsApp görüşmesiyle planlayalım.",
            "cta": "WhatsApp'tan yazın: 0551 514 95 11 📲"
        }
    },

    # ================= 7. PAZAR =================
    "07_pazar_oto_servis_emlak": {
        "id": "07_pazar_oto_servis_emlak",
        "day": "Pazar",
        "day_num": 7,
        "type": "sales",
        "name": "Oto Servis & Emlak Portföy Sistemleri",
        "category": "OTO SERVİS & GAYRİMENKUL OTOMASYONU",
        "has_single_post": False,
        # Carousel Slayt 1 (Kapak)
        "cover_badge": "• SEKTÖREL AKILLI OTOMASYON",
        "cover_title_1": "İŞ EMİRLERİ, PARÇALAR",
        "cover_title_2": "VE EMLAK PORTFÖYLERİ",
        "cover_title_3": "DEFTERDE Mİ KARIŞIYOR?",
        "cover_highlight_badge": "• PLAKA BAZLI İŞ EMRİ & TALEP EŞLEŞTİRME",
        "cover_highlight_text": "Oto Tamir & Emlak Ofislerine Özel",
        "cover_subtext": "Sektörün kendine has dinamiklerine uygun hazır sistemler.",
        # Carousel Slayt 2 (Problem)
        "problem_headline": "Sektörde Yaşanan Güven ve Takip Sorunu",
        "problems": [
            {
                "title": "Parça & İşçilik Tartışmaları",
                "desc": "Müşteriye sözlü söylenen masraf teslimatta tartışmaya dönüşür ve tahsilat aksar."
            },
            {
                "title": "Unutulan Müşteri Portföy Talepleri",
                "desc": "3 ay önce arayan alıcının kriteri unutulunca portföydeki ev satılamaz."
            },
            {
                "title": "Araç & Mülk Geçmişinin Bilinememesi",
                "desc": "Araca veya mülke daha önce ne işlem yapıldığı hafızada tutulamaz."
            }
        ],
        # Carousel Slayt 3 (Çözüm)
        "solution_headline": "Bastet Sektörel Çözümleri",
        "solutions": [
            {
                "title": "Plakaya Özel Dijital İş Emri",
                "desc": "Araç servise girdiği an kilometre, hasar ve değişecek parçalar kayıt altına alınır."
            },
            {
                "title": "WhatsApp ile Müşteri Onaylı Maliyet",
                "desc": "İşçilik ve yedek parça dökümü müşteriye WhatsApp'tan onay linkiyle iletilir."
            },
            {
                "title": "Akıllı Emlak Talep Eşleştirme",
                "desc": "Yeni mülk girdiğinizde sistem o evi arayan müşterilerinizle otomatik eşleştirir."
            },
            {
                "title": "WhatsApp'a Hazır Şık Sunum Kartı",
                "desc": "Müşteriye karmaşık linkler yerine profesyonel mülk sunum kartı iletin."
            }
        ],
        # Carousel Slayt 4 (Fiyat & Neden Bastet)
        "advantage_headline": "Sektöre Özel Tek Seferlik Fiyat",
        "price_title": "SEKTÖREL LİSANS PAKETİ",
        "price_amount": "10.000 TL",
        "price_subtext": "Tek Seferlik Kurulum · Sınırsız Araç / Portföy Kaydı",
        "comparison_title": "Eski Programlar vs Bastet",
        "comparison_bad": "Eski Sistemler: Bilgisayara kilitli, mobil desteği olmayan, yıllık ağır aidat",
        "comparison_good": "Bastet Yazılım: 10.000 TL tek seferlik! Telefondan ve tabletten tam kontrol.",
        # Carousel Slayt 5 (CTA)
        "cta_title": "Yeni Haftaya Düzenli ve Dijital Başlayın!",
        "cta_subtext": "Oto servis veya emlak demo sistemini hemen denemek için WhatsApp'tan yazın.",
        # Açıklama Metni
        "caption": {
            "title": "🚗 Servise gelen aracın hesabı veya emlak ofisindeki alıcı talepleri ne kadar kontrol altında?",
            "body": """Oto tamirhaneleri ve emlak ofisleri için hız ve şeffaflık her şeydir!

Bastet Sektörel Yönetim Sistemleri ile:
🔧 Plakayı girin; aracın geçmiş bakım dökümü anında ekrana gelsin.
🔧 Değişen parçaları ve işçiliği WhatsApp'tan müşteriye resmi onay olarak iletin.
🔑 Satılık/kiralık evleri tek ekranda toplayın, arayan alıcılarla otomatik eşleştirin.
🔑 Danışman performanslarını ve kasa gelirlerini cep telefonunuzdan yönetin.

Aylık aidat yok! 10.000 TL tek seferlik ödeme ile işletmenize teslim.""",
            "cta": """📲 Canlı demoyu denemek için WhatsApp'tan yazın:
WhatsApp: 0551 514 95 11
Web: bastetyazilim.com""",
            "hashtags": "#otoservis #emlakofisi #servisyazılımı #portföyyönetimi #ototamir #emlakdanışmanı #bastetyazilim #kobi #esnaf"
        },
        # Günlük Hikayeler
        "story_morning": {
            "title": "PAZAR HATIRLATMASI 🏡",
            "text": "Yarın yeni bir hafta başlıyor! İşletmenizin dijital süreçlerini bu hafta düzene sokalım mı?",
            "cta": "Hizmetlerimizi incelemek için profildeki linke tıklayın ➔"
        },
        "story_evening": {
            "title": "HAZIR MISINIZ? 🚀",
            "text": "3 günde teslim web siteniz veya tek seferlik 10.000 TL'lik otomasyon sisteminiz için bu akşam yazın, yarın başlayalım!",
            "cta": "WhatsApp: 0551 514 95 11 📲"
        }
    }
}
