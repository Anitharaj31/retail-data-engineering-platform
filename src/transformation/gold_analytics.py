from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, count, to_date


# Create Spark Session
spark = (
    SparkSession.builder
    .appName("Retail Gold Analytics")
    .getOrCreate()
)


# Read Silver Layer
silver_df = spark.read.parquet(
    "data/silver/transactions/*.parquet"
)


# --------------------------------------------------
# Gold Table 1: Sales by Category
# --------------------------------------------------

sales_by_category = (
    silver_df
    .groupBy("product_category")
    .agg(
        sum("revenue").alias("total_revenue"),
        count("*").alias("total_transactions")
    )
)

sales_by_category.write \
    .mode("overwrite") \
    .parquet("data/gold/sales_by_category")


# --------------------------------------------------
# Gold Table 2: Sales by Location
# --------------------------------------------------

sales_by_location = (
    silver_df
    .groupBy("store_location")
    .agg(
        sum("revenue").alias("total_revenue"),
        count("*").alias("total_transactions")
    )
)

sales_by_location.write \
    .mode("overwrite") \
    .parquet("data/gold/sales_by_location")


# --------------------------------------------------
# Gold Table 3: Daily Sales Trend
# --------------------------------------------------

daily_sales = (
    silver_df
    .withColumn(
        "date",
        to_date("transaction_timestamp")
    )
    .groupBy("date")
    .agg(
        sum("revenue").alias("total_revenue"),
        count("*").alias("total_transactions")
    )
)

daily_sales.write \
    .mode("overwrite") \
    .parquet("data/gold/daily_sales")


print("Gold Analytics Tables Created Successfully!")

spark.stop()