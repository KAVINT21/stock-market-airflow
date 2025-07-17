from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def print_hello():
    print("Hello from Astro Cloud!")

with DAG(dag_id="stock_dag",
         start_date=datetime(2024, 1, 1),
         schedule_interval="@daily",
         catchup=False) as dag:
    
    task = PythonOperator(
        task_id="say_hello",
        python_callable=print_hello
    )
