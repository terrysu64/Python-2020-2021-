#Date: July 27, 2021
#Author: Terry Su
#Purpose: using unittest to organize a selenium webpage test script for https://www.python.org/

import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):
        
    #sets up webdriver
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get('https://www.python.org/')

    #any method that starts with 'test' will automatically be run (the method is the test itself)
    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()

        mainPage.search_text_element = 'pycon'
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    def test_title(self):
        python_title = page.MainPage(self.driver)
        assert python_title.is_title_matches()
        
    #runs after test case is finished
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
