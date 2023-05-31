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

    def test_success_checkout(self): #test cases 1
        baseUrl = ("https://www.saucedemo.com")
        driver = self.browser
        driver.get(baseUrl)
        baselogin.test_success_login(driver)
        driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "/cart.html")
        driver.find_element(By.ID, "checkout").click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "/checkout-step-one.html")
        driver.find_element(By.ID, "first-name").send_keys("deden")
        driver.find_element(By.CSS_SELECTOR, "[data-test='lastName']").send_keys("efendi")
        driver.find_element(By.ID, "postal-code").send_keys("40123")
        driver.find_element(By.ID, "continue").click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "/checkout-step-two.html")
        driver.find_element(By.ID, "finish").click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "/checkout-complete.html")

if __name__ == '__main__':
    unittest.main()