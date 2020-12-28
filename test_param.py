import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nStart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nQuit browser..")
    browser.quit()

def find_param(browser, value):
    browser.implicitly_wait(5)
    input1 = browser.find_element_by_css_selector(".textarea")
    value_str = str(value)
    input1.send_keys(value_str)
    browser.implicitly_wait(5)
    button_param = browser.find_element_by_css_selector(".submit-submission")
    button_param.click()
    browser.implicitly_wait(5)
    correct = browser.find_element_by_css_selector(".smart-hints__hint").text
    assert correct == "Correct!", "Crash test"

@pytest.mark.parametrize('element', ["895", "896", "897", "898", "899", "903", "904", "905"])
def test_param(browser, element):
    browser.implicitly_wait(5)
    link = f"https://stepik.org/lesson/236{element}/step/1"
    browser.get(link)
    answer = math.log(int(time.time()))
    find_param(browser, answer)