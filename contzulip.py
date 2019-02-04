from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Xpath to first row of upcoming contest Table containing the headers =>
# //div[@class='contestList']/div[@class='datatable']/div/table/tbody/tr[1]/th


class codeforces():

    def tableheader(self):    
        driver=webdriver.Chrome("/home/tushar/Documents/Selenium/chromedriver")
        driver.maximize_window()
        driver.get("https://codeforces.com/contests")
        getcolumnheaders=driver.find_elements_by_xpath("//div[@class='contestList']/div[@class='datatable']/div/table/tbody/tr[1]/th")
        for col in getcolumnheaders:
        	print(col.text)



list_=codeforces()
list_.tableheader()