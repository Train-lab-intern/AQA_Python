import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Options_chrome
from selenium.webdriver.firefox.options import Options as Options_ff


@pytest.fixture(scope='function')
def driver(browser_options, host_options):
    if browser_options == 'ff' and host_options == 'server':
        with allure.step(f'Rune Firefox and {host_options}'):
            options = Options_ff()
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920x1080")
            driver_browser = webdriver.Firefox(options=options)

    elif browser_options == 'ff':
        with allure.step('Rune Firefox'):
            driver_browser = webdriver.Firefox()
            driver_browser.maximize_window()

    elif host_options == 'server':
        with allure.step(f'Rune Chrome with {host_options}'):
            options = Options_chrome()
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920x1080")
            driver_browser = webdriver.Chrome(options=options)

    else:
        with allure.step('Rune Chrome'):
            driver_browser = webdriver.Chrome()
            driver_browser.maximize_window()
    driver_browser.implicitly_wait(10)
    yield driver_browser
    driver_browser.quit()


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        action='store',
        default='chrome',
        help='Укажите значение браузера, поумолчанию Chrome'
    )
    parser.addoption(
        '--host',
        action='store',
        default='ui',
        help='Укажите варивнт запуска браузера, по умолчанию UI'
    )


@pytest.fixture(scope='session')
def browser_options(request):
    return request.config.getoption('--browser')


@pytest.fixture(scope='session')
def host_options(request):
    return request.config.getoption('--host')
