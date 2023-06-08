from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime
from groups.groups_downloads import download_tasks
from groups.groups_transforms import transform_tasks 

 
with DAG('group_dag', start_date=datetime(2023, 5, 10), 
    schedule_interval='@daily', catchup=False) as dag:
    
    args= {
            'start_date': dag.start_date,
            'schedule_interval': dag.schedule_interval,
            'catchup': dag.catchup
            }

    
    downloads = download_tasks()
 
    check_files = BashOperator(
        task_id='check_files',
        bash_command='sleep 10'
    )
    
    transforms = transform_tasks()
    
 
    downloads >> check_files >> transforms