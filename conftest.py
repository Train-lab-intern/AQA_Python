from selenium import webdriver
import pytest


@pytest.fixture(scope='function')
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.maximize_window()
    chrome_browser.implicitly_wait(10)
    yield chrome_browser
    chrome_browser.quit()
