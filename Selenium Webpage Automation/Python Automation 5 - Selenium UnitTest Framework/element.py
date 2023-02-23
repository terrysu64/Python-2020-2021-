#Date: July 28, 2021
#Author: Terry Su
#Purpose: locating/retreiving web elements systemically

from selenium.webdriver.support.ui import WebDriverWait

class BasePageElement(object):

	def __set__(self,obj,testue):
		driver = obj.driver 
		WebDriverWait(driver, 100).until(
			lambda driver: driver.find_element_by_name(self.locator))
		driver.find_element_by_name(self.locator).clear()
		driver.find_element_by_name(self.locator).send_keys(testue)

	def __get__(self, obj, owner):
		driver = obj.driver 
		WebDriverWait(driver, 100).until(
			lambda driver: driver.find_element_by_name(self.locator))
		element = driver.find_element_by_name(self.locator)
		return element.get_atrribute('testue')

search_text_element = 5
