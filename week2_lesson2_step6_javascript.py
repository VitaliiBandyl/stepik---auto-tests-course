from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    input_value = browser.find_element_by_css_selector("#input_value").text
    answer = calc(input_value)
    answer_field = browser.find_element_by_css_selector("#answer")
    answer_field.send_keys(answer)
    submit = browser.find_element_by_css_selector('[type="submit"]')              # JavaScript
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)   # JavaScript scroll to element
    checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    checkbox.click()
    radio_button = browser.find_element_by_css_selector("#robotsRule")
    radio_button.click()
    submit.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
