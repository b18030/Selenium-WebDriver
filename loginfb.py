from selenium import webdriver
driver=webdriver.Chrome("/home/tushar/Documents/Selenium/chromedriver")
driver.get("https://www.facebook.com")
driver.find_element_by_name("email").send_keys("tushar22.tg.tg@gmail.com")

driver.find_element_by_name("pass").send_keys("B18030goyal")
driver.find_element_by_id("loginbutton").click()
