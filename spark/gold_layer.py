from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, count, avg

spark = (
    SparkSession.builder
    .appName("RetailGoldLayer")
    .master("local[*]")
    .getOrCreate()
)

# Read Silver Layer
df = spark.read.parquet("data/processed/silver_transactions")

print("Silver Records:", df.count())

# ----------------------------
# Sales Summary
# ----------------------------
sales_summary = (
    df.groupBy("store_location", "product_category")
      .agg(
          sum("total_amount").alias("total_sales"),
          count("*").alias("total_orders"),
          avg("total_amount").alias("average_order_value")
      )
)

sales_summary.show()

sales_summary.write.mode("overwrite").parquet(
    "data/gold/sales_summary"
)

# ----------------------------
# Product Performance
# ----------------------------
product_summary = (
    df.groupBy("product_id", "product_category")
      .agg(
          sum("quantity").alias("quantity_sold"),
          sum("total_amount").alias("revenue")
      )
)

product_summary.show()

product_summary.write.mode("overwrite").parquet(
    "data/gold/product_summary"
)

# ----------------------------
# Customer Summary
# ----------------------------
customer_summary = (
    df.groupBy("customer_id")
      .agg(
          count("*").alias("orders"),
          sum("total_amount").alias("total_spent")
      )
)

customer_summary.show()

customer_summary.write.mode("overwrite").parquet(
    "data/gold/customer_summary"
)

spark.stop()