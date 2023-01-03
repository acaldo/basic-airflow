from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def print_hello():
    print('hello world')

with DAG(dag_id="python_operator", description='first dag with python operator',start_date=datetime(2022,7,1),schedule_interval="@once") as dag:
    t1 = PythonOperator(task_id="dummy", python_callable=print_hello)
    t1



