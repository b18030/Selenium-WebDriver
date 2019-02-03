from selenium import webdriver

class RunchromeTestsWindows():

	def test(self):
		driver=webdriver.Chrome("/home/tushar/Documents/Selenium/chromedriver")

		#Window Maximize
		driver.maximize_window()
		#open the url
		driver.get("https://www.youtube.com")
		#Get Title
		title=driver.title
		print("Title of the page is: "+ title)
		#Get Current Url
		Currenturl=driver.current_url
		print("Current Url Of the Web Page is: "+Currenturl)
		#Browser Refresh
		driver.refresh()
		print("Browser Refreshed for the first time")
		#OPen another url
		driver.get("https://www.facebook.com")
		Currenturl=driver.current_url
		print("Current Url Of the Web Page is: "+Currenturl)		
		#Browse back
		driver.back()
		print("GO One step back in browsing history")
		#Browse forward
		driver.forward()
		print("Go one step forward in browser history")
		#Get page source
		pageSource=driver.page_source
		print(pageSource)
		#Browser close/Quit
		#driver.close()
		driver.quit()



Browserinteractions=RunchromeTestsWindows()
Browserinteractions.test()		










# To create creating-virtual-environment

# https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html