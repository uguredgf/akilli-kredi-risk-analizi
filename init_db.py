import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tahminler (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            gelir REAL,
            borc REAL,
            kredi_gecmisi INTEGER,
            yas INTEGER,
            sonuc TEXT
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Veritabanı (database.db) başarıyla oluşturuldu!")

if __name__ == '__main__':
    init_db()