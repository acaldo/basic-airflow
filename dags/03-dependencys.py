from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

def print_hello():
    print("HELLO 1")

with DAG(dag_id="dependencias_test",
         description="Creando dependendecias parcero",
         schedule_interval="@once",
         start_date =datetime(2022,12,6)) as dag:


    t1 = PythonOperator(task_id="tarea1",
                        python_callable=print_hello)

    t2 = BashOperator(task_id="tarea2",
                      bash_command="echo 'Hello 2'")       

    t3 = BashOperator(task_id="tarea3",
                      bash_command="echo 'Hello 3'")  

    t4 = BashOperator(task_id="tarea4",
                      bash_command="echo 'Hello 4'")

    t1 >> [t2,t3] >> t4 
"""     t1.set_downstream(t2) 
    t2.set_downstream([t3,t4])                                                                                 
 """
    #Other way