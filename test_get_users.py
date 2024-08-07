import json
from assertpy import assert_that
import pytest
from send_request import send_get_req
from cerberus import Validator

@pytest.mark.qa1
def test_get_users(get_schema):
    response = send_get_req()
    json_data = response.json()
    print(json.dumps(json_data,indent=2))
    pages = 'total_pages' in json_data.keys()
    if pages:
        print("Exists")
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.ok).is_true()
    assert_that(json_data['data'][0]['id']).is_equal_to(7)