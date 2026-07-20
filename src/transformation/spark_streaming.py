from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

import os


# --------------------------------------------------
# Spark Configuration
# --------------------------------------------------

os.environ["SPARK_LOCAL_IP"] = "127.0.0.1"
os.environ["SPARK_DRIVER_HOST"] = "127.0.0.1"


spark = SparkSession.builder \
    .appName("RetailSalesStreaming") \
    .master("local[*]") \
    .config(
        "spark.jars.packages",
        "org.apache.spark:spark-sql-kafka-0-10_2.13:4.0.0"
    ) \
    .config(
        "spark.driver.host",
        "127.0.0.1"
    ) \
    .config(
        "spark.driver.bindAddress",
        "127.0.0.1"
    ) \
    .config(
        "spark.sql.shuffle.partitions",
        "2"
    ) \
    .getOrCreate()


spark.sparkContext.setLogLevel("ERROR")


print("Spark Streaming Started...")


# --------------------------------------------------
# Read Data From Kafka
# --------------------------------------------------

kafka_df = spark.readStream \
    .format("kafka") \
    .option(
        "kafka.bootstrap.servers",
        "localhost:9092"
    ) \
    .option(
        "subscribe",
        "retail_transactions"
    ) \
    .option(
        "startingOffsets",
        "earliest"
    ) \
    .load()



# --------------------------------------------------
# Define Kafka JSON Schema
# --------------------------------------------------

schema = StructType([

    StructField(
        "transaction_id",
        StringType(),
        True
    ),

    StructField(
        "customer_id",
        StringType(),
        True
    ),

    StructField(
        "product_id",
        StringType(),
        True
    ),

    StructField(
        "product_category",
        StringType(),
        True
    ),

    StructField(
        "quantity",
        IntegerType(),
        True
    ),

    StructField(
        "price",
        IntegerType(),
        True
    ),

    StructField(
        "total_amount",
        IntegerType(),
        True
    ),

    StructField(
        "payment_method",
        StringType(),
        True
    ),

    StructField(
        "store_location",
        StringType(),
        True
    ),

    StructField(
        "timestamp",
        StringType(),
        True
    )

])



# --------------------------------------------------
# Convert Kafka Message To DataFrame
# --------------------------------------------------

sales_df = kafka_df.select(

    from_json(
        col("value").cast("string"),
        schema
    ).alias("data")

).select(
    "data.*"
)



# --------------------------------------------------
# Transform Sales Data
# --------------------------------------------------

processed_df = sales_df \
    .withColumn(
        "transaction_timestamp",
        to_timestamp("timestamp")
    ) \
    .withColumn(
        "revenue",
        col("quantity") * col("price")
    )



# --------------------------------------------------
# Output Locations
# --------------------------------------------------

output_path = (
    "/Users/anitharaj/"
    "retail-data-engineering-platform/"
    "data/silver/transactions"
)

checkpoint_path = (
    "/Users/anitharaj/"
    "retail-data-engineering-platform/"
    "data/checkpoints/transactions"
)



# Create folders

os.makedirs(
    output_path,
    exist_ok=True
)

os.makedirs(
    checkpoint_path,
    exist_ok=True
)



# --------------------------------------------------
# Write Streaming Output
# --------------------------------------------------

query = processed_df.writeStream \
    .format("parquet") \
    .option(
        "path",
        output_path
    ) \
    .option(
        "checkpointLocation",
        checkpoint_path
    ) \
    .outputMode(
        "append"
    ) \
    .trigger(
        once=True
    ) \
    .start()


query.awaitTermination()
