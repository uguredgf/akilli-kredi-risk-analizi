# Akilli Kredi Risk Analizi - Sunum Akisi

## Slayt 1 - Proje Tanitimi
- Proje adi: Akilli Kredi Risk Analizi Sistemi
- Ders: Algoritma ve Programlama II
- Temel hedef: Kullanici girdilerine gore kredi risk siniflandirmasi yapmak
- Kullanilan teknoloji seti: Python, Flask, SQLite, React, scikit-learn

## Slayt 2 - Problemin Tanimi ve Amac
- Bankacilikta kredi karari hizli ve tutarli sekilde alinmalidir.
- Sistem, gelir, borc, kredi gecmisi ve yas verilerinden risk tahmini uretir.
- Cikti siniflari: riskli (0) ve risksiz (1).
- Sonuc hem ekranda gosterilir hem veritabanina kaydedilir.

## Slayt 3 - Proje Mimarisi
- Katmanlar:
  - Frontend (React)
  - Backend (Flask API)
  - Veritabani (SQLite)
  - ML modeli (RandomForest - model.pkl)
- Akis:
  1. Kullanici formu doldurur.
  2. Frontend `/tahmin` endpointine POST atar.
  3. Flask modeli yukler, tahmin uretir, DB kaydi olusturur.
  4. Sonuc frontend tarafinda kullaniciya gosterilir.

## Slayt 4 - Veri Seti ve Ozellikler
- CSV dosyasi: `kredi_veri_seti.csv`
- Ozellikler: `gelir`, `borc`, `kredi_gecmisi`, `yas`
- Etiket: `etiket` (0: riskli, 1: risksiz)
- Sentetik veri uretimi: `sentetik.py`
- Veri seti buyutulerek modelin genelleme kabiliyeti artirilmistir.

## Slayt 5 - ML Modeli ve Performans
- Model: `RandomForestClassifier`
- Egitim dosyasi: `asama_iki.py`
- Model cikti dosyasi: `model.pkl`
- Test sonucu (mevcut calistirmada): Accuracy yaklasik `%96`
- Confusion matrix rapora eklenmelidir.

## Slayt 6 - Flask ve Endpoint Yapisi
- Ana endpoint: `POST /tahmin`
- Beklenen JSON:
  - `gelir` (float)
  - `borc` (float)
  - `kredi_gecmisi` (0/1)
  - `yas` (int)
- Donen sonuc:
  - `sonuc` veya `kredi_durumu` alanlari
- Veritabani tablosu: `tahminler (gelir, borc, kredi_gecmisi, yas, sonuc)`

## Slayt 7 - Frontend Arayuzu
- React formu ile kullanicidan tum girdiler alinmaktadir.
- Alan dogrulama eklendi:
  - Gelir > 0
  - Borc >= 0
  - Yas pozitif (UI tarafinda min yas kontrolu var)
- API uyumlulugu artirildi:
  - `localhost:5000` ve `localhost:5001` endpointleri desteklenir
  - `sonuc` ve `kredi_durumu` alanlari normalize edilir
- Sonuc karti risk durumunu anlasilir sekilde gosterir.

## Slayt 8 - Veritabani Islemleri
- Veritabani kurulumu: `init_db.py`
- Tahmin kayitlari otomatik olarak `tahminler` tablosuna eklenir.
- Kontrol scripti: `db_kontrol.py`
- Sunumda son 5 kayit gosterimi etkili olur.

## Slayt 9 - Gorev Dagilimi (Ornek)
- Uye 1: Veri uretimi ve model egitimi
- Uye 2: Flask API, endpointler, veritabani islemleri
- Uye 3: Frontend arayuz, API entegrasyonu, kullanici deneyimi
- Her uye sorumlu oldugu modulun kodunu sunumda aciklayabilmelidir.

## Slayt 10 - Demo Senaryosu
- Adim 1: Flask API baslatilir.
- Adim 2: React frontend baslatilir.
- Adim 3: Farkli profillerle 2-3 tahmin yapilir.
- Adim 4: Sonuclarin DB kaydi gosterilir.
- Adim 5: Model dogruluk ve confusion matrix ciktilari paylasilir.

## Slayt 11 - Degerlendirme ve Iyilestirme Fikirleri
- Guclu yonler:
  - Uctan uca calisan mimari
  - ML + API + DB + Frontend entegrasyonu
  - Hizli prototipleme
- Iyilestirme:
  - Tek backend dosyasinda standart API cevabi
  - Model versiyonlama ve hata loglama
  - Dashboard: gecmis tahminler, risk dagilimi grafigi

## Slayt 12 - Sonuc
- Proje, dersin bekledigi tum temel bilesenleri karsilar.
- Kredi risk siniflandirmasi amacina uygun calisan bir prototip elde edilmistir.
- Gelecek calismalarda veri kalitesi ve aciklanabilirlik (feature importance) gelistirilebilir.

---

## Juri Soru-Cevap Hazirlik Notlari
- Neden Random Forest sectiniz?
  - Dengesiz veri ve dogrusal olmayan iliskilerde stabil performans verdigi icin.
- Neden SQLite kullandiniz?
  - Ders kapsaminda hafif, kurulum gerektirmeyen bir cozum oldugu icin.
- Frontend-backend uyumu nasil saglandi?
  - Endpoint ve donus alanlarindaki farkliliklara karsi normalize eden istemci mantigi yazildi.
- Model yanlis tahminde ne olur?
  - Sistem su an sadece skor dondurur; ileri adimda guven skoru ve aciklama katmani eklenebilir.
