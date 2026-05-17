from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)

# 1. Model dosyasını yüklüyoruz (asama_iki.py çalıştırıldıktan sonra üretilen model)
MODEL_PATH = 'model.pkl'
if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)  # [cite: 368]
    print("-> Başarılı: model.pkl Flask sistemine entegre edildi.")
else:
    model = None
    print("-> UYARI: model.pkl bulunamadı! Lütfen önce asama_iki.py dosyasını çalıştırın.")


# 2. Hocanın rapor şablonunda belirttiği Tahmin Endpoint'i (POST /tahmin)
@app.route('/tahmin', methods=['POST'])  # [cite: 408]
def tahmin_et():
    if model is None:
        return jsonify({'error': 'Yapay zeka model dosyası sunucuda bulunamadı!'}), 500

    try:
        # Frontend katmanından (React veya HTML/JS) gelen ham JSON verisini yakalıyoruz
        veri = request.get_json()

        # Hocanın PDF'te belirttiği öznitelikleri (attributes) cımbızlıyoruz
        gelir = float(veri.get('gelir'))  # [cite: 129]
        borc = float(veri.get('borc'))  # [cite: 129]
        kredi_gecmisi = int(veri.get('kredi_gecmisi'))  # [cite: 129]
        yas = int(veri.get('yas'))  # [cite: 129]

        # Modelin eğitildiği sütun sırasına göre tahmini gerçekleştiriyoruz
        tahmin_kodu = model.predict([[gelir, borc, kredi_gecmisi, yas]])[0]  # [cite: 369]

        # Sayısal sonucu dökümandaki gibi metne döküyoruz (1: risksiz, 0: riskli)
        sonuc_metni = "risksiz" if tahmin_kodu == 1 else "riskli"  # [cite: 125, 360]

        # Frontend veya Database katmanına sadece saf veri (JSON) döndürüyoruz
        return jsonify({
            'kredi_durumu_kod': int(tahmin_kodu),  # Rapor ve DB için 1 veya 0 [cite: 360]
            'kredi_durumu': sonuc_metni,  # Ekranda basılması için "risksiz"/"riskli" [cite: 125]
            'mesaj': 'Tahmin başarıyla hesaplandı.'
        }), 200

    except Exception as e:
        return jsonify({
            'error': 'Eksik veya geçersiz veri formatı!',
            'details': str(e)
        }), 400


if __name__ == '__main__':
    app.run(port=5001, debug=True)