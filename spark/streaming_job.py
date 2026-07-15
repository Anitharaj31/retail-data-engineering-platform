from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    IntegerType,
    DoubleType
)


# Create Spark Session
spark = (
    SparkSession.builder
    .appName("RetailStreamingPipeline")
    .master("local[*]")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("WARN")


# Schema for incoming Kafka JSON messages
schema = StructType([

    StructField("transaction_id", StringType(), True),
    StructField("customer_id", StringType(), True),
    StructField("product_id", StringType(), True),
    StructField("product_category", StringType(), True),
    StructField("quantity", IntegerType(), True),
    StructField("price", DoubleType(), True),
    StructField("total_amount", DoubleType(), True),
    StructField("payment_method", StringType(), True),
    StructField("store_location", StringType(), True),
    StructField("timestamp", StringType(), True)

])


# Read streaming data from Kafka
kafka_df = (
    spark.readStream
    .format("kafka")
    .option(
        "kafka.bootstrap.servers",
        "localhost:9092"
    )
    .option(
        "subscribe",
        "retail_transactions"
    )
    .option(
        "startingOffsets",
        "latest"
    )
    .load()
)


# Convert Kafka message value from binary to JSON
transactions_df = (
    kafka_df
    .selectExpr(
        "CAST(value AS STRING) AS json"
    )
    .select(
        from_json(
            col("json"),
            schema
        ).alias("data")
    )
    .select(
        "data.*"
    )
)


# Data quality filter
clean_transactions = (
    transactions_df
    .filter(
        col("transaction_id").isNotNull()
    )
    .filter(
        col("total_amount") > 0
    )
)


# Display streaming output
query = (
    clean_transactions
    .writeStream
    .format("parquet")
    .outputMode("append")
    .option(
        "path",
        "data/processed/silver_transactions"
    )
    .option(
        "checkpointLocation",
        "data/checkpoints/silver_transactions"
    )
    .start()
)

query.awaitTermination()