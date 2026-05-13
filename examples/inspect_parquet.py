import pandas as pd

PARQUET_PATH = "data/processed/nyc_311_clean.parquet"

print("Loading parquet file...\n")

df = pd.read_parquet(PARQUET_PATH)

print("First 5 rows:\n")
print(df.head())

print("\nShape of dataset:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:\n")
print(df.dtypes)