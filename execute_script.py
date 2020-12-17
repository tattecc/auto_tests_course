from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x = browser.find_element_by_id("input_value").text
    x_str = str(x)
    x_int = int(x_str)
    y = calc(x)

    x_el = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", x_el)
    x_el.send_keys(y)
    
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()
    button = browser.find_element_by_xpath ("//button[@type='submit']")
    button.click()

finally:
    time.sleep(30)
    browser.quit()