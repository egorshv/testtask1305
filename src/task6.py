from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.providers.http.hooks.http import HttpHook
import pandas as pd
from pydantic import BaseModel, ValidationError, conint
from typing import List
from datetime import datetime as dt


class BankAPIDocument(BaseModel):
    key1: conint(ge=0)  # Assuming key1 is a non-negative integer
    key2: dt  # Assuming key2 is a datetime
    key3: str


def validate_json(json_data):
    try:
        data = BankAPIDocument(**json_data)
        print("JSON is valid.")
        return True
    except ValidationError as e:
        print(f"Validation Error: {e}")
        return False


def process_json(json_data):
    df = pd.DataFrame(json_data['Rows'], columns=json_data['Columns'])
    df.rename(columns={"key1": "document_id", "key2": "document_dt", "key3": "document_name"}, inplace=True)
    df['load_dt'] = datetime.now()
    print("Processed DataFrame:")
    print(df)
    return df


def get_timestamp():
    return int(datetime.timestamp(datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)))


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 14),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG(
    'bank_api_processing',
    default_args=default_args,
    description='DAG for processing data from bank API',
    schedule_interval='@daily',
)

validate_json_task = PythonOperator(
    task_id='validate_json',
    python_callable=validate_json,
    provide_context=True,
    dag=dag,
)

process_json_task = PythonOperator(
    task_id='process_json',
    python_callable=process_json,
    provide_context=True,
    dag=dag,
)

http_hook = HttpHook(method='GET', http_conn_id='gazprombank_api')

get_data_task = SimpleHttpOperator(
    task_id='get_data',
    http_conn_id='gazprombank_api',
    method='GET',
    endpoint=f'/very/important/docs?documents_date={get_timestamp()}',
    headers={},
    xcom_push=True,
    dag=dag,
)

get_data_task >> validate_json_task >> process_json_task
