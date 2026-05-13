import requests
import yaml
import json
import time

from src.utils import get_logger

log = get_logger(__name__)


def extract_data():

    log.info("Starting data extraction...")

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

            log.info(f"Data successfully saved to {output_path}")
            log.info(f"Total records fetched: {len(data)}")

            return data

        except Exception as e:

            log.warning(f"Attempt {attempt + 1} failed: {e}")

            time.sleep(2)

    # Fallback logic
    log.error("Extraction failed after retries.")

    try:
        with open(output_path, "r") as f:

            data = json.load(f)

            log.info("Using existing local raw file as fallback.")

            return data

    except Exception:

        log.error("No fallback data available.")

        return None


if __name__ == "__main__":
    extract_data()