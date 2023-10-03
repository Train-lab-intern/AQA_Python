import pytest
import allure
from api.endpoint.registration import Registration
from api import test_data


@allure.feature('Registration')
@allure.story('Send a request with a valid email')
@pytest.mark.parametrize('email', test_data.VALID_EMAILS)
def test_check_valid_emails(connect_db, email, check_existence_and_delete_email):
    register_endpoint = Registration()
    response = register_endpoint.create_new_user(email, test_data.USERNAME, test_data.PASSWORD)
    assert response.status_code == 200
    assert response.text == 'Registration initiated.' \
                            ' Please check your email for further instructions.'


@allure.feature('Registration')
@allure.story('Send a request with an invalid email address')
@pytest.mark.parametrize('email', test_data.INVALID_EMAILS)
def test_check_invalid_emails(connect_db, email, check_existence_and_delete_email):
    register_endpoint = Registration()
    response = register_endpoint.create_new_user(email, test_data.USERNAME, test_data.PASSWORD)
    response_data = response.json()
    message = response_data['message']
    status = response_data['status']
    assert response.status_code == 400
    assert message == 'Invalid email address'
    assert status == 'BAD_REQUEST'


@allure.feature('Registration')
@allure.story('Check username')
@pytest.mark.parametrize('username', test_data.USERNAMES)
@pytest.mark.parametrize('email', [test_data.EMAIL])
def test_username(connect_db, username, check_existence_and_delete_email, email):
    register_endpoint = Registration()
    response = register_endpoint.create_new_user(email, username, test_data.PASSWORD)
    assert response.status_code == 200
    assert response.text == 'Registration initiated.' \
                            ' Please check your email for further instructions.'


@allure.feature('Registration')
@allure.story('Send a request with an valid password')
@pytest.mark.parametrize('password', test_data.VALID_PASSWORD)
@pytest.mark.parametrize('email', [test_data.EMAIL])
def test_valid_password(connect_db, password, email, check_existence_and_delete_email):
    register_endpoint = Registration()
    response = register_endpoint.create_new_user(email, test_data.USERNAME, password)
    assert response.status_code == 200
    assert response.text == 'Registration initiated.' \
                            ' Please check your email for further instructions.'


@allure.feature('Registration')
@allure.story('Send a request with an invalid password')
@pytest.mark.parametrize('password', test_data.INVALID_PASSWORD)
@pytest.mark.parametrize('email', [test_data.EMAIL])
def test_invalid_password(connect_db, password, email, check_existence_and_delete_email):
    register_endpoint = Registration()
    response = register_endpoint.create_new_user(email, test_data.USERNAME, password)
    body = response.json()
    status = body['status']
    assert response.status_code == 400
    assert status == 'BAD_REQUEST'


@allure.feature('Registration')
@allure.story('Send a request with empty fields')
def test_registration_with_empty_fields(connect_db):
    register_endpoint = Registration()
    response = register_endpoint.create_new_user(
        test_data.EMPTY_FIELD, test_data.EMPTY_FIELD, test_data.EMPTY_FIELD
    )
    body = response.json()
    status = body['status']
    assert response.status_code == 400
    assert status == 'BAD_REQUEST'


@allure.feature('Registration')
@allure.story('Send a request with empty username and password')
def test_registration_with_empty_username_and_password(connect_db):
    register_endpoint = Registration()
    response = register_endpoint.create_new_user(
        test_data.EMAIL, test_data.EMPTY_FIELD, test_data.EMPTY_FIELD
    )
    body = response.json()
    status = body['status']
    assert response.status_code == 400
    assert status == 'BAD_REQUEST'


@allure.feature('Registration')
@allure.story('Send a request with empty email and password')
def test_registration_with_empty_email_and_password(connect_db):
    register_endpoint = Registration()
    response = register_endpoint.create_new_user(
        test_data.EMPTY_FIELD, test_data.USERNAME, test_data.EMPTY_FIELD
    )
    body = response.json()
    status = body['status']
    assert response.status_code == 400
    assert status == 'BAD_REQUEST'


@allure.feature('Registration')
@allure.story('Send a request with empty username and email')
def test_registration_with_empty_username_and_email(connect_db):
    register_endpoint = Registration()
    response = register_endpoint.create_new_user(
        test_data.EMPTY_FIELD, test_data.EMPTY_FIELD, test_data.PASSWORD
    )
    body = response.json()
    status = body['status']
    message = body['message']
    assert response.status_code == 400
    assert status == 'BAD_REQUEST'
    assert message == 'User email must be between 8 and 256 characters'


@allure.feature('Registration')
@allure.story('Send a request with data existing user')
@pytest.mark.parametrize('email', [test_data.EMAIL])
def test_registration_with_existing_user(connect_db, check_existence_and_delete_email, email):
    register_endpoint = Registration()
    register_endpoint.create_new_user(
        email, test_data.USERNAME, test_data.PASSWORD
    )
    response = register_endpoint.post_request_create_user(
        email, test_data.USERNAME, test_data.PASSWORD
    )
    body = response.json()
    status = body['status']
    message = body['message']
    assert response.status_code == 400
    assert status == 'BAD_REQUEST'
    assert message == 'User with this username is already exists.'


@allure.feature('Registration')
@allure.story('Send a request confirm registration')
@pytest.mark.parametrize('email', [test_data.EMAIL])
def test_confirm_registration(
        connect_db, check_existence_and_delete_email, email, delete_session
):
    register_endpoint = Registration()
    register_endpoint.create_new_user(
        email, test_data.USERNAME, test_data.PASSWORD
    )
    response = register_endpoint.confirm_registration(email)
    assert response.status_code == 200
    assert response.text == 'Registration completed successfully!'


@allure.feature('Registration')
@allure.story('Send a request confirm registration')
@pytest.mark.parametrize('email', [test_data.EMAIL])
def test_confirm_registration_with_invalid_email(
        connect_db, check_existence_and_delete_email, email, delete_session
):
    register_endpoint = Registration()
    register_endpoint.create_new_user(
        email, test_data.USERNAME, test_data.PASSWORD
    )
    response = register_endpoint.confirm_registration(test_data.NON_EXISTENT_EMAIL)
    body = response.json()
    status = body['status']
    message = body['message']
    assert response.status_code == 400
    assert status == 'BAD_REQUEST'
    assert message == f'User not found with email: {test_data.NON_EXISTENT_EMAIL}'
