import pandas as pd
import os


os.makedirs("data/dashboard", exist_ok=True)


tables = [
    "sales_by_product",
    "sales_by_category",
    "sales_by_location",
    "daily_sales"
]


for table in tables:

    df = pd.read_parquet(
        f"data/gold/{table}"
    )

    df.to_csv(
        f"data/dashboard/{table}.csv",
        index=False
    )

    print(f"Exported {table}")


print("Dashboard data export completed!")