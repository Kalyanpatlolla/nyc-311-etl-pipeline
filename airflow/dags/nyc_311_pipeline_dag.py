from datetime import datetime, timedelta
import sys

sys.path.append("/opt/airflow")
from airflow import DAG
from airflow.operators.python import PythonOperator

from src.extract import extract_data
from src.transform import transform_data
from src.load import load_to_warehouse
from src.validate import validate_data
from src.build_marts import build_marts

default_args = {
    "retries": 2,
    "retry_delay": timedelta(minutes=1),
}


with DAG(
    dag_id="nyc_311_etl_pipeline",
    default_args=default_args,
    start_date=datetime(2025, 5, 1),
    schedule="@daily",
    catchup=False,
    tags=["nyc311", "etl"],
) as dag:

    extract_task = PythonOperator(
        task_id="extract_data",
        python_callable=extract_data
    )

    transform_task = PythonOperator(
        task_id="transform_data",
        python_callable=transform_data
    )

    validate_task = PythonOperator(
    task_id="validate_data",
    python_callable=validate_data
    )

    load_task = PythonOperator(
        task_id="load_to_warehouse",
        python_callable=load_to_warehouse
    )

    build_marts_task = PythonOperator(
    task_id="build_marts",
    python_callable=build_marts
    )

extract_task >> transform_task >> validate_task >> load_task >> build_marts_task