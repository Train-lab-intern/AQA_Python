from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver, link=None):
        self.driver = driver
        self.link = link

    def open(self):
        self.driver.get(self.link)

    def hover_over_element(self, locator):
        element = self.driver.find_element(*locator)
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def is_element_clickable_after_hover(self, locator, timeout=5):
        self.hover_over_element(locator)
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def find_element_and_click(self, locator):
        self.driver.find_element(*locator).click()

    def assert_current_url(self, expected_url):
        current_url = self.driver.current_url
        assert current_url == expected_url, f"URL does not match. Actual page is: {current_url}"
