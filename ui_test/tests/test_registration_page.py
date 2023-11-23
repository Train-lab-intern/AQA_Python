import allure
import pytest
import test_data
from ui_test.pages.registration_page import RegistrationPage


@allure.feature('Registration page')
@allure.story('Open site')
def test_open_registration_page(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open()
    assert registration_page.current_url()


@allure.feature('Registration page')
@allure.story('Logo site')
def test_logo_site_is_displayed(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open()
    assert registration_page.logo_is_displayed()


@allure.feature('Registration page')
@allure.story('Logo site')
def test_click_logo_site_in_registration_page(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open()
    registration_page.click_logo_site()
    assert registration_page.check_url_home_page()


@allure.feature('Registration page')
@allure.story('Welcome text')
def test_welcome_text_in_registration_page_is_displayed(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open()
    assert registration_page.welcome_text_is_displayed()


@allure.feature('Registration page')
@allure.story('Welcome text')
def test_check_welcome_text(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open()
    assert registration_page.check_welcome_text()


@allure.feature('Registration page')
@allure.story('Email field')
def test_email_field_is_displayed(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open()
    assert registration_page.email_field_is_displayed()


@allure.feature('Registration page')
@allure.story('Email field')
def test_email_field_text(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open()
    assert registration_page.email_field_text()


@allure.feature('Registration page')
@allure.story('Login field')
def test_login_field_is_displayed(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open()
    assert registration_page.login_field_is_displayed()


@allure.feature('Registration page')
@allure.story('Login field')
def test_login_field_text(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open()
    assert registration_page.login_field_text()


@allure.feature('Registration page')
@allure.story('Password field')
def test_password_field_is_displayed(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open()
    assert registration_page.password_field_is_displayed()


@allure.feature('Registration page')
@allure.story('Password field')
def test_password_field_text(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open()
    assert registration_page.password_field_text()


@allure.feature('Registration page')
@allure.story('Password field')
def test_password_view_icon_is_displayed_in_password_field(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open()
    assert registration_page.password_view_icon_is_displayed()


@allure.feature('Registration page')
@allure.story('Password field')
def test_password_view_icon_click_in_password_field(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open()
    registration_page.password_view_icon_click()
    assert registration_page.type_password_field()


@allure.feature('Registration page')
@allure.story('Confirm password field')
def test_confirm_password_field_is_displayed(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open()
    assert registration_page.confirm_password_field_is_displayed()


@allure.feature('Registration page')
@allure.story('Confirm password field')
def test_confirm_password_field_text(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open()
    assert registration_page.confirm_password_field_text()


@allure.feature('Registration page')
@allure.story('Confirm password field')
def test_password_view_icon_is_displayed_in_confirm_password_field(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open()
    assert registration_page.confirm_password_field_is_displayed()


@allure.feature('Registration page')
@allure.story('Confirm password field')
def test_type_confirm_password_field_in_confirm_password_field(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open()
    registration_page.confirm_password_view_icon_click()
    assert registration_page.type_confirm_password_field()


@allure.feature('Registration page')
@allure.story('Register button')
def test_register_button_is_displayed(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open()
    assert registration_page.register_button_is_displayed()


@allure.feature('Registration page')
@allure.story('Register button')
def test_register_button_text(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open()
    assert registration_page.register_button_text()


@allure.feature('Registration page')
@allure.story('Registration button click')
@pytest.mark.parametrize('email', [test_data.EMAIL])
def test_register_button_click(driver, check_existence_and_delete_email, email):
    registration_page = RegistrationPage(
        driver, email, test_data.USERNAME, test_data.PASSWORD, test_data.PASSWORD
    )
    registration_page.open()
    registration_page.enter_email()
    registration_page.enter_login()
    registration_page.enter_password()
    registration_page.enter_confirm_password()
    registration_page.register_button_click()
    assert registration_page.pop_up_window_is_displayed()


@allure.feature('Registration page')
@allure.story('Have account?')
def test_have_account_text_is_displayed(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open()
    assert registration_page.have_account_text_is_displayed()


@allure.feature('Registration page')
@allure.story('Have account?')
def test_check_have_account_text(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open()
    assert registration_page.have_account_text()


@allure.feature('Registration page')
@allure.story('Login link')
def test_login_link_is_displayed(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open()
    assert registration_page.login_field_is_displayed()


@allure.feature('Registration page')
@allure.story('Login link')
def test_login_link_text(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open()
    assert registration_page.login_field_text()


@allure.feature('Registration page')
@allure.story('Login link')
def test_login_link_click(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open()
    registration_page.login_link_click()
    assert registration_page.login_link_url()


@allure.feature('Registration page')
@allure.story('Questions left?')
def test_questions_left_text_is_displayed(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open()
    assert registration_page.questions_left_text_is_displayed()


@allure.feature('Registration page')
@allure.story('Questions left?')
def test_check_questions_left_text(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open()
    assert registration_page.questions_left_text()


@allure.feature('Registration page')
@allure.story('Ask us!')
def test_ask_us_link_is_displayed(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open()
    assert registration_page.ask_us_link_is_displayed()


@allure.feature('Registration page')
@allure.story('Ask us!')
def test_ask_us_link_text(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open()
    assert registration_page.ask_ua_link_text()


@allure.feature('Registration page')
@allure.story('Ask us!')
@pytest.mark.skip('not implemented')
def test_ask_us_link_click(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open()
    registration_page.ask_us_link_click()
    assert driver.current_url == ''


@allure.feature('Registration page')
@allure.story('Data processing conditions')
def test_data_processing_conditions_is_displayed(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open()
    assert registration_page.data_processing_conditions_is_displayed()


@allure.feature('Registration page')
@allure.story('Data processing conditions')
def test_data_processing_conditions_text(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open()
    assert registration_page.data_processing_conditions_text()


@allure.feature('Registration page')
@allure.story('Input email field 257 characters')
@pytest.mark.parametrize('email', [test_data.EMAIL_257_CHARACTERS])
def test_check_input_email_field_257_characters(driver, email, check_existence_and_delete_email):
    registration_page = RegistrationPage(
        driver, email, test_data.USERNAME, test_data.PASSWORD, test_data.PASSWORD
    )
    registration_page.open()
    registration_page.enter_email()
    registration_page.enter_login()
    registration_page.enter_password()
    registration_page.enter_confirm_password()
    registration_page.register_button_click()
    assert registration_page.pop_up_window_is_displayed()
    assert registration_page.pop_up_email_long_line_text()


@allure.feature('Registration page')
@allure.story('Email field error massege')
def test_registration_with_empty_email_field_has_error_message_is_displayed(driver):
    registration_page = RegistrationPage(
        driver, test_data.EMPTY_FIELD, test_data.USERNAME, test_data.PASSWORD, test_data.PASSWORD
    )
    registration_page.open()
    registration_page.enter_login()
    registration_page.enter_password()
    registration_page.enter_confirm_password()
    registration_page.register_button_click()
    assert registration_page.email_field_error_massage_is_displayed()


@allure.feature('Registration page')
@allure.story('Email field error massage')
def test_registration_with_empty_email_field_has_error_message_text(driver):
    registration_page = RegistrationPage(
        driver, test_data.EMPTY_FIELD, test_data.USERNAME, test_data.PASSWORD, test_data.PASSWORD
    )
    registration_page.open()
    registration_page.enter_login()
    registration_page.enter_password()
    registration_page.enter_confirm_password()
    registration_page.register_button_click()
    assert registration_page.error_message_email_field_empty()


@allure.feature('Registration page')
@allure.story('Email field error massage')
def test_error_massage_is_displayed_if_enter_wrong_format_email(driver):
    registration_page = RegistrationPage(
        driver, test_data.INVALID_EMAIL, test_data.USERNAME, test_data.PASSWORD, test_data.PASSWORD
    )
    registration_page.open()
    registration_page.enter_email()
    registration_page.enter_login()
    registration_page.enter_password()
    registration_page.enter_confirm_password()
    registration_page.register_button_click()
    assert registration_page.email_field_error_massage_is_displayed()


@allure.feature('Registration page')
@allure.story('Email field error massage')
def test_error_massage_text_if_enter_wrong_format_email(driver):
    registration_page = RegistrationPage(
        driver, test_data.INVALID_EMAIL, test_data.USERNAME, test_data.PASSWORD, test_data.PASSWORD
    )
    registration_page.open()
    registration_page.enter_email()
    registration_page.enter_login()
    registration_page.enter_password()
    registration_page.enter_confirm_password()
    registration_page.register_button_click()
    assert registration_page.error_message_email_field_wrong_format()


@allure.feature('Registration page')
@allure.story('Login field error massage')
def test_registration_with_empty_login_field_error_message_is_displayed(driver):
    registration_page = RegistrationPage(
        driver, test_data.EMAIL, test_data.EMPTY_FIELD, test_data.PASSWORD, test_data.PASSWORD
    )
    registration_page.open()
    registration_page.open()
    registration_page.enter_email()
    registration_page.enter_login()
    registration_page.enter_password()
    registration_page.enter_confirm_password()
    registration_page.register_button_click()
    assert registration_page.login_field_error_message_is_displayed()


@allure.feature('Registration page')
@allure.story('Login field error massage')
def test_registration_with_empty_login_field_error_message_text(driver):
    registration_page = RegistrationPage(
        driver, test_data.EMAIL, test_data.EMPTY_FIELD, test_data.PASSWORD, test_data.PASSWORD
    )
    registration_page.open()
    registration_page.open()
    registration_page.enter_email()
    registration_page.enter_login()
    registration_page.enter_password()
    registration_page.enter_confirm_password()
    registration_page.register_button_click()
    assert registration_page.error_message_login_field_empty()


@allure.feature('Registration page')
@allure.story('Login field error massage')
def test_registration_with_empty_password_field_error_message_is_displayed(driver):
    registration_page = RegistrationPage(
        driver, test_data.EMAIL, test_data.USERNAME, test_data.EMPTY_FIELD, test_data.EMPTY_FIELD
    )
    registration_page.open()
    registration_page.open()
    registration_page.enter_email()
    registration_page.enter_login()
    registration_page.enter_password()
    registration_page.enter_confirm_password()
    registration_page.register_button_click()
    assert registration_page.password_field_error_message_is_displayed()


@allure.feature('Registration page')
@allure.story('Password field error massage')
def test_registration_with_empty_password_field_error_message_text(driver):
    registration_page = RegistrationPage(
        driver, test_data.EMAIL, test_data.USERNAME, test_data.EMPTY_FIELD, test_data.EMPTY_FIELD
    )
    registration_page.open()
    registration_page.open()
    registration_page.enter_email()
    registration_page.enter_login()
    registration_page.enter_password()
    registration_page.enter_confirm_password()
    registration_page.register_button_click()
    assert registration_page.text_error_message_password_field_empty()


@allure.feature('Registration page')
@allure.story('Password field error massage')
def test_registration_a_hint_on_how_to_create_password_is_displayed(driver):
    registration_page = RegistrationPage(
        driver, test_data.EMAIL, test_data.USERNAME,
        test_data.NON_FULL_PASSWORD, test_data.NON_FULL_PASSWORD
    )
    registration_page.open()
    registration_page.open()
    registration_page.enter_email()
    registration_page.enter_login()
    registration_page.enter_password()
    registration_page.enter_confirm_password()
    registration_page.register_button_click()
    assert registration_page.hint_on_how_to_create_password_is_displayed()


@allure.feature('Registration page')
@allure.story('Password field error massage')
def test_registration_a_hint_on_how_to_create_password_text(driver):
    registration_page = RegistrationPage(
        driver, test_data.EMAIL, test_data.USERNAME,
        test_data.NON_FULL_PASSWORD, test_data.NON_FULL_PASSWORD
    )
    registration_page.open()
    registration_page.open()
    registration_page.enter_email()
    registration_page.enter_login()
    registration_page.enter_password()
    registration_page.enter_confirm_password()
    registration_page.register_button_click()
    assert registration_page.hint_on_how_to_create_password_text()


@allure.feature('Registration page')
@allure.story('Confirm password field error massage')
def test_registration_with_empty_confirm_password_field_error_message_is_displayed(driver):
    registration_page = RegistrationPage(
        driver, test_data.EMAIL, test_data.USERNAME, test_data.PASSWORD, test_data.EMPTY_FIELD
    )
    registration_page.open()
    registration_page.open()
    registration_page.enter_email()
    registration_page.enter_login()
    registration_page.enter_password()
    registration_page.enter_confirm_password()
    registration_page.register_button_click()
    assert registration_page.empty_confirm_password_error_massage_is_displayed()


@allure.feature('Registration page')
@allure.story('Confirm password field error massage')
def test_registration_with_empty_confirm_password_field_error_message_text(driver):
    registration_page = RegistrationPage(
        driver, test_data.EMAIL, test_data.USERNAME, test_data.PASSWORD, test_data.EMPTY_FIELD
    )
    registration_page.open()
    registration_page.open()
    registration_page.enter_email()
    registration_page.enter_login()
    registration_page.enter_password()
    registration_page.enter_confirm_password()
    registration_page.register_button_click()
    assert registration_page.empty_confirm_password_error_massage_text()


@allure.feature('Registration page')
@allure.story('Confirm password field error massage')
def test_error_message_is_displayed_in_confirm_password_if_password_will_not_match(driver):
    registration_page = RegistrationPage(
        driver, test_data.EMAIL, test_data.USERNAME, test_data.PASSWORD, test_data.NON_FULL_PASSWORD
    )
    registration_page.open()
    registration_page.open()
    registration_page.enter_email()
    registration_page.enter_login()
    registration_page.enter_password()
    registration_page.enter_confirm_password()
    registration_page.register_button_click()
    assert registration_page.error_massage_password_not_match_is_displayed()


@allure.feature('Registration page')
@allure.story('Confirm password field error massage')
def test_error_message_text_in_confirm_password_if_password_will_not_match(driver):
    registration_page = RegistrationPage(
        driver, test_data.EMAIL, test_data.USERNAME, test_data.PASSWORD, test_data.NON_FULL_PASSWORD
    )
    registration_page.open()
    registration_page.enter_email()
    registration_page.enter_login()
    registration_page.enter_password()
    registration_page.enter_confirm_password()
    registration_page.register_button_click()
    assert registration_page.error_massage_password_not_match_text()


@allure.feature('Registration page')
@allure.story('Registration with valid email')
@pytest.mark.parametrize('email', test_data.VALID_EMAILS)
def test_registration_with_valid_email(
        driver, email, check_existence_and_delete_email
):
    registration_page = RegistrationPage(
        driver, email, test_data.USERNAME, test_data.PASSWORD, test_data.PASSWORD
    )
    registration_page.open()
    registration_page.enter_email()
    registration_page.enter_login()
    registration_page.enter_password()
    registration_page.enter_confirm_password()
    registration_page.register_button_click()
    assert registration_page.pop_up_window_is_displayed()
    assert registration_page.pop_up_window_text_letter_sent()


@allure.feature('Registration page')
@allure.story('Registration with invalid email')
@pytest.mark.parametrize('email', test_data.INVALID_EMAILS)
def test_registration_with_invalid_email(
        driver, email, check_existence_and_delete_email
):
    registration_page = RegistrationPage(
        driver, email, test_data.USERNAME, test_data.PASSWORD, test_data.PASSWORD
    )
    registration_page.open()
    registration_page.enter_email()
    registration_page.enter_login()
    registration_page.enter_password()
    registration_page.enter_confirm_password()
    registration_page.register_button_click()
    assert registration_page.email_field_error_massage_is_displayed()


@allure.feature('Registration page')
@allure.story('Registration with valid password')
@pytest.mark.parametrize('email', [test_data.EMAIL])
@pytest.mark.parametrize('password', test_data.VALID_PASSWORD)
def test_registration_with_valid_password(
        driver, password, check_existence_and_delete_email, email
):
    registration_page = RegistrationPage(driver, email, test_data.USERNAME, password, password)
    registration_page.open()
    registration_page.enter_email()
    registration_page.enter_login()
    registration_page.enter_password()
    registration_page.enter_confirm_password()
    registration_page.register_button_click()
    assert registration_page.pop_up_window_is_displayed()


@allure.feature('Registration page')
@allure.story('Registration with invalid password')
@pytest.mark.parametrize('email', [test_data.EMAIL])
@pytest.mark.parametrize('password', test_data.INVALID_PASSWORD)
def test_registration_with_invalid_password(
        driver, password, check_existence_and_delete_email, email
):
    registration_page = RegistrationPage(driver, email, test_data.USERNAME, password, password)
    registration_page.open()
    registration_page.enter_email()
    registration_page.enter_login()
    registration_page.enter_password()
    registration_page.enter_confirm_password()
    registration_page.register_button_click()
    assert registration_page.password_field_error_message_is_displayed()


@allure.feature('Registration page')
@allure.story('Input password field 257 characters')
@pytest.mark.parametrize('email', [test_data.EMAIL])
@pytest.mark.parametrize('password', [test_data.PASSWORD_257_CHARACTERS])
def test_check_input_password_field_257_characters(
        driver, password, check_existence_and_delete_email, email
):
    registration_page = RegistrationPage(
        driver, email, test_data.USERNAME, password, password
    )
    registration_page.open()
    registration_page.enter_email()
    registration_page.enter_login()
    registration_page.enter_password()
    registration_page.enter_confirm_password()
    registration_page.register_button_click()
    assert registration_page.pop_up_window_is_displayed()
    assert registration_page.pop_up_password_long_line_text()


@allure.feature('Registration page')
@allure.story('Registration with existing user')
@pytest.mark.parametrize('email', [test_data.EMAIL])
def test_registration_with_existing_user(driver, check_existence_and_delete_email, email):
    registration_page = RegistrationPage(
        driver, email, test_data.USERNAME, test_data.PASSWORD, test_data.PASSWORD
    )
    registration_page.create_new_user()
    registration_page.open()
    registration_page.enter_email()
    registration_page.enter_login()
    registration_page.enter_password()
    registration_page.enter_confirm_password()
    registration_page.register_button_click()
    assert registration_page.pop_up_window_is_displayed()
    assert registration_page.pop_up_window_existing_user_text()
