import requests
import yaml
import json
import time


def extract_data():
    print("Starting data extraction...")

    # Load config
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    url = config["api"]["url"]
    limit = config["api"]["limit"]
    output_path = config["paths"]["raw_data"]

    params = {
        "$limit": limit,
        "$order": "created_date DESC"
    }

    max_retries = 3

    for attempt in range(max_retries):
        try:
            response = requests.get(url, params=params, timeout=30)
            response.raise_for_status()

            data = response.json()

            with open(output_path, "w") as f:
                json.dump(data, f)

            print(f"Data successfully saved to {output_path}")
            print(f"Total records fetched: {len(data)}")

            return data

        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(2)

    # ❌ After retries fail → fallback logic
    print("Extraction failed after retries.")

    try:
        with open(output_path, "r") as f:
            data = json.load(f)
            print("Using existing local raw file as fallback.")
            return data
    except Exception:
        print("No fallback data available.")
        return None