import json
import requests
from api import settings


class BaseMethod:

    def __init__(self):
        self.base_url = settings.BASE_URL
        self.register_user = settings.REGISTER_USER
        self.authentication_url = settings.AUTHENTICATION_URL

    def post_request_create_user(self, email, password):
        headers = {
            'Content-Type': 'application/json'
        }
        data = json.dumps({
            "email": f"{email}",
            "password": f"{password}"
        })
        request = requests.request('POST', self.base_url + self.register_user, headers=headers,
                                   data=data, timeout=20)
        return request

    def post_request_authentication(self, email, password):
        headers = {
            'Content-Type': 'application/json'
        }
        data = json.dumps({
            "userEmail": f"{email}",
            "userPassword": f"{password}"
        })
        request = requests.request(
            'POST', self.base_url + self.authentication_url, data=data, headers=headers, timeout=20
        )
        return request
