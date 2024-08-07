import requests
import json
from assertpy import assert_that
import pytest
from send_request import send_get_req,send_get_by_id,send_register,send_register_no_password,send_create_user


@pytest.mark.qa1
def test_get_users():
    response = send_get_req()
    json_data = response.json()
    print(json.dumps(json_data,indent=2))
    pages = 'total_pages' in json_data.keys()
    if pages:
        print("Exists")
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.ok).is_true()
    assert_that(json_data['data'][0]['id']).is_equal_to(7)


    
@pytest.mark.qa1
def test_register_user_negative(get_payload):
    payload = get_payload['payload_register_no_passwor']
    response  = send_register_no_password(payload)
    json_data = response.json()
    assert_that(response.status_code).is_equal_to(400)
    assert_that(json_data).contains_key("error")
    assert_that(json_data).contains_entry({"error": "Missing password"})


