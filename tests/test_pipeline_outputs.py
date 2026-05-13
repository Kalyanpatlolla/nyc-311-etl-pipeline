from pathlib import Path


def test_raw_json_exists():
    raw_file = Path("data/raw/nyc_311_raw.json")
    assert raw_file.exists(), "Raw JSON file does not exist"


def test_processed_parquet_exists():
    parquet_file = Path("data/processed/nyc_311_clean.parquet")
    assert parquet_file.exists(), "Processed parquet file does not exist"


def test_duckdb_warehouse_exists():
    warehouse_file = Path("data/warehouse/nyc_311.duckdb")
    assert warehouse_file.exists(), "DuckDB warehouse file does not exist"