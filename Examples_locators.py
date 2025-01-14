from selenium import webdriver
from selenium.webdriver.common.by import By

"""Чтобы открыть браузер и сохранить в переменную, Firefox/Opera"""
browser = webdriver.Chrome
browser.get("https://dev.fp.big3.ru/")

"""Поиск по ID"""
button = browser.find_element(By.ID, "")
button.click()
"""Поиск по имени класса. Пробел в имени класса значит то, что можно использовать один из них"""
button_2 = browser.find_element(By.CLASS_NAME, "")

"""Поиск по тексту ссылки"""
"""Если не работает, есть такое решение: browser.execute_script("arguments[0].click();", link) ИЛИ browser.execute_script('window.scrollBy(0,document.body.scrollHeight)') """
link = browser.find_element(By.LINK_TEXT, "Contact").click()

"""Поиск по CSS селектору"""
button_3 = browser.find_element(By.CSS_SELECTOR, "input[class='btn btn-primary']")
button_3.click()

"""Поиск по XPath, // - значит, ищем во всем документе"""
button_4 = browser.find_element(By.XPATH, '//input[@class="btn btn-primary"]')