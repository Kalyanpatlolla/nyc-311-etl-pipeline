from google.cloud import bigquery
import pandas as pd
import yaml
import os
from dotenv import load_dotenv
load_dotenv()

def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)


def load_to_bigquery():
    config = load_config()

    project_id = os.getenv("GCP_PROJECT_ID")
    dataset_id = config["bigquery"]["dataset"]
    table_id = config["bigquery"]["table"]

    file_path = config["paths"]["processed_data"]

    print("Starting BigQuery load...")

    client = bigquery.Client()

    table_ref = f"{project_id}.{dataset_id}.{table_id}"

    df = pd.read_parquet(file_path)

    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_TRUNCATE"
    )

    job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)

    job.result()

    print(f"Loaded {len(df)} rows into {table_ref}")


if __name__ == "__main__":
    load_to_bigquery()
