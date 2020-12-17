from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    
    x_el = browser.find_element_by_id("answer")
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