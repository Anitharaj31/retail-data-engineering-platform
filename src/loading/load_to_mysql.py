import pandas as pd
import glob
from sqlalchemy import create_engine

# -----------------------------
# Read all parquet files
# -----------------------------
files = glob.glob(
    "data/processed/transactions/*.parquet"
)

df = pd.concat(
    [pd.read_parquet(f) for f in files],
    ignore_index=True
)

print("Records Loaded :", len(df))

# -----------------------------
# MySQL Connection
# -----------------------------
engine = create_engine(
    "mysql+pymysql://root:@localhost/retail_db"
)

# -----------------------------
# Load into MySQL
# -----------------------------
df.to_sql(
    "sales_transactions",
    con=engine,
    if_exists="replace",
    index=False
)

print("Data Loaded Successfully!")