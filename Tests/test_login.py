from Pages.login_page import LoginPage, LOGO
import time


def test_login(browser):
    #создаем сессию работы со страницей авторизации
    page_login = LoginPage(browser)
    page_login.open()
    time.sleep(10)
    page_login.auth()
    time.sleep(10)

    assert browser.find_element(*LOGO).is_displayed()

