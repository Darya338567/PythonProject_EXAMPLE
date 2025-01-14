from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

"""Для работы с выпадающими списками импортируется модуль Select"""
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get("url")

vars = browser.find_elements(By.CLASS_NAME, "")
first_var = vars[0]
vars = browser.find_elements(By.CLASS_NAME, "")[0]

"""Прописываем явное ожидание (по элементу, который загрузился последним, ищем его по тагнейму и текту элементв)"""
WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element(By.TAG_NAME,",body"), "text")
print(first_var.text)
print(first_var.get_attribute("href"))
sorter = browser.find_element(By.XPATH,"")
select = Select(sorter)
select.select_by_value("price")

"""При получении ошибки .StaleElementReferenseExeptions нужно перезаписать поиск элемента при перезагрузке страницы, НО правильно прописать исчезновение прошлой связи:"""
WebDriverWait(browser, 10).until((EC.staleness_of(first_var)))