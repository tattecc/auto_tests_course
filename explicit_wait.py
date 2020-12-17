from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    #x = browser.find_element_by_id("price").text
    #x_str = str(x)
    #x_int = int(x_str)

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element_by_id("book")
    button.click()
    #message = browser.find_element_by_id("verify_message")

    #assert "successful" in message.text
    
    #button = browser.find_element_by_id("button")
    #button.click()

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