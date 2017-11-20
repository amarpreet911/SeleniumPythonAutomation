from __future__ import print_function
from selenium import webdriver


def setup_package(self):
    print('')
    # self.driver = webdriver.Chrome(executable_path = '/home/amarpreet911/Documents/Selenium/Selenium_Files/chromedriver')
    # self.driver.get("http://facebook.com")
    print(__name__, '__init__.py : setup_package() ========================================')

def teardown_package():
    print(__name__, '__init__.py : teardown_package() =====================================')
