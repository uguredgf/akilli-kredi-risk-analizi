from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/tahmin', methods=['POST'])
def tahmin():
    if request.method == 'POST':
        gelir = float(request.form['gelir'])
        borc = float(request.form['borc'])
        kredi_gecmisi = int(request.form['kredi_gecmisi'])
        yas = int(request.form['yas'])
        
        if gelir > (borc * 1.5) and kredi_gecmisi == 1:
            sonuc = "risksiz"
        else:
            sonuc = "riskli"

        conn = get_db_connection()
        conn.execute('''
            INSERT INTO tahminler (gelir, borc, kredi_gecmisi, yas, sonuc) 
            VALUES (?, ?, ?, ?, ?)
        ''', (gelir, borc, kredi_gecmisi, yas, sonuc))
        conn.commit()
        conn.close()

        return render_template('index.html', sonuc=sonuc)

if __name__ == '__main__':
    app.run(debug=True)