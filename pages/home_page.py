from pages.locators import home_page_locators as hpl
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def open_page(self):
        self.browser.get(self.base_url)

    def logo_is_displayed(self):
        return self.find_element(hpl.train_lab_logo).is_displayed()

    def about_us_button_is_displayed(self):
        return self.find_element(hpl.about_us_btn).is_displayed()

    def o_nas_button_text(self):
        return self.find_element(hpl.about_us_btn).text

    def tasks_button_is_displayed(self):
        return self.find_element(hpl.tasks_btn).is_displayed()

    def tasks_button_text(self):
        return self.find_element(hpl.tasks_btn).text

    def sign_in_button_is_displayed(self):
        return self.find_element(hpl.sign_in_btn).is_displayed()

    def sign_in_button_text(self):
        return self.find_element(hpl.sign_in_btn).text

    def success_banner_text(self):
        self.wait_element(hpl.success_banner_bar)
        return self.find_element(hpl.success_banner_bar).text

    def our_simulators_banner_text(self):
        self.wait_element(hpl.our_simulators_banner)
        return self.find_element(hpl.our_simulators_banner).text

    def start_the_journey_button_is_displayed(self):
        return self.find_element(hpl.start_the_journey_btn).is_displayed()

    def start_the_journey_button_text(self):
        return self.find_element(hpl.start_the_journey_btn).text

    def sql_banner_is_displayed(self):
        return self.find_element(hpl.sql_banner).is_displayed()

    def python_banner_is_displayed(self):
        return self.find_element(hpl.python_banner).is_displayed()

    def java_script_banner_is_displayed(self):
        return self.find_element(hpl.java_script_banner).is_displayed()
