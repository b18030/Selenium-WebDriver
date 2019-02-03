from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class GetText():

    def test(self):    
        driver=webdriver.Chrome("/home/tushar/Documents/Selenium/chromedriver")
        driver.maximize_window()
        driver.get("https://en.wikipedia.org/wiki/Main_Page")
        driver.implicitly_wait(5)

        Otherareasofwiki=driver.find_element(By.XPATH,"//a[@title='Wikipedia:Community portal']")
        content=Otherareasofwiki.text 
        print("Text on element is=>"+content)


ff=GetText()
ff.test()        