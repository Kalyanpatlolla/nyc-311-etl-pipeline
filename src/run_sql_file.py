import duckdb
import yaml

from src.utils import get_logger

log = get_logger(__name__)


def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)


def run_sql_file(sql_path):
    config = load_config()
    db_path = config["duckdb"]["database"]

    log.info(f"Connecting to DuckDB: {db_path}")
    log.info(f"Running SQL file: {sql_path}")

    with open(sql_path, "r") as f:
        sql = f.read()

    con = duckdb.connect(db_path)
    con.execute(sql)
    con.close()

    log.info("SQL executed successfully.")


if __name__ == "__main__":
    run_sql_file("queries/create_staging_view.sql")