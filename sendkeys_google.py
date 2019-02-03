from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClickAndSendKeys():

    def test(self):    
        driver=webdriver.Chrome("/home/tushar/Documents/Selenium/chromedriver")
        driver.maximize_window()
        driver.get("https://www.google.com")
        driver.implicitly_wait(5)

        InputField = driver.find_element(By.XPATH, "//input[@title='Search']")
        InputField.send_keys("Automation by Tushar Goyal")
        time.sleep(3)
        InputField.clear()
        time.sleep(3)
        InputField.send_keys("Automation By IITIAN Tushar Goyal")
        time.sleep(2)
        driver.find_element(By.XPATH,"//div[@class='FPdoLc VlcLAe']//input[@value='Google Search']").click()




ff = ClickAndSendKeys()
ff.test()