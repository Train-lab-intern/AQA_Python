import pytest
import allure
from api.endpoint.registration import Registration
from api.endpoint.authentication import Authentication
import test_data


@allure.feature('Authentication')
@allure.story('Authentication with valid email and password')
@pytest.mark.parametrize('login', test_data.LOGINS)
@pytest.mark.parametrize('email', [test_data.EMAIL])
def test_authentication_with_valid_email_and_password(
        connect_db, email, check_existence_and_delete_email, login
):
    register_endpoint = Registration(email, test_data.PASSWORD)
    register_endpoint.create_new_user()
    auth_endpoint = Authentication(login, test_data.PASSWORD)
    auth_endpoint.authentication()
    assert auth_endpoint.returned_200()


@allure.feature('Authentication')
@allure.story('Authentication with incorrect login and incorrect password')
@pytest.mark.parametrize('login', [test_data.EMPTY_FIELD, test_data.NON_EXISTENT_EMAIL])
@pytest.mark.parametrize('password', [test_data.EMPTY_FIELD, test_data.NON_EXISTENT_PASSWORD])
@pytest.mark.parametrize('email', [test_data.EMAIL])
def test_authentication_with_incorrect_login_and_incorrect_password(
        connect_db, email, check_existence_and_delete_email, login, password
):
    register_endpoint = Registration(email, test_data.PASSWORD)
    register_endpoint.create_new_user()
    auth_endpoint = Authentication(login, password)
    auth_endpoint.authentication()
    assert auth_endpoint.returned_400()
    assert auth_endpoint.returned_message_user_not_found(login)
    assert auth_endpoint.returned_status_bad_request()


@allure.feature('Authentication')
@allure.story('Authentication with incorrect email')
@pytest.mark.parametrize('login', [test_data.EMPTY_FIELD, test_data.NON_EXISTENT_EMAIL])
@pytest.mark.parametrize('email', [test_data.EMAIL])
def test_authentication_with_incorrect_email(
        connect_db, email, check_existence_and_delete_email, login
):
    register_endpoint = Registration(email, test_data.PASSWORD)
    register_endpoint.create_new_user()
    auth_endpoint = Authentication(login, test_data.PASSWORD)
    auth_endpoint.authentication()
    assert auth_endpoint.returned_400()
    assert auth_endpoint.returned_message_user_not_found(login)
    assert auth_endpoint.returned_status_bad_request()


@allure.feature('Authentication')
@allure.story('Authentication with incorrect password')
@pytest.mark.parametrize('password', [test_data.EMPTY_FIELD, test_data.NON_EXISTENT_PASSWORD])
@pytest.mark.parametrize('email', [test_data.EMAIL])
def test_authentication_with_incorrect_password(
        connect_db, email, check_existence_and_delete_email, password
):
    register_endpoint = Registration(email, test_data.PASSWORD)
    register_endpoint.create_new_user()
    auth_endpoint = Authentication(email, password)
    auth_endpoint.authentication()
    assert auth_endpoint.returned_400()
    assert auth_endpoint.returned_message_invalid_data_format()
    assert auth_endpoint.returned_status_bad_request()


@allure.feature('Authentication')
@allure.story('Authentication with password in login and login in password')
@pytest.mark.parametrize('email', [test_data.EMAIL])
def test_authentication_with_password_in_login_and_login_in_password(
        connect_db, email, check_existence_and_delete_email
):
    register_endpoint = Registration(email, test_data.PASSWORD)
    register_endpoint.create_new_user()
    auth_endpoint = Authentication(test_data.PASSWORD, test_data.EMAIL)
    auth_endpoint.authentication()
    assert auth_endpoint.returned_400()
    assert auth_endpoint.returned_message_user_not_found(test_data.PASSWORD)
    assert auth_endpoint.returned_status_bad_request()
