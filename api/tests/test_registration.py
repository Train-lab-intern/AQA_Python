import pytest
import allure
from api.endpoint.registration import Registration
import test_data


@allure.feature('Registration')
@allure.story('Send a request with a valid email')
@pytest.mark.parametrize('email', test_data.VALID_EMAILS)
def test_check_valid_emails(connect_db, email, check_existence_and_delete_email):
    register_endpoint = Registration(email, test_data.PASSWORD)
    register_endpoint.create_new_user()
    assert register_endpoint.returned_200()


@allure.feature('Registration')
@allure.story('Send a request with an invalid email address')
@pytest.mark.parametrize('email', test_data.INVALID_EMAILS)
def test_check_invalid_emails(connect_db, email, check_existence_and_delete_email):
    register_endpoint = Registration(email, test_data.PASSWORD)
    register_endpoint.create_new_user()
    assert register_endpoint.returned_400()
    assert register_endpoint.returned_message_invalid_email_address()
    assert register_endpoint.returned_status_bad_request()


@allure.feature('Registration')
@allure.story('Send a request with a 257 characters email address')
@pytest.mark.parametrize('email', test_data.EMAIL_257_CHARACTERS)
def test_check_257_characters_emails(connect_db, email, check_existence_and_delete_email):
    register_endpoint = Registration(email, test_data.PASSWORD)
    register_endpoint.create_new_user()
    assert register_endpoint.returned_400()
    assert register_endpoint.returned_message_email_must_be_between_8_and_256_characters()
    assert register_endpoint.returned_status_bad_request()


@allure.feature('Registration')
@allure.story('Send a request with an valid password')
@pytest.mark.parametrize('password', test_data.VALID_PASSWORD)
@pytest.mark.parametrize('email', [test_data.EMAIL])
def test_valid_password(connect_db, password, email, check_existence_and_delete_email):
    register_endpoint = Registration(email, password)
    register_endpoint.create_new_user()
    assert register_endpoint.returned_200()


@allure.feature('Registration')
@allure.story('Send a request with an invalid password')
@pytest.mark.parametrize('password', test_data.INVALID_PASSWORD)
@pytest.mark.parametrize('email', [test_data.EMAIL])
def test_invalid_password(connect_db, password, email, check_existence_and_delete_email):
    register_endpoint = Registration(email, password)
    register_endpoint.create_new_user()
    assert register_endpoint.returned_400()
    assert register_endpoint.returned_status_bad_request()


@allure.feature('Registration')
@allure.story('Send a request with empty fields')
@pytest.mark.parametrize('password', [test_data.EMPTY_FIELD, test_data.SPACES])
@pytest.mark.parametrize('email', [test_data.EMPTY_FIELD, test_data.SPACES])
def test_registration_with_empty_and_spaces_in_fields(connect_db, email, password):
    register_endpoint = Registration(email, password)
    register_endpoint.create_new_user()
    assert register_endpoint.returned_400()
    assert register_endpoint.returned_status_bad_request()
    assert register_endpoint.returned_message_email_and_password_fields_are_required()


@allure.feature('Registration')
@allure.story('Send a request with empty password')
@pytest.mark.parametrize('password', [test_data.EMPTY_FIELD, test_data.SPACES])
def test_registration_with_empty_amd_spaces_in_password(connect_db, password):
    register_endpoint = Registration(
        test_data.EMAIL, password
    )
    register_endpoint.create_new_user()
    assert register_endpoint.returned_400()
    assert register_endpoint.returned_status_bad_request()
    assert register_endpoint.returned_message_password_field_is_required()


@allure.feature('Registration')
@allure.story('Send a request with empty email')
@pytest.mark.parametrize('email', [test_data.EMPTY_FIELD, test_data.SPACES])
def test_registration_with_empty_and_spaces_in_email(connect_db, email):
    register_endpoint = Registration(
        email, test_data.PASSWORD
    )
    register_endpoint.create_new_user()
    assert register_endpoint.returned_400()
    assert register_endpoint.returned_status_bad_request()
    assert register_endpoint.returned_message_email_field_is_required()


@allure.feature('Registration')
@allure.story('Send a request with data existing user')
@pytest.mark.parametrize('email', [test_data.EMAIL])
def test_registration_with_existing_user(connect_db, check_existence_and_delete_email, email):
    register_endpoint = Registration(email, test_data.PASSWORD)
    register_endpoint.create_new_user()
    register_endpoint.create_new_user()
    assert register_endpoint.returned_400()
    assert register_endpoint.returned_status_bad_request()
    assert register_endpoint.returned_message_user_exists()
