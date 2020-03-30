from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    a = browser.find_element_by_css_selector('#num1').text
    b = browser.find_element_by_css_selector('#num2').text
    select = Select(browser.find_element_by_css_selector('.custom-select'))
    select.select_by_value(str(int(a) + int(b)))
    submit = browser.find_element_by_css_selector('[type="submit"]')
    submit.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
