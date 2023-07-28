from Front.pages.base_page import BasePage
from Front.pages.locators import home_page_locators as hpl
from selenium.webdriver.common.by import By
from Front.bd_creds import take_text_by_front_id_from_db as bd_creds


class HomePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_page(self):
        self.browser.get(self.base_url)

    def logo(self):
        return self.find_element(hpl.train_lab_logo)

    def o_nas_button(self):
        but_area = self.find_element(hpl.o_nas_bar)
        return but_area.find_element(By.CLASS_NAME, 'btn-secondary')

    def o_nas_button_text(self):
        but_list = self.find_element(hpl.o_nas_bar)
        return but_list.find_element(By.CLASS_NAME, 'btn-secondary').text

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

    def success_banner_text_takes_from_bd(self):
        self.wait_element(hpl.success_banner_bar)
        success_ban = self.find_element(hpl.success_banner_bar).text
        if success_ban == bd_creds(1.1):
            return True
        else:
            return False

    def our_simulators_banner_text(self):
        self.wait_element(hpl.our_simulators_banner)
        return self.find_element(hpl.our_simulators_banner).text

    def our_simulators_banner_text_takes_from_bd(self):
        self.wait_element(hpl.our_simulators_banner)
        simulators_ban = self.find_element(hpl.our_simulators_banner).text
        if simulators_ban == bd_creds(1.2):
            return True
        else:
            return False

