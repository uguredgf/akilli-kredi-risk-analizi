import pandas as pd
from sklearn.ensemble import RandomForestClassifier # Kullanacağımız algoritma
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib # Modeli kaydetmek için

# 1. Az önce ürettiğimiz veriyi okuyoruz
veri = pd.read_csv("kredi_veri_seti.csv")

# 2. X (Girdiler) ve y (Çıktı/Etiket) olarak veriyi ikiye ayırıyoruz
X = veri[["gelir", "borc", "kredi_gecmisi", "yas"]] # Modelin bakacağı özellikler
y = veri["etiket"] # Modelin tahmin etmeye çalışacağı hedef sonuç

# 3. Veriyi %80 Eğitim (öğrenmesi için), %20 Test (kendini sınaması için) olarak bölüyoruz
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Modeli tanımlıyoruz ve eğitiyoruz
model = RandomForestClassifier()
model.fit(X_train, y_train) # Verilerden öğrenme aşaması

# 5. Modelin test verileri üzerinde ne kadar başarılı olduğunu ölçüyoruz
tahminler = model.predict(X_test)
dogruluk = accuracy_score(y_test, tahminler)
karmasiklik_matrisi = confusion_matrix(y_test, tahminler)

print(f"Modelin Doğruluk Oranı (Accuracy): %{dogruluk * 100}")
print("Karmaşıklık Matrisi (Confusion Matrix):")
print(karmasiklik_matrisi)
print("2. AŞAMA TAMAM: Model eğitildi ve performansı ölçüldü.")

# 6. Eğitilen modeli .pkl uzantılı bir dosya olarak kaydediyoruz
joblib.dump(model, "model.pkl")
print("3. AŞAMA TAMAM: model.pkl dosyası kaydedildi.")