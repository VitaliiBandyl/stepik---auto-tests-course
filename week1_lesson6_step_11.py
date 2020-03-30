from selenium import webdriver
import time

# Создаем словарь в котором ключем будет название обязательного поля,
# а значением кортеж с сss-селектора и текста которое мы запишем в это поле
required_fields = {
    "First Name": (".first:required", "Ivan"),
    "Last Name": (".second:required","Petrov"),
    "Email": (".third:required", "IvanPetrov@stepik.org")
}

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Проходимся циклом по всем элементам словаря
    for key, value in required_fields.items():
        select = browser.find_element_by_tag_name(value[0])
        select.send_keys(value[1])

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
