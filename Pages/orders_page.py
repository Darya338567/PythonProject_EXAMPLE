from selenium.webdriver.common.by import By
from Pages.base_page import BasePage

INPUT_LOGIN = (By.CSS_SELECTOR, "input[placeholder='Введите логин']")
INPUT_PASSWORD = (By.CSS_SELECTOR, "input[placeholder='Введите пароль']")
BUTTON_SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
MENU_ORDERS = (By.LINK_TEXT, "Закупки")
TITLE_ORDER = (By.CSS_SELECTOR, ".heading.heading_h1.ng-tns-c472-1")

class OrdersPage(BasePage):
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

    def go_to_orders(self):
        orders = self.browser.find_element(*MENU_ORDERS)
        orders.click()

    def title_orders(self):
        return self.find(*TITLE_ORDER)

