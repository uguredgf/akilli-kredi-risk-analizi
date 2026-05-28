# Algoritma ve Programlama-II Proje Rapor Icerigi

Bu metin, `Algoritma_ve_Programlama2_Dersi_Proje_Sablonu (1).docx` icindeki basliklara gore doldurulmak uzere hazirlanmistir.

## Kapak Bilgileri
- Grup Numarasi: [Doldurulacak]
- Takim Lideri ve Uyeler: [Okul no - ad soyad]
- Projenin Adi: Akilli Kredi Risk Analizi

## 1. PROJE OZELLIKLERI

### 1.1 Projenin Amaci
Bu proje, kullanicidan alinan gelir, borc, kredi gecmisi ve yas bilgilerine gore kredi basvurusunun riskli mi risksiz mi oldugunu tahmin eden bir karar destek sistemi gelistirmeyi amaclar. Sistem; makine ogrenmesi modeli, Flask API, SQLite veritabani ve React tabanli arayuzden olusan uctan uca bir yapi ile calismaktadir.

### 1.2 Veri Seti ile Ilgili Bilgiler
- Veri seti dosyasi: `kredi_veri_seti.csv`
- Veri kaynagi: Sentetik veri uretimi (`sentetik.py`)
- Toplam satir sayisi: 1000
- Ozellikler (attributes):
  - `gelir`
  - `borc`
  - `kredi_gecmisi`
  - `yas`
- Etiket (sinif):
  - `etiket` (0 = riskli, 1 = risksiz)

Ornek 10 satir (rapora tablo olarak ekleyiniz):
1. 5000,2000,1,30,1
2. 2000,3000,0,25,0
3. 6000,1000,1,40,1
4. 1500,3500,0,22,0
5. 4500,1500,1,35,1
6. 1800,2800,0,28,0
7. 7000,1200,1,45,1
8. 2200,3000,0,26,0
9. 4800,2000,1,32,1
10. 1600,3200,0,24,0

### 1.3 Veritabani ile Ilgili Bilgiler
- Veritabani: SQLite
- Dosya: `database.db`
- Tablo: `tahminler`
- Alanlar:
  - `id` (INTEGER, PK, AUTOINCREMENT)
  - `gelir` (REAL)
  - `borc` (REAL)
  - `kredi_gecmisi` (INTEGER)
  - `yas` (INTEGER)
  - `sonuc` (TEXT)
- Islev: Her tahmin sonucunda kullanici girdileri ve sonuc veritabanina kaydedilmektedir.

### 1.4 Kullanilan Programlama Dili ve Framework
- Backend: Python + Flask
- Frontend: React (Vite)
- ML: scikit-learn (RandomForestClassifier)
- Veri isleme: pandas
- Model saklama: joblib

### 1.5 Frontend Araclari
- React fonksiyonel component yapisi
- CSS ile ozel arayuz tasarimi
- Form dogrulama (sayi sinirlari)
- Fetch API ile Flask endpoint entegrasyonu

### 1.6 Proje Mimarisi
Sistem 4 temel katmandan olusur:
1. Veri ve model katmani (`sentetik.py`, `asama_iki.py`, `model.pkl`)
2. API katmani (`app.py` veya `ml_api.py`)
3. Veritabani katmani (`database.db`)
4. Sunum katmani (`frontend`)

Calisma akisi:
1. Kullanici arayuzde formu doldurur.
2. Frontend JSON verisini `/tahmin` endpointine yollar.
3. Flask modeli kullanarak tahmin uretir.
4. Sonuc veritabanina kaydedilir.
5. Sonuc frontendde kullaniciya gosterilir.

### 1.7 Klasor Yapisi
- `app.py`: Flask endpoint ve DB kayit islemleri
- `ml_api.py`: Alternatif Flask API dosyasi
- `sentetik.py`: Sentetik veri uretimi
- `asama_iki.py`: Model egitimi, test ve kayit
- `init_db.py`: DB tablo olusturma
- `db_kontrol.py`: DB kayitlarini listeleme
- `frontend/`: React arayuz dosyalari

### 1.8 Makine Ogrenmesi Modeli Bilgileri
- Algoritma: RandomForestClassifier
- Giris degiskenleri: gelir, borc, kredi_gecmisi, yas
- Cikis: 0/1 siniflandirma
- Egitim-test bolunmesi: `%80 - %20`
- Basari olcutu: Accuracy + Confusion Matrix
- Ornek mevcut sonuc: Accuracy yaklasik `%96`

### 1.9 Flask Route ve Endpoint Yapis i
- `GET /` : API ayakta kontrol mesaji
- `POST /tahmin` : Tahmin endpointi
  - Input JSON: gelir, borc, kredi_gecmisi, yas
  - Output: risk sonucu (`riskli` veya `risksiz`)

## 2. PROJE YONETIMI

### 2.1 Takim Uyeleri
- Uye 1: [Ad Soyad - No]
- Uye 2: [Ad Soyad - No]
- Uye 3: [Ad Soyad - No]

### 2.2 Gorev Dagilimi
- Uye 1: Veri seti, sentetik veri uretimi, model egitimi
- Uye 2: Flask API, endpoint ve veritabani entegrasyonu
- Uye 3: Frontend arayuz, form dogrulama, API baglantisi

### 2.3 Is Paketleri
1. Problem tanimi ve proje plani
2. Veri seti olusturma ve temizleme
3. Model egitimi ve performans olcumu
4. Flask API gelistirme
5. Veritabani tasarimi ve kayit islemleri
6. Frontend gelistirme ve test
7. Entegrasyon testleri
8. Raporlama ve sunum hazirligi

## 3. SONUCLAR

### 3.1 Ekran Goruntuleri
Raporunuza asagidakileri ekleyiniz:
- Ana form ekrani
- Riskli sonuc ekrani
- Risksiz sonuc ekrani
- Veritabaninda tahmin kayitlari

### 3.2 Onemli Kod Parcalari
Raporunuza su kod bolumlerini ekleyiniz:
- Flask `POST /tahmin` route
- Random Forest model egitim kodu
- SQLite `INSERT INTO tahminler` sorgusu
- Frontend fetch istegi ve sonuc gosterimi

### 3.3 Model Performans Sonuclari
- Accuracy sonucu: [Calistirma sonucunu ekleyin]
- Confusion Matrix: [asama_iki.py cikti goruntusu/tablolu hali]
- Kisa yorum:
  - Model genel olarak yuksek dogruluk verir.
  - Sinir durumlarda (borc-gelir dengesi kritik olan satirlar) yanlis siniflandirma gorulebilir.

### 3.4 Genel Degerlendirme
Proje, ders kapsamindaki Flask, SQLite, frontend ve makine ogrenmesi entegrasyonu beklentilerini karsilamaktadir. Sistem gercek hayatta kredi on degerlendirme adiminda yardimci olacak bir prototip olarak calismaktadir. Gelecekte veri setinin gercek verilerle zenginlestirilmesi, model aciklanabilirligi ve guven skoru gosterimi ile sistem daha guclu hale getirilebilir.
