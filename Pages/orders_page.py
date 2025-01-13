from selenium.webdriver.common.by import By
from Pages.base_page import BasePage

INPUT_LOGIN = (By.XPATH, '/html/body/big3-app-root/ng-scrollbar/div/div/div/div/ng-component/div/div[1]/div/div/ng-component/div/ng-component/div/form/div[1]/div[1]/label/input')
INPUT_PASSWORD = (By.XPATH, "/html/body/big3-app-root/ng-scrollbar/div/div/div/div/ng-component/div/div[1]/div/div/ng-component/div/ng-component/div/form/div[1]/div[2]/label/input")
BUTTON_SUBMIT = (By.XPATH, '/html/body/big3-app-root/ng-scrollbar/div/div/div/div/ng-component/div/div[1]/div/div/ng-component/div/ng-component/div/form/div[2]/button')
MENU_ORDERS = (By.XPATH, '//*[@id="sidebar"]/div/nav/ul/li[2]/a/span')
TITLE_ORDER = (By.CSS_SELECTOR, '.heading.heading_h1.ng-tns-c458-1')

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

