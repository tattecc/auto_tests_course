import unittest
from selenium import webdriver
import time

class TestReg(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        element1 = browser.find_element_by_xpath('//input[@placeholder="Input your first name"]')
        element1.send_keys('a')
        element2 = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
        element2.send_keys('b')
        element3 = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
        element3.send_keys('c')    

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        
    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        element1 = browser.find_element_by_xpath('//input[@placeholder="Input your first name"]')
        element1.send_keys('a')
        element2 = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
        element2.send_keys('b')
        element3 = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
        element3.send_keys('c')    

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        
if __name__ == "__main__":
    unittest.main()