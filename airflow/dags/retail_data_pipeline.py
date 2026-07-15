from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime


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
        bash_command="""
        cd /Users/anitharaj/retail-data-engineering-platform &&
        python src/data_generator.py
        """
    )


    ingest_sales_data = BashOperator(
        task_id="ingest_sales_data",
        bash_command="""
        cd /Users/anitharaj/retail-data-engineering-platform &&
        python src/ingestion/kafka_producer.py
        """
    )


    transform_sales_data = BashOperator(
        task_id="transform_sales_data",
        bash_command="""
        cd /Users/anitharaj/retail-data-engineering-platform &&
        python src/transformation/spark_streaming.py
        """
    )


    generate_sales_data >> ingest_sales_data >> transform_sales_data