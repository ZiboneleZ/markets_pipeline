# 📈 Market Data Pipeline & Analytics (Automated ETL)

An automated ETL (Extract, Transform, Load) pipeline that tracks global currency rates against the USD, stores historical data in a local SQLite database, and generates automated performance reports with technical indicators.

## 🚀 Project Overview

This project was built to solve the challenge of manual data collection and analysis. It automates the entire lifecycle of data:
1. **Extraction:** Fetches real-time exchange rates for EUR, JPY, GBP, and ZAR via the ExchangeRate-API.
2. **Loading:** Cleans and inserts data into a structured SQLite database.
3. **Transformation:** Calculates a **4-Hour Moving Average** using Pandas to identify market trends.
4. **Visualization:** Generates an automated Excel report and a visual Matplotlib dashboard.

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Automation:** Linux Cron (WSL)
* **Data Handling:** Pandas, SQLite3
* **Visualization:** Matplotlib, Openpyxl
* **Environment:** Python-dotenv, Requests

## 📂 Project Structure
```text
market_pipeline/
├── data/
│   └── market_data.db        # SQLite Database
├── outputs/
│   ├── Market_Report.xlsx    # Automated Excel export
│   └── Dashboard.png         # Trend visualization
├── collector.py              # Ingestion script
├── analyzer.py               # Processing & Viz script
├── .env                      # API Keys & Paths (Hidden)
└── requirements.txt          # Project dependencies

⚙️ Engineering Challenges & Solutions
During development, several environment-specific hurdles were overcome, demonstrating proficiency in Linux systems and debugging:

Cron Automation in WSL: Solved issues where scheduled tasks failed due to pathing. Implemented absolute paths for the virtual environment and scripts to ensure reliable 24/7 automation.

DNS Resolution: Fixed a Temporary failure in name resolution error within WSL by reconfiguring the Linux subsystem's DNS settings (8.8.8.8), ensuring the collector could reach external APIs consistently.

Logical Debugging: Identified and resolved a "silent fail" in the analysis layer where a string literal was used instead of a variable during Pandas filtering, ensuring the data integrity of the final reports.

📊 Visualizations
The pipeline generates a 4-pane dashboard showing price movements and moving averages for the tracked currencies.

# New challenges I am still working on, is the fact that my API only uses daily prices. Therefore pulling the prices every hour is not only redundant but not usefull as the prices are the same for the 24 hours of the day. This results in a straight line when displaying the prices on a chart. Also, this makes the 4-hour Moving Average to be not usefull as it also displays a straight line. 

# I will proceed to find a solution for this problem. (22/01/2026)
