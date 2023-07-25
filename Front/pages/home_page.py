from Front.pages.base_page import BasePage
from Front.pages.locators import home_page_locators as hpl
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep  #DELETE


class HomePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_page(self):
        self.browser.get(self.base_url)

    def logo(self):
        return self.find_element(hpl.train_lab_logo)

    def o_nas_button(self):
        but_area = self.find_element(hpl.o_nas_bar)
        o_nas_but = but_area.find_element(By.CLASS_NAME, 'btn-secondary')
        return o_nas_but

    def o_nas_button_text(self):
        but_list = self.find_element(hpl.o_nas_bar)
        o_nas_but = but_list.find_element(By.CLASS_NAME, 'btn-secondary')
        return o_nas_but.text

    def tasks_button(self):
        tasks_but = self.find_element(hpl.tasks_but)
        return tasks_but

    def tasks_button_text(self):
        tasks_but = self.find_element(hpl.tasks_but)
        return tasks_but.text

    def sign_in_button(self):
        sign_in_but = self.find_element(hpl.sign_in_but)
        return sign_in_but

    def sign_in_button_text(self):
        sign_in_but = self.find_element(hpl.sign_in_but)
        return sign_in_but.text
