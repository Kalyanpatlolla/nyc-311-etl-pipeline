import duckdb
import yaml
import os

from src.utils import get_logger

log = get_logger(__name__)


def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)


def load_to_warehouse():

    config = load_config()

    db_path = config["duckdb"]["database"]
    table_name = config["duckdb"]["table"]
    parquet_path = config["paths"]["processed_data"]

    log.info("Starting DuckDB load...")
    log.info(f"Source parquet: {parquet_path}")
    log.info(f"Target database: {db_path}")
    log.info(f"Target table: {table_name}")

    # Ensure warehouse directory exists
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    # Connect to DuckDB
    con = duckdb.connect(db_path)

    # Load parquet into table
    con.execute(f'''
        CREATE OR REPLACE TABLE {table_name} AS
        SELECT * FROM read_parquet('{parquet_path}')
    ''')

    # Verify load
    row_count = con.execute(
        f"SELECT COUNT(*) FROM {table_name}"
    ).fetchone()[0]

    column_count = len(
        con.execute(f"DESCRIBE {table_name}").fetchall()
    )

    log.info(f"Loaded {row_count} rows into {table_name}")
    log.info(f"Schema: {column_count} columns")

    con.close()

    return row_count


if __name__ == "__main__":
    load_to_warehouse()