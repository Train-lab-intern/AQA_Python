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


def test_success_banner_text_is_ok(browser):
    home_page = HomePage(browser)
    home_page.open_page()
    assert home_page.success_banner_text() == 'Создай свой успех'


def test_success_banner_text_takes_from_bd(browser):
    home_page = HomePage(browser)
    home_page.open_page()
    assert home_page.success_banner_text_takes_from_bd() is True


def test_our_simulators_banner_text_is_ok(browser):
    home_page = HomePage(browser)
    home_page.open_page()
    assert home_page.our_simulators_banner_text() == 'Наши тренажеры' \
             ' разработаны на основе тестовых заданий работодателей. ' \
             'выполняя задания и зарабатывая баллы, ты найдешь работу мечты'


def test_our_simulators_banner_text_takes_from_bd(browser):
    home_page = HomePage(browser)
    home_page.open_page()
    assert home_page.our_simulators_banner_text_takes_from_bd() is True
