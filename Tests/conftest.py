import pytest
from selenium import webdriver
#from selenium.common.remote.webdriver import webdriver

@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.maximize_window()
    chrome_browser.implicitly_wait(10)
    return chrome_browser