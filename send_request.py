import requests
from conf import *

def send_get_req():
    url = f"{base_url}/users"
    response = requests.get(url,params={"page":"2"})
    return response

def send_get_by_id():
    url = f"{base_url}/users/2"
    response = requests.get(url)
    return response


def send_register(payload):
    url = f"{base_url}/register"
    response = requests.post(url,json=payload)
    return response

def send_register_no_password(payload):
    url = "https://reqres.in/api/register"
    response = requests.post(url,json=payload)
    return response


def send_create_user(payload):
    url = "https://reqres.in/api/users"
    response = requests.post(url,json=payload)
    return response