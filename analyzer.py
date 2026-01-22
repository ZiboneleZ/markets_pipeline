import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv('DB_PATH')
OUTPUT_DIR = os.getenv("OUTPUT_DIR")

def run_analysis():
    if not os.path.exists(DB_PATH):
        print("No database found!")
        return

    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM market_history", conn)
    conn.close()

    if df.empty: return

    symbols = df['symbol'].unique()
    plt.figure(figsize=(12, 8))

    all_data = []
    for i, symbol in enumerate(symbols, 1):        
        sym_df = df[df['symbol'] == symbol].copy()
        #Calculating the 4HR Moving Average
        sym_df['4h_MA'] = sym_df['price'].rolling(window=4).mean()
        all_data.append(sym_df)
        
        #print(sym_df)
            
        #This is the subplot logic
        plt.subplot(2, 2, i)
        plt.plot(sym_df['timestamp'], sym_df['price'], label='Price', color='blue')
        plt.plot(sym_df['timestamp'], sym_df['4h_MA'], label='4h MA', color='orange', linestyle='--')
        plt.title(f"{symbol} Trend")
        plt.xticks(rotation=45)
        plt.legend()

        #print(all_data)

    #Saving outputs to my folders
    pd.concat(all_data).to_excel(f"{OUTPUT_DIR}Market_Report.xlsx", index=False)
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}Dashboard.png")
    #print(all_data)
    print(f"Analysis complete. Files saved in {OUTPUT_DIR}")

if __name__ == '__main__':
    run_analysis()
