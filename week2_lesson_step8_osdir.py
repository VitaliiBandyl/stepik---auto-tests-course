from selenium import webdriver
import time
import os

# Создаем словарь в котором ключем будет название обязательного поля,
# а значением кортеж с сss-селектора и текста которое мы запишем в это поле
required_fields = {
    "First Name": ("[name=\"firstname\"]", "Ivan"),
    "Last Name": ("[name=\"lastname\"]", "Petrov"),
    "Email": ("[name=\"email\"]", "IvanPetrov@stepik.org")
}

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла

try:
    # Проходимся циклом по всем элементам словаря
    for key, value in required_fields.items():
        element = browser.find_element_by_css_selector(value[0])
        element.send_keys(value[1])

    element = browser.find_element_by_css_selector("#file")
    element.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
