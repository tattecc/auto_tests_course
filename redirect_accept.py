from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    button_capcha = browser.find_element_by_xpath ("//button[@type='submit']")
    button_capcha.click()

    first_window = browser.window_handles[1]
    browser.switch_to.window(first_window)

    x = browser.find_element_by_id("input_value").text
    x_str = str(x)
    x_int = int(x_str)
    y = calc(x)

    x_el = browser.find_element_by_id("answer")
    x_el.send_keys(y)
    
    button = browser.find_element_by_xpath ("//button[@type='submit']")
    button.click()

finally:
    time.sleep(30)
    browser.quit()