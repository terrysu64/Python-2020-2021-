#Date: July 12, 2021
#Author: Terry Su
#Purpose: Playing around with the selenium automated web testing framework using Python
#great Python selenium cheatsheet: http://allselenium.info/python-selenium-commands-cheat-sheet-frequently-used/

from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title #assert = check for bugs or if an element exists in the webpage HTML
show_msg_button = chrome_browser.find_element_by_class_name('btn-default')
print(show_msg_button.get_attribute('innerHTML')) #button text

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('user-message')

user_message.clear()
user_message.send_keys('Hey, I am Terry')

show_msg_button.click()
output_message = chrome_browser.find_element_by_id('display')
assert 'Hey, I am Terry' in output_message.text

chrome_browser.quit()
