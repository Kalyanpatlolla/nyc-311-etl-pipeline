import duckdb
import yaml


def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)


config = load_config()

db_path = config["duckdb"]["database"]

print(f"Connecting to DuckDB: {db_path}")

con = duckdb.connect(db_path)

query = """
SELECT *
FROM mart_peak_hours;
"""

results = con.execute(query).fetchall()

print("\nPeak Hour Results:\n")

for row in results:
    print(row)

con.close()

print("\nConnection closed.")