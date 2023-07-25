from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.base_url = 'https://front-test-a2ykv.ondigitalocean.app/'

    def find_element(self, args: tuple):
        by_name, by_val = args
        return self.browser.find_element(by_name, by_val)

    def find_elements(self, args: tuple):
        by_name, by_val = args
        return self.browser.find_elements(by_name, by_val)


