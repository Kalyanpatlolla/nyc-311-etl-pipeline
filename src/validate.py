import pandas as pd
import yaml

from src.utils import get_logger

log = get_logger(__name__)


def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)


def validate_data():
    log.info("Starting data validation...")

    config = load_config()
    parquet_path = config["paths"]["processed_data"]

    df = pd.read_parquet(parquet_path)

    log.info(f"Rows loaded for validation: {len(df)}")

    # Validation 1: Empty dataset
    if df.empty:
        raise ValueError("Validation failed: dataset is empty")

    log.info("Passed: dataset is not empty")

    # Validation 2: Duplicate IDs
    duplicate_count = df["unique_key"].duplicated().sum()

    if duplicate_count > 0:
        raise ValueError(
            f"Validation failed: found {duplicate_count} duplicate unique_key values"
        )

    log.info("Passed: no duplicate unique_key values")

    # Validation 3: Borough values
    valid_boroughs = {
        "brooklyn",
        "bronx",
        "manhattan",
        "queens",
        "staten island",
    }

    invalid_boroughs = set(df["borough"].dropna().unique()) - valid_boroughs

    if invalid_boroughs:
        raise ValueError(
            f"Validation failed: invalid borough values found: {invalid_boroughs}"
        )

    log.info("Passed: borough values are valid")
    log.info("All validation checks passed!")

    return True


if __name__ == "__main__":
    validate_data()