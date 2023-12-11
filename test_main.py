import pytest
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


# Header tests
def test_is_logo_visible(driver):
    page = MainPage(driver)
    page.open_main_page()
    page.logo_visibility()


def test_about_us_clickable(driver):
    page = MainPage(driver)
    page.open_main_page()
    page.hover_over_element(MainPageLocators.ABOUT_US_BUTTON)
    page.is_element_clickable_after_hover(MainPageLocators.ABOUT_US_BUTTON)


def test_tasks_button_visible(driver):
    page = MainPage(driver)
    page.open_main_page()
    page.hover_over_element(MainPageLocators.TASKS_BUTTON)
    page.is_element_clickable_after_hover(MainPageLocators.ABOUT_US_BUTTON)


def test_enter_clickable(driver):
    page = MainPage(driver)
    page.open_main_page()
    page.hover_over_element(MainPageLocators.REG_BUTTON)
    page.is_element_clickable_after_hover(MainPageLocators.REG_BUTTON)


# Footer tests
@pytest.mark.xfail
def test_linkedin_redirection(driver):
    page = MainPage(driver)
    page.open_main_page()
    page.check_linkedin_redirection()

def test_github_redirection(driver):
    page = MainPage(driver)
    page.open_main_page()
    page.check_github_redirection()
