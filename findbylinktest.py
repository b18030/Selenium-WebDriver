from selenium import webdriver

class FindByLinkText():
	
	def test(self):
		baseUrl="https://learn.letskodeit.com"
		driver=webdriver.Chrome("/home/tushar/Documents/Selenium/chromedriver")
		driver.get(baseUrl)


		elementByLinkText=driver.find_element_by_link_text("Login")

		if elementByLinkText is not None:
			print("We found an element By Link Text")

		elementByPartialLinkText=driver.find_element_by_partial_link_text("Sign")

		if elementByPartialLinkText is not None:
			print("We found an element By Partial Link Text")



ft=FindByLinkText()
ft.test()						