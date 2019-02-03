from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClickAndSendKeys():

    def test(self):    
        driver=webdriver.Chrome("/home/tushar/Documents/Selenium/chromedriver")
        driver.maximize_window()
        driver.get("https://www.facebook.com")
        driver.implicitly_wait(5)

        emailField = driver.find_element(By.ID, "email")
        emailField.send_keys("automated by tushar")

        passwordField = driver.find_element(By.ID, "pass")
        passwordField.send_keys("B18030goyal")

        time.sleep(3)

        emailField.clear()

        time.sleep(3)

        emailField.send_keys("tushar22.tg.tg@gmail.com")
        time.sleep(2)
        driver.find_element_by_id("loginbutton").click()




ff = ClickAndSendKeys()
ff.test()