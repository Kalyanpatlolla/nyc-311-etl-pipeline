import json
import pandas as pd
import yaml


def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)


def transform_data():
    config = load_config()

    raw_path = config["paths"]["raw_data"]
    processed_path = config["paths"]["processed_data"]

    print("Starting data transformation...")

    with open(raw_path, "r") as f:
        data = json.load(f)

    df = pd.DataFrame(data)

    print(f"Raw records loaded: {len(df)}")

    required_columns = [
        "unique_key",
        "created_date",
        "agency",
        "complaint_type",
        "borough",
        "status"
    ]

    df = df[required_columns].copy()

    df = df.dropna(subset=["unique_key", "created_date", "complaint_type", "borough"])

    df["created_date"] = pd.to_datetime(df["created_date"], errors="coerce")
    df = df.dropna(subset=["created_date"])

    df["borough"] = df["borough"].str.lower().str.strip()
    df["agency"] = df["agency"].str.upper().str.strip()
    df["complaint_type"] = df["complaint_type"].str.strip()
    df["status"] = df["status"].str.strip()

    df["created_hour"] = df["created_date"].dt.hour
    df["created_dayofweek"] = df["created_date"].dt.day_name()

    df = df.drop_duplicates(subset=["unique_key"])

    df.to_parquet(processed_path, index=False)

    print(f"Clean records saved: {len(df)}")
    print(f"Processed file saved to: {processed_path}")

    return df


if __name__ == "__main__":
    transform_data()