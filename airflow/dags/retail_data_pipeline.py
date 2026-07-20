from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime


PROJECT_PATH = "/Users/anitharaj/retail-data-engineering-platform"
PYTHON_PATH = f"{PROJECT_PATH}/venv/bin/python"


default_args = {
    "owner": "anitha",
    "start_date": datetime(2026, 7, 13),
}


with DAG(
    dag_id="retail_data_pipeline",
    default_args=default_args,
    schedule="@daily",
    catchup=False,
) as dag:

    generate_sales_data = BashOperator(
        task_id="generate_sales_data",
        bash_command=f"""
        cd {PROJECT_PATH} &&
        {PYTHON_PATH} src/data_generator.py
        """,
    )

    ingest_sales_data = BashOperator(
        task_id="ingest_sales_data",
        bash_command=f"""
        cd {PROJECT_PATH} &&
        {PYTHON_PATH} src/ingestion/kafka_producer.py
        """,
    )

    transform_sales_data = BashOperator(
        task_id="transform_sales_data",
        bash_command=f"""
        export SPARK_LOCAL_IP=127.0.0.1
        export SPARK_DRIVER_HOST=127.0.0.1

        cd {PROJECT_PATH} &&
        {PYTHON_PATH} src/transformation/spark_streaming.py
        """,
    )

    create_gold_layer = BashOperator(
        task_id="create_gold_layer",
        bash_command=f"""
        export SPARK_LOCAL_IP=127.0.0.1
        export SPARK_DRIVER_HOST=127.0.0.1

        cd {PROJECT_PATH} &&
        {PYTHON_PATH} src/transformation/gold_layer.py
        """,
    )

    (
        generate_sales_data
        >> ingest_sales_data
        >> transform_sales_data
        >> create_gold_layer
    )