#Date: July 26, 2021
#Author: Terry Su
#Purpose: using Selenium action chains to automate cookie clicker

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')
driver.get('https://orteil.dashnet.org/cookieclicker/')
driver.maximize_window()

#implicit wait
driver.implicitly_wait(4)

cookie = driver.find_element_by_id('bigCookie')
cookie_count = driver.find_element_by_id('cookies')
items = [driver.find_element_by_id('productPrice' + str(i)) for i in range(3,-1,-1)] #going in reverse lets us check the higher class upgrades first

actions = ActionChains(driver)
actions.click(cookie)

#click the cookie, then check for available upgrades
while True:
    actions.perform()
    count = int(cookie_count.text.split(' ')[0])

    for item in items:

        text = item.get_attribute('textContent')

        if ',' in text:
            testue = int(text[:text.index(',')]+text[text.index(',')+1:])
        else:
            testue = int(item.get_attribute('textContent'))

        if testue <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()



