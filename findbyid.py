from selenium import webdriver

class FindByIdandname():
	
	def test(self):
		baseUrl="https://www.youtube.com"
		driver=webdriver.Chrome("/home/tushar/Documents/Selenium/chromedriver")
		driver.get(baseUrl)
		elementById=driver.find_element_by_id("search-input")
		elementByName=driver.find_element_by_name("search_query")

		if elementById is not None:
			print("We found an element By Id")
		if elementByName is not None:
			print("We found an element By Name")


ft=FindByIdandname()
ft.test()						