from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import home_page_locators as hpl


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_page(self):
        self.driver.get(self.base_url)

    def logo(self):
        return self.find_element(hpl.train_lab_logo)

    def o_nas_button(self):
        but_area = self.find_element(hpl.o_nas_bar)
        return but_area.find_element(By.CSS_SELECTOR, '.btn.btn-secondary')

    def o_nas_button_text(self):
        but_list = self.find_element(hpl.o_nas_bar)
        return but_list.find_element(By.CSS_SELECTOR, '.btn.btn-secondary').text

    def tasks_button(self):
        return self.find_element(hpl.tasks_but)

    def tasks_button_text(self):
        return self.find_element(hpl.tasks_but).text

    def sign_in_button(self):
        return self.find_element(hpl.sign_in_but)

    def sign_in_button_text(self):
        return self.find_element(hpl.sign_in_but).text

    def success_banner_text(self):
        self.wait_element(hpl.success_banner_bar)
        return self.find_element(hpl.success_banner_bar).text

    def our_simulators_banner_text(self):
        self.wait_element(hpl.our_simulators_banner)
        return self.find_element(hpl.our_simulators_banner).text
