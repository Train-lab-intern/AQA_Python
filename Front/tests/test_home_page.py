from Front.pages.home_page import HomePage
from Front.conftest import browser


def test_trainlab_logo_is_displayed(browser):
    home_page = HomePage(browser)
    home_page.open_page()
    assert home_page.logo().is_displayed()


def test_o_nas_button_is_displayed(browser):
    home_page = HomePage(browser)
    home_page.open_page()
    assert home_page.o_nas_button().is_displayed()


def test_o_nas_button_text_is_ok(browser):
    home_page = HomePage(browser)
    home_page.open_page()
    assert home_page.o_nas_button_text() == 'О нас'


def test_tasks_button_is_displayed(browser):
    home_page = HomePage(browser)
    home_page.open_page()
    assert home_page.tasks_button().is_displayed()


def test_tasks_button_text_is_ok(browser):
    home_page = HomePage(browser)
    home_page.open_page()
    assert home_page.tasks_button_text() == 'Задания'


def test_sign_in_button_is_displayed(browser):
    home_page = HomePage(browser)
    home_page.open_page()
    assert home_page.sign_in_button().is_displayed()


def test_sign_in_button_text_is_ok(browser):
    home_page = HomePage(browser)
    home_page.open_page()
    assert home_page.sign_in_button_text() == 'Войти'


