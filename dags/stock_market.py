from airflow.decorators import dag, task
from datetime import datetime

@dag(start_date=datetime(2024, 1, 1), schedule_interval="@daily", catchup=False)
def stock_pipeline():
    @task
    def start():
        print("Pipeline started")

    start()

stock_pipeline()
