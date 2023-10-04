import allure
from api.endpoint.base_method import BaseMethod


class Authentication(BaseMethod):

    def __init__(self, login, password):
        super().__init__()
        self.response = None
        self.login = login
        self.password = password

    def authentication(self):
        with allure.step('Send a login request'):
            self.response = self.post_request_authentication(self.login, self.password)
            return self.response

    def returned_200(self):
        with allure.step('Check status code 200'):
            return self.response.status_code == 200

    def returned_400(self):
        with allure.step('Check status code 400'):
            return self.response.status_code == 400

    def returned_status_bad_request(self):
        with allure.step('Check response status'):
            response_data = self.response.json()
            status = response_data['status']
            return status == 'BAD_REQUEST'

    def returned_message_user_not_found(self, email):
        with allure.step('Check response message'):
            response_data = self.response.json()
            message = response_data['message']
            return message == f'User not found with email: {email}'

    def returned_message_invalid_data_format(self):
        with allure.step('Check response message'):
            response_data = self.response.json()
            message = response_data['message']
            return message == 'Bad credentials'
