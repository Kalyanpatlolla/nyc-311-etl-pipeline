from src.validate import validate_data


def test_validate_data_passes():
    result = validate_data()
    assert result is True