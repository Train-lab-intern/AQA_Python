import json
import requests

BASE_URL = 'https://test.app.it-roast.com'


def post_request_create_user(email, username, password):
    register_user = '/api/v1/users/register'
    headers = {
        'Content-Type': 'application/json'
    }
    data = json.dumps({
        "username": f"{username}",
        "email": f"{email}",
        "password": f"{password}"
    })
    request = requests.request('POST', BASE_URL + register_user, headers=headers,
                               data=data, timeout=20)
    return request


def get_request_confirm_registration(email):
    complete_registration = '/api/v1/users/complete-registration'
    params = {
        'userEmail': f'{email}'
    }
    request = requests.request(
        'GET', BASE_URL + complete_registration, params=params, timeout=20
    )
    return request


def post_request_authentication(email, password):
    authentication_url = '/api/v1/auth'
    headers = {
        'Content-Type': 'application/json'
    }
    data = json.dumps({
        "userEmail": f"{email}",
        "userPassword": f"{password}"
    })
    request = requests.request(
        'POST', BASE_URL + authentication_url, data=data, headers=headers, timeout=20
    )
    return request

