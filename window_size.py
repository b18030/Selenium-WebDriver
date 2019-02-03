from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WindowSize():

    def test(self):    
        driver=webdriver.Chrome("/home/tushar/Documents/Selenium/chromedriver")
        driver.maximize_window()
        driver.get("https://en.wikipedia.org/wiki/Main_Page")
        driver.implicitly_wait(5)

        height=driver.execute_script("return window.innerHeight;")
        width=driver.execute_script("return window.innerWidth;")
        print("Height: "+ str(height))
        print("Width: "+ str(width))

ff=WindowSize()
ff.test()        


