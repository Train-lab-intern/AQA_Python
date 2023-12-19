import pytest
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from data.urls import MAIN_PAGE, MAIN_PAGE_TEST


# Header tests
def test_check_logo_visibility(driver):
    page = MainPage(driver, MAIN_PAGE_TEST)
    page.open()
    page.logo_visibility()


@pytest.mark.parametrize('button', MainPageLocators.HEADER_BUTTONS)
def test_check_header_buttons_clickability(driver, button):
    page = MainPage(driver, MAIN_PAGE)
    page.open()
    page.check_element_clickability(button)

# Footer tests
@pytest.mark.xfail
def test_linkedin_redirection(driver):
    page = MainPage(driver, MAIN_PAGE)
    page.open()
    page.check_linkedin_redirection()


def test_github_redirection(driver):
    page = MainPage(driver, MAIN_PAGE)
    page.open()
    page.check_github_redirection()
