from selenium import webdriver
import chromedriver_autoinstaller
import pytest


@pytest.fixture(scope='function')
def browser():
    chromedriver_autoinstaller.install()
    chrome_browser = webdriver.Chrome()
    chrome_browser.maximize_window()
    chrome_browser.implicitly_wait(10)
    yield chrome_browser
    chrome_browser.quit()
