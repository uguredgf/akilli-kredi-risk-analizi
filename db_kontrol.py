import sqlite3
import pandas as pd

conn = sqlite3.connect('database.db')
print(pd.read_sql_query("SELECT * FROM tahminler", conn))
conn.close()