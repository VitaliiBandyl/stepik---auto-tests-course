from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    start = browser.find_element_by_css_selector('[type="submit"]').click()

    new_window = browser.window_handles[1]
    current_window = browser.window_handles[0]
    browser.switch_to_window(new_window)

    input_value = browser.find_element_by_css_selector("#input_value").text

    answer = calc(input_value)
    answer_field = browser.find_element_by_css_selector("#answer")
    answer_field.send_keys(answer)

    submit = browser.find_element_by_css_selector('[type="submit"]')
    submit.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
