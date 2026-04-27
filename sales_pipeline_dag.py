from airflow import DAG 
from airflow.operators.python import PythonOperator
from datetime import datetime 
import os

def run_python():
    os.system("python /opt/airflow/dags/python_script.py")
    
def run_sql():
    print("Runnind SQL step")
    
with DAG(
    dag_id='sales_pipeline',
    start_date=datetime(2026,4,27),
    schedule='@daily',
    catchup=False) as dag:
    
    task1=PythonOperator(
    task_id='run_python_script',
    python_callable=run_python
    )
    
    task2=PythonOperator(
    task_id='run_sql_step',
    python_callable=run_sql
    )
    
    task1>>task2