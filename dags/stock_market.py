from airflow import dag,task
from datetime import datetime
import requests

def fetch_stock():
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": "AAPL",
        "apikey": "1CCQTRMYE2PGX51N"  # 👈 use your key
    }
    response = requests.get(url, params=params)
    print(response.json())  # For logs

@dag(
    start_date=datetime(2024, 1, 1),
    schedule='@daily',
    catchup=False,
    tags=["stock_market"],
)

def stock_market():
    @task
    def fetch_stock_data():
        fetch_stock()
    
stock_market()