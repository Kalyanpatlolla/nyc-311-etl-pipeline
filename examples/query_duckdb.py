import duckdb

DB_PATH = "data/warehouse/nyc_311.duckdb"

print("Connecting to DuckDB warehouse...")

conn = duckdb.connect(DB_PATH)

query = """
SELECT
    borough,
    COUNT(*) AS total_complaints
FROM service_requests
GROUP BY borough
HAVING COUNT(*) > 10
ORDER BY total_complaints DESC;
"""

print("Running HAVING query...")

results = conn.execute(query).fetchall()

print("\nBoroughs with more than 10 complaints:\n")

for row in results:
    print(row)

conn.close()

print("\nConnection closed.")