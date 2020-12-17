from selenium import webdriver
import time 
import os 

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ekaterina")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Zhukova")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("tat.ec@ya.ru")

    button_file = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '1.txt')
    button_file.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()