from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

def print_hello():
    print('hello world')

with DAG(dag_id="5.1-orquestation",
         description='probando la orquestacion',
         start_date=datetime(2022,7,1),
         end_date=datetime(2022,8,1),
         schedule_interval="@daily",
         default_args={"depends_on_past": True},
         max_activate_runs=1) as dag:
    t1 = BashOperator(task_id="tarea1", bash_command="sleep 2 && echo 'tarea1'")
    t2 = BashOperator(task_id="tarea2", bash_command="sleep 2 && echo 'tarea2'")
    t3 = BashOperator(task_id="tarea3", bash_command="sleep 2 && echo 'tarea3'")
    t4 = BashOperator(task_id="tarea4", bash_command="sleep 2 && echo 'tarea4'")

    
    t1 >> t2 >> [t3 , t4]

