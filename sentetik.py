import pandas as pd
import random

# Bos listemizi olusturalim
veriler = []

print(" veri uretimi baslatiliyor...")

# 1000 tane ornek veri uretiyoruz
for i in range(5000):
    # Yas araligini 10 ile 100 arasi yaptik
    yas = random.randint(10, 100)


    etiket = 0

    # Gelir araligi
    gelir = random.randint(20000, 75000)

    # Borc araligi
    borc = random.randint(0, 50000)

    # Kredi gecmisi (0: Kotu, 1: Iyi)
    kredi_gecmisi = random.choice([0, 1])

    # 🚨 CRITICAL RULE: 18 yasindan kucukse VEYA 80 yasindan buyukse kredi otomatik REDDEDILIR
    if yas < 18 or yas > 80:
        etiket = 0

    else:
        # Eger yas 18 ile 80 arasindaysa, normal kredi kurallari devreye girer:
        if kredi_gecmisi == 1:
            # Kredi gecmisi iyiyse (1):
            # Borc, gelirin %45'inden kucuk veya esitse RISKSIZ (1), buyukse RISKLI (0)
            if borc <= (gelir * 0.45):
                etiket = 1
            else:
                etiket = 0

        elif kredi_gecmisi == 0:
            # Kredi gecmisi kotuyse (0): Gelir borcun 4 kati veya fazlasiysa kurtarir (1)
            if gelir >= (borc * 4):
                etiket = 1
            else:
                etiket = 0

    # Uretilen bu satiri listeye ekle
    veriler.append([yas, gelir, borc, kredi_gecmisi, etiket])

# Listeyi pandas DataFrame yapisina donusturuyoruz
df = pd.DataFrame(veriler, columns=['yas', 'gelir', 'borc', 'kredi_gecmisi', 'etiket'])

# Veri setini CSV dosyasi olarak kaydediyoruz
df.to_csv('kredi_veri_seti.csv', index=False)

print("--------------------------------------------------")
print("BASARILI: Yas araligi 10-100 yapildi, 80 yas ustu engeli eklendi!")
print("kredi_veri_seti.csv dosyasi basariyla kaydedildi.")
print("--------------------------------------------------")