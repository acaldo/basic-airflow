from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(dag_id="bash_operator", description='first dag with bash operator',start_date=datetime(2022,7,1),schedule_interval="@once") as dag:
    t1 = BashOperator(task_id="dummy", bash_command="echo 'hello world'")
    t1