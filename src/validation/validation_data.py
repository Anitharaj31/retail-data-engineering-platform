import glob
import pandas as pd

files = glob.glob(
    "data/processed/transactions/*.parquet"
)

if len(files) == 0:
    raise Exception("No parquet files found.")

df = pd.concat(
    [pd.read_parquet(f) for f in files],
    ignore_index=True
)

print("=" * 50)
print("DATA VALIDATION")
print("=" * 50)

print(f"Total Records : {len(df)}")
print(f"Columns       : {len(df.columns)}")

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nFirst Five Rows:")
print(df.head())

print("\nValidation Successful")