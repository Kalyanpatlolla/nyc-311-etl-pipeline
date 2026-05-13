from src.extract import extract_data
from src.transform import transform_data
from src.validate import validate_data
from src.load import load_to_warehouse
from src.build_marts import build_marts


def run_pipeline():
    print("Starting ETL Pipeline...\n")

    # Step 1: Extract
    print("===== Step 1/5: Extract =====")
    data = extract_data()
    if data is None:
        print("Extraction failed. Stopping pipeline.")
        return

    # Step 2: Transform
    print("\n===== Step 2/5: Transform =====")
    df = transform_data()
    if df is None or df.empty:
        print("Transformation failed. Stopping pipeline.")
        return

    # Step 3: Validate
    print("\n===== Step 3/5: Validate =====")
    try:
        validate_data()
    except ValueError as e:
        print(f"Validation failed: {e}")
        print("Stopping pipeline. Bad data will NOT be loaded.")
        return

    # Step 4: Load
    print("\n===== Step 4/5: Load =====")
    rows_loaded = load_to_warehouse()

    # Step 5: Build Marts
    print("\n===== Step 5/5: Build Marts =====")
    build_marts()

    print(f"\nPipeline completed successfully. Rows loaded: {rows_loaded}")


if __name__ == "__main__":
    run_pipeline()