import pytest
import allure
import psycopg2
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Options_chrome
from selenium.webdriver.firefox.options import Options as Options_ff
import database_connection


@pytest.fixture(scope='function')
def check_existence_and_delete_email(connect_db, email):
    curs = connect_db.cursor()
    email = email.lower()
    curs.execute(f"select email from users where email = '{email}';")
    user = curs.fetchall()
    if user != '':
        curs.execute(f"delete from users where email = '{email}';")
        connect_db.commit()
    yield
    curs = connect_db.cursor()
    curs.execute(f"delete from users where email = '{email}';")
    connect_db.commit()


@pytest.fixture(scope='function')
def driver(browser_options, host_options):
    if browser_options == 'ff' and host_options == 'server':
        with allure.step(f'Run Firefox and {host_options}'):
            options = Options_ff()
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920x1080")
            driver_browser = webdriver.Firefox(options=options)

    elif browser_options == 'ff':
        with allure.step('Run Firefox'):
            driver_browser = webdriver.Firefox()
            driver_browser.maximize_window()

    elif host_options == 'server':
        with allure.step(f'Run Chrome with {host_options}'):
            options = Options_chrome()
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920x1080")
            driver_browser = webdriver.Chrome(options=options)

    else:
        with allure.step('Run Chrome'):
            driver_browser = webdriver.Chrome()
            driver_browser.maximize_window()
    driver_browser.implicitly_wait(10)
    yield driver_browser
    driver_browser.quit()


@pytest.fixture(scope='function')
def connect_db():
    with allure.step('Run a database connection'):
        con = psycopg2.connect(
            host=database_connection.host,
            port=database_connection.port,
            user=database_connection.username,
            password=database_connection.password,
            database=database_connection.database
        )
        yield con
        con.close()


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
        default='localhost',
        help='Укажите варивнт запуска тестов с хоста, по умолчанию localhost.'
    )


@pytest.fixture(scope='session')
def browser_options(request):
    return request.config.getoption('--browser')


@pytest.fixture(scope='session')
def host_options(request):
    return request.config.getoption('--host')
