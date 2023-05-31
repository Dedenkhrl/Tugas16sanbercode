import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



def test_success_login(driver): #test cases 1
    baseUrl = ("https://www.saucedemo.com")
    driver.get(baseUrl)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "[data-test='password']").send_keys("secret_sauce")
    driver.find_element(By.NAME, "login-button").click()
        