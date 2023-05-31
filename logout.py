import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import baselogin

class Testcheckout(unittest.TestCase): # test scenario

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_logout(self): #test cases 1
        baseUrl = ("https://www.saucedemo.com")
        driver = self.browser
        driver.get(baseUrl)
        baselogin.test_success_login(driver)
        driver.find_element(By.CLASS_NAME, "bm-burger-button").click()
        driver.find_element(By.ID, "logout_sidebar_link").click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl)    

if __name__ == '__main__':
    unittest.main()