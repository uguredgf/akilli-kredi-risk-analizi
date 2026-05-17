import random
import pandas as pd

# 1. Verileri tutacağımız liste
veriler = []

# 2. 1000 satırlık rastgele veri üretiyoruz
for _ in range(1000):
    # Yaş aralığını 10'dan başlatıyoruz ki model küçük yaşları da görsün
    yas = random.randint(10, 75)
    gelir = random.randint(2000, 15000)
    borc = random.randint(0, 10000)
    kredi_gecmisi = random.choice([0, 1])  # 0: kötü, 1: iyi

    # KURAL GÜNCELLEME:
    # 18 yaşından küçükse borç/gelir ne olursa olsun RİSKLİ (0) yapıyoruz
    if yas < 18:
        etiket = 0
    # Borç gelirin %60'ından fazlaysa veya kredi geçmişi kötüyse RİSKLİ (0)
    elif borc > (gelir * 0.6) or kredi_gecmisi == 0:
        etiket = 0
    else:
        etiket = 1

    veriler.append([gelir, borc, kredi_gecmisi, yas, etiket])

# 3. CSV dosyası olarak kaydediyoruz
df = pd.DataFrame(veriler, columns=["gelir", "borc", "kredi_gecmisi", "yas", "etiket"])
df.to_csv("kredi_veri_seti.csv", index=False)
print("1. AŞAMA TAMAM: 18 yaş sınırı kuralıyla veri seti oluşturuldu.")