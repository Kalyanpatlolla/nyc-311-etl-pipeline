from src.run_sql_file import run_sql_file
from src.utils import get_logger

log = get_logger(__name__)


def build_marts():
    log.info("Starting warehouse mart build...")

    sql_files = [
        "queries/create_staging_view.sql",
        "queries/create_mart_complaints_by_borough.sql",
        "queries/create_mart_peak_hours.sql",
        "queries/create_mart_top_complaints.sql",
    ]

    for sql_file in sql_files:
        log.info(f"Running SQL file: {sql_file}")
        run_sql_file(sql_file)

    log.info("All warehouse marts built successfully.")


if __name__ == "__main__":
    build_marts()