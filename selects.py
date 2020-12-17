from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("num1").text
    x_str = str(x)
    x_int = int(x_str)
    y = browser.find_element_by_id("num2").text
    y_str = str(y)
    y_int = int(y_str)
    sum = str(x_int + y_int)
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum)

    
    button = browser.find_element_by_xpath ("//button[@type='submit']")
    button.click()

finally:
    time.sleep(30)
    browser.quit()