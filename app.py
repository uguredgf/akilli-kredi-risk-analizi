from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import joblib

app = Flask(__name__)
CORS(app) 

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET'])
def index():
    return jsonify({"mesaj": "Proje API calisiyor!"})

@app.route('/tahmin', methods=['POST'])
def tahmin():
    if request.method == 'POST':
        veri = request.json
        
        gelir = float(veri['gelir'])
        borc = float(veri['borc'])
        kredi_gecmisi = int(veri['kredi_gecmisi'])
        yas = int(veri['yas'])
        
        # --- MODEL YÜKLEME VE TAHMİN KISMI ---
        model = joblib.load("model.pkl")
        tahmin_dizisi = model.predict([[gelir, borc, kredi_gecmisi, yas]])
        tahmin_degeri = tahmin_dizisi[0] 
        
        # Gelen 0 veya 1 değerini metne çeviriyoruz
        if str(tahmin_degeri) == "1" or str(tahmin_degeri) == "1.0":
            sonuc = "risksiz"
        else:
            sonuc = "riskli"
      
        # --- VERİTABANI KAYIT KISMI ---
        conn = get_db_connection()
        conn.execute('''
            INSERT INTO tahminler (gelir, borc, kredi_gecmisi, yas, sonuc) 
            VALUES (?, ?, ?, ?, ?)
        ''', (gelir, borc, kredi_gecmisi, yas, sonuc))
        conn.commit()
        conn.close()

        # Metne çevrilmiş sonucu React'e gönderiyoruz
        return jsonify({'sonuc': sonuc})

if __name__ == '__main__':
    app.run(debug=True)