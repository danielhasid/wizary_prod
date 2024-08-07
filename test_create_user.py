import json
import pytest
from assertpy import assert_that
from send_request import send_create_user

@pytest.mark.qa1
def test_create_user(get_payload):
    json_data = get_payload
    payload = json_data['payload_create_user']
    response  = send_create_user(payload)
    json_data = response.json()
    assert_that(response.status_code).is_equal_to(201)
    assert_that(response.reason).is_equal_to('Created')
    print(json.dumps(json_data,indent=2))
    # name_entry = {"name": payload['name']}
    # assert_that(json_data).contains_entry(name_entry)
    assert_that(json_data['name']).is_equal_to(payload['name'])

