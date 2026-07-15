from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, count

spark = (
    SparkSession.builder
    .appName("Retail Gold Layer")
    .getOrCreate()
)

# Read Silver Layer
silver_df = spark.read.parquet(
    "data/silver/transactions/*.parquet"
)

# Gold Table: Sales by Product

sales_by_product = (
    silver_df
    .groupBy("product_id")
    .agg(
        sum("revenue").alias("total_revenue"),
        count("*").alias("total_transactions")
    )
)

# Save Gold Layer

sales_by_product.write \
    .mode("overwrite") \
    .parquet("data/gold/sales_by_product")

print("Gold Layer Created Successfully!")

spark.stop()