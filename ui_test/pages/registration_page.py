import allure
from ui_test import text
from ui_test.pages.base_page import BasePage
from ui_test.pages.locators import registration_page_locators as loc



class RegistrationPage(BasePage):
    def __init__(
            self, driver=None, email=None, username=None, password=None, confirm_password=None
    ):
        super().__init__(driver)
        self.driver = driver
        self.email = email
        self.username = username
        self.password = password
        self.confirm_password = confirm_password
        self.response = None

    def open(self):
        with allure.step('Open registration page'):
            self.driver.get('https://front-test-a2ykv.ondigitalocean.app/registration')

    def current_url(self):
        with allure.step('Check url'):
            return self.driver.current_url == ('https://front-test-a2ykv.ondigitalocean.'
                                               'app/registration')

    def check_url_home_page(self):
        with allure.step('Check home page url'):
            return self.driver.current_url == 'https://front-test-a2ykv.ondigitalocean.app/'

    def logo_site(self):
        return self.find_element(loc.logo)

    def logo_is_displayed(self):
        with allure.step('Website logo displayed'):
            return self.logo_site().is_displayed()

    def click_logo_site(self):
        with allure.step('Click website logo'):
            return self.logo_site().click()

    def welcome_text_is_displayed(self):
        with allure.step('Check welcome text displayed'):
            return self.find_element(loc.welcome_text).is_displayed()

    def check_welcome_text(self):
        with allure.step('Check welcome text'):
            return self.find_element(loc.welcome_text).text == 'Мы рады видеть вас'

    def email_field(self):
        return self.find_element(loc.email_field)

    def email_field_is_displayed(self):
        with allure.step('Email field displayed'):
            return self.email_field().is_displayed()

    def email_field_text(self):
        with allure.step('Email field text'):
            return self.email_field().get_attribute('placeholder') == 'Почта'

    def login_field(self):
        return self.find_element(loc.login_field)

    def login_field_is_displayed(self):
        with allure.step('Login field displayed'):
            return self.login_field().is_displayed()

    def login_field_text(self):
        with allure.step('Login field text'):
            return self.login_field().get_attribute('placeholder') == 'Логин'

    def password_field(self):
        return self.find_element(loc.password_field)

    def password_field_is_displayed(self):
        with allure.step('Password field displayed'):
            return self.password_field().is_displayed()

    def password_field_text(self):
        with allure.step('Password field text'):
            return self.password_field().get_attribute('placeholder') == 'Пароль'

    def password_view_icon(self):
        return self.find_elements(loc.password_view_icon)[0]

    def password_view_icon_is_displayed(self):
        with allure.step('Password view icon displayed'):
            return self.password_view_icon().is_displayed()

    def password_view_icon_click(self):
        with allure.step('Password view icon click'):
            return self.password_view_icon().click()

    def type_password_field(self):
        with allure.step('Check type password field'):
            return self.password_field().get_attribute('type') == 'text'

    def confirm_password_field(self):
        return self.find_element(loc.confirm_password_field)

    def confirm_password_field_is_displayed(self):
        with allure.step('Confirm password field displayed'):
            return self.confirm_password_field().is_displayed()

    def confirm_password_field_text(self):
        with allure.step('Confirm password field text'):
            return self.confirm_password_field().get_attribute('placeholder') == 'Пароль'

    def confirm_password_view_icon(self):
        return self.find_elements(loc.password_view_icon)[1]

    def confirm_password_view_icon_is_displayed(self):
        with allure.step('Confirm password view icon displayed'):
            return self.confirm_password_view_icon().is_displayed()

    def confirm_password_view_icon_click(self):
        with allure.step('Confirm password view icon click'):
            return self.confirm_password_view_icon().click()

    def type_confirm_password_field(self):
        with allure.step('Check type password field'):
            return self.confirm_password_field().get_attribute('type') == 'text'

    def have_account_text_is_displayed(self):
        with allure.step('Text: have account displayed'):
            return self.find_elements(loc.text_questions)[0].is_displayed()

    def have_account_text(self):
        with allure.step('Check have account text'):
            return self.find_elements(loc.text_questions)[0].text == 'Есть аккаунт?'

    def login_link(self):
        return self.find_element(loc.login_link)

    def login_link_is_displayed(self):
        with allure.step('Check login link displayed'):
            return self.login_link().is_displayed()

    def login_link_text(self):
        with allure.step('Check login link displayed'):
            return self.login_link().text == 'Войти!'

    def login_link_click(self):
        with allure.step('Login link click'):
            return self.login_link().click()

    def login_link_url(self):
        with allure.step('Check login link'):
            return self.driver.current_url == 'https://front-test-a2ykv.ondigitalocean.app/auth'

    def questions_left_text_is_displayed(self):
        with allure.step('Text: questions left displayed'):
            return self.find_elements(loc.text_questions)[1].is_displayed()

    def questions_left_text(self):
        with allure.step('Check questions left text'):
            return self.find_elements(loc.text_questions)[1].text == 'Остались вопросы?'

    def ask_us_link(self):
        return self.find_element(loc.ask_us_link)

    def ask_us_link_is_displayed(self):
        with allure.step('Check ask us link displayed'):
            return self.ask_us_link().is_displayed()

    def ask_ua_link_text(self):
        with allure.step('Check ask us text'):
            return self.ask_us_link().text == 'Спроси нас!'

    def ask_us_link_click(self):
        with allure.step('Ask us link click'):
            return self.ask_us_link().click()

    def data_processing_conditions_is_displayed(self):
        with allure.step('Data processing conditions displayed'):
            return self.find_element(loc.data_processing_conditions).is_displayed()

    def data_processing_conditions_text(self):
        with allure.step('Check data processing conditions text'):
            return self.find_element(
                loc.data_processing_conditions
            ).text == (
                'Нажимая кнопку «Зарегистрироваться», вы подтверждаете своё согласие'
                ' с условиями обработки данных.'
            )

    def len_email_field(self):
        with allure.step('Check len email field'):
            return len(self.email_field().get_attribute('value'))

    def register_button(self):
        return self.find_element(loc.register_button)

    def register_button_is_displayed(self):
        with allure.step('Check register button displayed'):
            return self.register_button().is_displayed()

    def register_button_text(self):
        with allure.step('Check register button text'):
            return self.register_button().text == 'Зарегистрироваться'

    def register_button_click(self):
        with allure.step('Check register button displayed'):
            return self.register_button().click()

    def email_field_error_massage(self):
        return self.find_elements(loc.message_field)[0]

    def email_field_error_massage_is_displayed(self):
        with allure.step('Check email field error massage displayed'):
            return self.email_field_error_massage().is_displayed()

    def error_message_email_field_empty(self):
        with allure.step('Check email field error massage text'):
            return self.email_field_error_massage().text == text.CM_7

    def error_message_email_field_wrong_format(self):
        with allure.step('Check email field error massage text'):
            return self.email_field_error_massage().text == text.CM_2

    def login_field_error_message(self):
        return self.find_elements(loc.message_field)[0]

    def login_field_error_message_is_displayed(self):
        with allure.step('Check email login error massage displayed'):
            return self.login_field_error_message().is_displayed()

    def error_message_login_field_empty(self):
        with allure.step('Check login field error massage text'):
            return self.login_field_error_message().text == text.CM_7

    def password_error_message(self):
        return self.find_elements(loc.message_field)[0]

    def password_field_error_message_is_displayed(self):
        with allure.step('Check password field error massage displayed'):
            return self.password_error_message().is_displayed()

    def text_error_message_password_field_empty(self):
        with allure.step('Check password field error massage text'):
            return self.password_error_message().text == text.CM_7

    def hint_on_how_to_create_password_is_displayed(self):
        with allure.step('Check how to create password massage displayed'):
            return self.password_error_message().is_displayed()

    def hint_on_how_to_create_password_text(self):
        with allure.step('Check how to create password massage text'):
            return self.password_error_message().text == text.CM_1

    def confirm_password_error_massage(self):
        return self.find_elements(loc.message_field)[0]

    def empty_confirm_password_error_massage_is_displayed(self):
        with allure.step('Check confirm password error massage displayed'):
            return self.confirm_password_error_massage().is_displayed()

    def empty_confirm_password_error_massage_text(self):
        with allure.step('Check confirm password error massage text'):
            return self.confirm_password_error_massage().text == text.CM_7

    def error_massage_password_not_match_is_displayed(self):
        with allure.step('Check password not match massage displayed'):
            return self.confirm_password_error_massage().is_displayed()

    def error_massage_password_not_match_text(self):
        with allure.step('Check massage password not match displayed'):
            return self.confirm_password_error_massage().text == text.CM_11

    def enter_email(self):
        with allure.step('Enter email'):
            return self.email_field().send_keys(self.email)

    def enter_login(self):
        with allure.step('Enter login'):
            return self.login_field().send_keys(self.username)

    def enter_password(self):
        with allure.step('Enter password'):
            return self.password_field().send_keys(self.password)

    def enter_confirm_password(self):
        with allure.step('Enter confirm password'):
            return self.confirm_password_field().send_keys(self.confirm_password)

    def pop_up_window(self):
        return self.find_element(loc.pop_up_window)

    def pop_up_window_is_displayed(self):
        with allure.step('Check pop up window displayed'):
            return self.find_element(loc.pop_up_window).is_displayed()

    def pop_up_window_text_letter_sent(self):
        with allure.step('Check pop up window text'):
            return self.pop_up_window().text == text.CM_4

    def pop_up_window_existing_user_text(self):
        with allure.step('Check pop up window text'):
            return self.pop_up_window().text == text.CM_3

    def pop_up_email_long_line_text(self):
        with allure.step('Check pop up window text'):
            return self.pop_up_window().text == text.MESSAGE_LONG_EMAIL

    def pop_up_password_long_line_text(self):
        with allure.step('Check pop up window text'):
            return self.pop_up_window().text == text.MESSAGE_LONG_PASSWORD

    def create_new_user(self):
        with allure.step('Send request to create user'):
            self.response = self.post_request_create_user(
                self.email, self.username, self.password
            )
            return self.response
