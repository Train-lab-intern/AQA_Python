import pytest
import allure
from api import base_method
from api import test_data


@allure.feature('Registration')
@allure.story('Send a request with a valid email')
@pytest.mark.parametrize('email', test_data.valid_email)
def test_check_valid_emails(connect_db, email, check_existence_and_delete_email):
    with allure.step('Send request to create user'):
        response = base_method.post_request_create_user(
            f'{email}', test_data.username, test_data.password
        )
    with allure.step('Check status code'):
        assert response.status_code == 200, f'line length is equal {len(email)}'


@allure.feature('Registration')
@allure.story('Send a request with an invalid email address')
@pytest.mark.parametrize('email', test_data.invalid_emails)
def test_check_invalid_emails(connect_db, email, check_existence_and_delete_email):
    with allure.step('Send request to create user'):
        response = base_method.post_request_create_user(
            f'{email}', test_data.username, test_data.password
        )
    with allure.step('Check status code'):
        assert response.status_code == 400, f'line length is equal {len(email)}'


@allure.feature('Registration')
@allure.story('Check username')
@pytest.mark.parametrize('username', test_data.usernames)
@pytest.mark.parametrize('email', [test_data.email])
def test_username(connect_db, username, check_existence_and_delete_email, email):
    with allure.step('Send request to create user'):
        response = base_method.post_request_create_user(
            f'{email}', f'{username}', test_data.password
        )
    with allure.step('Check status code'):
        assert response.status_code == 200


@allure.feature('Registration')
@allure.story('Send a request with an valid password')
@pytest.mark.parametrize('password', test_data.valid_password)
@pytest.mark.parametrize('email', [test_data.email])
def test_valid_password(connect_db, password, email, check_existence_and_delete_email):
    with allure.step('Send request to create user'):
        response = base_method.post_request_create_user(f'{email}', test_data.username, f'{password}')
    with allure.step('Check status code'):
        assert response.status_code == 200, f'{password}, line length is equal {len(password)}'


@allure.feature('Registration')
@allure.story('Send a request with an invalid password')
@pytest.mark.parametrize('password', test_data.invalid_password)
@pytest.mark.parametrize('email', [test_data.email])
def test_invalid_password(connect_db, password, email, check_existence_and_delete_email):
    with allure.step('Send request to create user'):
        response = base_method.post_request_create_user(f'{email}', test_data.username, f'{password}')
    with allure.step('Check status code'):
        assert response.status_code == 400, f'{password}, line length is equal {len(password)}'


@allure.feature('Registration')
@allure.story('Send a request with empty fields')
def test_registration_with_empty_fields(connect_db):
    with allure.step('Send request to create user'):
        response = base_method.post_request_create_user(
            test_data.empty_field, test_data.empty_field, test_data.empty_field
        )
    with allure.step('Check status code'):
        assert response.status_code == 400


@allure.feature('Registration')
@allure.story('Send a request with empty username and password')
def test_registration_with_empty_username_and_password(connect_db):
    with allure.step('Send request to create user'):
        response = base_method.post_request_create_user(
            test_data.email, test_data.empty_field, test_data.empty_field
        )
    with allure.step('Check status code'):
        assert response.status_code == 400


@allure.feature('Registration')
@allure.story('Send a request with empty email and password')
def test_registration_with_empty_email_and_password(connect_db):
    with allure.step('Send request to create user'):
        response = base_method.post_request_create_user(
            test_data.empty_field, test_data.username, test_data.empty_field
        )
    with allure.step('Check status code'):
        assert response.status_code == 400


@allure.feature('Registration')
@allure.story('Send a request with empty username and email')
def test_registration_with_empty_username_and_email(connect_db):
    with allure.step('Send request to create user'):
        response = base_method.post_request_create_user(
            test_data.empty_field, test_data.empty_field, test_data.password
        )
    with allure.step('Check status code'):
        assert response.status_code == 400


@allure.feature('Registration')
@allure.story('Send a request with data existing user')
@pytest.mark.parametrize('email', [test_data.email])
def test_registration_with_existing_user(connect_db, check_existence_and_delete_email, email):
    with allure.step('Send request to create user'):
        base_method.post_request_create_user(
            f'{email}', test_data.username, test_data.password
        )
    with allure.step('Send a request with existing data'):
        response = base_method.post_request_create_user(
            f'{email}', test_data.username, test_data.password
        )
    with allure.step('Check status code'):
        assert response.status_code == 400


@allure.feature('Registration')
@allure.story('Send a request confirm registration')
@pytest.mark.parametrize('email', ['test.trainlab@gmail.com'])
def test_confirm_registration(connect_db, check_existence_and_delete_email, email):
    with allure.step('Send request to create user'):
        base_method.post_request_create_user(
            f'{email}', test_data.username, test_data.password
        )
    with allure.step('Send request confirm registration'):
        base_method.get_request_confirm_registration(f'{email}')
    with allure.step('Send a login request'):
        response = base_method.post_request_authentication(f'{email}', test_data.password)
        response_user_data = response.json()
        user_id = response_user_data['userDto']['id']
    with allure.step('Check status code'):
        assert response.status_code == 200
    with allure.step('Delete session'):
        base_method.delete_session(connect_db, user_id)
