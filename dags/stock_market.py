from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def dummy_task():
    print("This is a placeholder")

with DAG(
    dag_id="stock_market_pipeline",
    schedule_interval="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id="dummy",
        python_callable=dummy_task
    )
