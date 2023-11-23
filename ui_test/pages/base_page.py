import json
import requests
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

BASE_URL = 'https://test.app.it-roast.com'
REGISTER_USER = '/api/v1/users/register'


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.base_url = BASE_URL
        self.register_user = REGISTER_USER

    def find_element(self, *args):
        element, value = args[0]
        return self.driver.find_element(element, value)

    def find_elements(self, *args):
        element, value = args[0]
        return self.driver.find_elements(element, value)

    def driver_wait(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.element_to_be_clickable(locator))

    def post_request_create_user(self, email, username, password):
        headers = {
            'Content-Type': 'application/json'
        }
        data = json.dumps({
            "username": f"{username}",
            "email": f"{email}",
            "password": f"{password}"
        })
        request = requests.request('POST', self.base_url + self.register_user, headers=headers,
                                   data=data, timeout=20)
        return request
