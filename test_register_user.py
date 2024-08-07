import pytest
import json
from assertpy import assert_that
from send_request import send_register
from cerberus import Validator

@pytest.mark.qa1
def test_register_user(get_payload,get_schema):
    schema = get_schema['register_user_schema'] #validate schema 
    payload = get_payload['payload_register_user']
    response = send_register(payload)
    validator = Validator(schema,require_all=True)#validate schema 
    json_data = response.json()

    assert_that(response.status_code).is_equal_to(200)
    is_valid = validator.validate(json_data)
    assert_that(is_valid,validator.errors).is_true()#validate correct schem
    assert_that(json_data).contains_key("id")
    assert_that(json_data).contains_key("token")
