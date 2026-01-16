import os
import sqlite3
import requests
from datetime import datetime
from dotenv import load_dotenv

# Loading config from .env
load_dotenv()
API_KEY = os.get_env('EXCHANGE_API_KEY')
DB_PATH = os.get_env('DB_PATH')

def get_rates():
    #Fetching base USD rates
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"
    try:
        response = requests.get(url)
        data = response.json()
        if data['result'] == 'success':
            r = data['conversion_rates']
            # Picking Only Four - EUR, JPY, GBP, ZAR
            return {'EUR': r['EUR'], 'JPY': r['JPY'], 'GBP': r['GBP'], 'ZAR': ['ZAR']}

    except Exception as e:
        print(f"API Error: {e}")
    return None

def save_to_db(payload):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS market_history
                    (timestamp TEXT, symbol TEXT, price REAL)
                ''')
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for symbol, price in payload.items():
            cursor.execute('INSERT INTO market_history VALUES (?, ?, ?)', now, symbol, price))
        conn.close()

if __name__ == '__main__':
    data = get_rates
    if data:
        save_to_db(data)

