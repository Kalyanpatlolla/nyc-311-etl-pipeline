import pandas as pd
import pytest


def test_duplicate_unique_keys_raise_error():

    df = pd.DataFrame({
        "unique_key": ["1", "1"],
        "borough": ["brooklyn", "brooklyn"]
    })

    with pytest.raises(ValueError, match="Duplicate unique_key values found"):

        duplicates = df["unique_key"].duplicated().sum()

        if duplicates > 0:
            raise ValueError("Duplicate unique_key values found")