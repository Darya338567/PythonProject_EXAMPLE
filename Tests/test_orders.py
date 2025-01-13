import time
from Pages.orders_page import OrdersPage, TITLE_ORDER


def test_go_orders(browser):
    # создаем сессию работы со страницей авторизации
    page_order = OrdersPage(browser)
    page_order.open()
    page_order.auth()
    time.sleep(10)
    page_order.go_to_orders()
    time.sleep(10)
    assert browser.find_element(*TITLE_ORDER).text == "Закупки"






