from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data.urls import LINKEDIN_PAGE, GITHUB_PAGE



class MainPage(BasePage):

    def logo_visibility(self):
        self.check_element_visibility(MainPageLocators.LOGO)

    def check_linkedin_redirection(self):
        self.find_element_and_click(MainPageLocators.LINKEDIN_LINK)
        self.assert_current_url(LINKEDIN_PAGE)

    def check_github_redirection(self):
        self.find_element_and_click(MainPageLocators.GITHUB_LINK)
        self.assert_current_url(GITHUB_PAGE)
