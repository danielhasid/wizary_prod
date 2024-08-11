
import json
import pytest

@pytest.fixture(scope="session")
def get_payload():
    with open("../payload/json_data.json", "r") as file:
        data = json.load(file)
        return data

@pytest.fixture(scope="session")
def get_schema():
    with open("../payload/expected_schem.json", "r") as file:
        data = json.load(file)
        return data
    