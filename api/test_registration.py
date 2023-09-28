import pytest
import allure
from api import base_method
from api import test_data


@allure.feature('Registration')
@allure.story('Send a request with a valid email')
@pytest.mark.parametrize('email', test_data.VALID_EMAIL)
def test_check_valid_emails(connect_db, email, check_existence_and_delete_email):
    with allure.step('Send request to create user'):
        response = base_method.post_request_create_user(
            f'{email}', test_data.USERNAME, test_data.PASSWORD
        )
    with allure.step('Check status code'):
        assert response.status_code == 200, f'line length is equal {len(email)}'


@allure.feature('Registration')
@allure.story('Send a request with an invalid email address')
@pytest.mark.parametrize('email', test_data.INVALID_EMAIL)
def test_check_invalid_emails(connect_db, email, check_existence_and_delete_email):
    with allure.step('Send request to create user'):
        response = base_method.post_request_create_user(
            f'{email}', test_data.USERNAME, test_data.PASSWORD
        )
    with allure.step('Check status code'):
        assert response.status_code == 400, f'line length is equal {len(email)}'


@allure.feature('Registration')
@allure.story('Check username')
@pytest.mark.parametrize('username', test_data.USERNAMES)
@pytest.mark.parametrize('email', [test_data.EMAIL])
def test_username(connect_db, username, check_existence_and_delete_email, email):
    with allure.step('Send request to create user'):
        response = base_method.post_request_create_user(
            f'{email}', f'{username}', test_data.PASSWORD
        )
    with allure.step('Check status code'):
        assert response.status_code == 200


@allure.feature('Registration')
@allure.story('Send a request with an valid password')
@pytest.mark.parametrize('password', test_data.VALID_PASSWORD)
@pytest.mark.parametrize('email', [test_data.EMAIL])
def test_valid_password(connect_db, password, email, check_existence_and_delete_email):
    with allure.step('Send request to create user'):
        response = base_method.post_request_create_user(
            f'{email}', test_data.USERNAME, f'{password}'
        )
    with allure.step('Check status code'):
        assert response.status_code == 200, f'{password}, line length is equal {len(password)}'


@allure.feature('Registration')
@allure.story('Send a request with an invalid password')
@pytest.mark.parametrize('password', test_data.INVALID_PASSWORD)
@pytest.mark.parametrize('email', [test_data.EMAIL])
def test_invalid_password(connect_db, password, email, check_existence_and_delete_email):
    with allure.step('Send request to create user'):
        response = base_method.post_request_create_user(
            f'{email}', test_data.USERNAME, f'{password}'
        )
    with allure.step('Check status code'):
        assert response.status_code == 400, f'{password}, line length is equal {len(password)}'


@allure.feature('Registration')
@allure.story('Send a request with empty fields')
def test_registration_with_empty_fields(connect_db):
    with allure.step('Send request to create user'):
        response = base_method.post_request_create_user(
            test_data.EMPTY_FIELD, test_data.EMPTY_FIELD, test_data.EMPTY_FIELD
        )
    with allure.step('Check status code'):
        assert response.status_code == 400


@allure.feature('Registration')
@allure.story('Send a request with empty username and password')
def test_registration_with_empty_username_and_password(connect_db):
    with allure.step('Send request to create user'):
        response = base_method.post_request_create_user(
            test_data.EMAIL, test_data.EMPTY_FIELD, test_data.EMPTY_FIELD
        )
    with allure.step('Check status code'):
        assert response.status_code == 400


@allure.feature('Registration')
@allure.story('Send a request with empty email and password')
def test_registration_with_empty_email_and_password(connect_db):
    with allure.step('Send request to create user'):
        response = base_method.post_request_create_user(
            test_data.EMPTY_FIELD, test_data.USERNAME, test_data.EMPTY_FIELD
        )
    with allure.step('Check status code'):
        assert response.status_code == 400


@allure.feature('Registration')
@allure.story('Send a request with empty username and email')
def test_registration_with_empty_username_and_email(connect_db):
    with allure.step('Send request to create user'):
        response = base_method.post_request_create_user(
            test_data.EMPTY_FIELD, test_data.EMPTY_FIELD, test_data.PASSWORD
        )
    with allure.step('Check status code'):
        assert response.status_code == 400


@allure.feature('Registration')
@allure.story('Send a request with data existing user')
@pytest.mark.parametrize('email', [test_data.EMAIL])
def test_registration_with_existing_user(connect_db, check_existence_and_delete_email, email):
    with allure.step('Send request to create user'):
        base_method.post_request_create_user(
            f'{email}', test_data.USERNAME, test_data.PASSWORD
        )
    with allure.step('Send a request with existing data'):
        response = base_method.post_request_create_user(
            f'{email}', test_data.USERNAME, test_data.PASSWORD
        )
    with allure.step('Check status code'):
        assert response.status_code == 400


@allure.feature('Registration')
@allure.story('Send a request confirm registration')
@pytest.mark.parametrize('email', [test_data.EMAIL])
def test_confirm_registration(
        connect_db, check_existence_and_delete_email, email, delete_session
):
    with allure.step('Send request to create user'):
        base_method.post_request_create_user(
            f'{email}', test_data.USERNAME, test_data.PASSWORD
        )
    with allure.step('Send request confirm registration'):
        base_method.get_request_confirm_registration(f'{email}')
    with allure.step('Send a login request'):
        response = base_method.post_request_authentication(f'{email}', test_data.PASSWORD)
    with allure.step('Check status code'):
        assert response.status_code == 200
