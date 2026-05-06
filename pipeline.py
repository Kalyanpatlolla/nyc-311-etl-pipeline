from src.extract import extract_data
from src.transform import transform_data
from src.load import load_to_bigquery


def run_pipeline():
    print("🚀 Starting ETL Pipeline...\n")

    print("🔹 Step 1: Extract")
    data = extract_data()
    if data is None:
        print("❌ Extraction failed. Stopping pipeline.")
        return

    print("\n🔹 Step 2: Transform")
    df = transform_data()
    if df is None or df.empty:
        print("❌ Transformation failed. Stopping pipeline.")
        return

    print("\n🔹 Step 3: Load")
    load_to_bigquery()

    print("\n✅ Pipeline completed successfully!")


if __name__ == "__main__":
    run_pipeline()