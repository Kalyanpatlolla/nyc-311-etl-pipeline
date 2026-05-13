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
FROM mart_top_complaints
LIMIT 10;
"""

results = con.execute(query).fetchall()

print("\nTop Complaint Results:\n")

for row in results:
    print(row)

con.close()

print("\nConnection closed.")