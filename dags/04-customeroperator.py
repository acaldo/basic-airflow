from airflow import DAG
from datetime import datetime
from hellooperator import HelloOperator

with DAG(dag_id="customer_operator",
         description='first dag with customer operator',
         start_date=datetime(2022,7,1),
         schedule_interval="@once",
         catchup = False) as dag:
    t1 = HelloOperator(task_id="hello", name="Airflow")
    t1