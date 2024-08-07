import json
import pytest
from send_request import send_get_by_id
from assertpy import assert_that
from cerberus import Validator

@pytest.mark.qa1
def test_get_user(get_schema):
    schema = get_schema['get_user_schema']
    validator = Validator(schema,require_all=True)
    response = send_get_by_id()
    json_data = response.json()
    print(json.dumps(json_data,indent=2))
    assert_that(response.status_code).is_equal_to(200)
    is_valid = validator.validate(json_data)
    assert_that(is_valid,validator.errors).is_true()
    assert_that(response.ok).is_true()
    for key in json_data['data']:
        assert_that(key).is_empty
        print(f"{key} is not empty")

    assert_that(json_data).contains_key("data")
    assert_that(json_data).contains_key("support")

    assert_that(json_data['data']['id']).is_equal_to(2)
