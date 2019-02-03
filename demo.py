import time
from selenium import webdriver

driver= webdriver.Chrome("/home/tushar/Documents/Selenium/chromedriver")
driver.get("http://www.amazon.com")
driver.get_screenshot_as_file("/home/tushar/Documents/Selenium/Helloamazon.png")


