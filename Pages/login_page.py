from selenium.webdriver.common.by import By
from Pages.base_page import BasePage

INPUT_LOGIN = (By.XPATH, '/html/body/big3-app-root/ng-scrollbar/div/div/div/div/ng-component/div/div[1]/div/div/ng-component/div/ng-component/div/form/div[1]/div[1]/label/input')
INPUT_PASSWORD = (By.XPATH, "/html/body/big3-app-root/ng-scrollbar/div/div/div/div/ng-component/div/div[1]/div/div/ng-component/div/ng-component/div/form/div[1]/div[2]/label/input")
BUTTON_SUBMIT = (By.XPATH, '/html/body/big3-app-root/ng-scrollbar/div/div/div/div/ng-component/div/div[1]/div/div/ng-component/div/ng-component/div/form/div[2]/button')
LOGO = (By.XPATH, '/html/body/big3-app-root/ng-scrollbar/div/div/div/div/ng-component/div/big3-navbar-v/div/div[1]/a/big3-logo/div/h2')

class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get("https://dev.fp.big3.ru/auth")

    def auth(self):
        login = self.browser.find_element(*INPUT_LOGIN)
        login.clear()
        login.send_keys("admin")
        password = self.browser.find_element(*INPUT_PASSWORD)
        password.clear()
        password.send_keys("?tP28#c2uK1rx'FeAFFO")
        submit = self.browser.find_element(*BUTTON_SUBMIT)
        submit.submit()

    def logo(self):
        return self.find(*LOGO)

