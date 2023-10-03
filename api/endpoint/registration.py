import allure
from api.endpoint.base_method import BaseMethod


class Registration(BaseMethod):

    def create_new_user(self, email, username, password):
        with allure.step('Send request to create user'):
            response = self.post_request_create_user(
                f'{email}', username, password
            )
            return response

    def confirm_registration(self, email):
        with allure.step('Send request confirm registration'):
            return self.get_request_confirm_registration(f'{email}')

    def authentication(self, email, password):
        with allure.step('Send a login request'):
            return self.post_request_authentication(f'{email}', password)
