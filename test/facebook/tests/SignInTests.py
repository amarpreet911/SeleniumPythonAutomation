import unittest
from selenium import webdriver
import sys
sys.path.insert(0, '/home/amarpreet911/Documents/Python/Work_Space/SeleniumPython/PageObModel/test/facebook/pages')
import LoginPage as l_page
import HomePage as h_page

sys.path.insert(0, '/home/amarpreet911/Documents/Python/Work_Space/SeleniumPython/PageObModel/test/testcomponents/base')
import BaseTest as bt


def setup_module():
    print(__name__, ': setup_module(), SignInTest ~~~~~~~~~~~~~~~~~~~~~~')


def teardown_module():
    print(__name__, ': teardown_module(), signInTest Close ~~~~~~~~~~~~~~~~~~~')


class SignInTests(unittest.TestCase, bt.BaseTest):
    '''
    def __init__(self, driver):
        self.driver = driver
        super.__init__(driver)
        # will run before every test
    '''
    def setup(self):
        print(__name__, ': TestClass.setup()  - - - - - - - -')

    # will run after every test
    def teardown(self):
        print(__name__, ': TestClass.teardown() - - - - - - -')

    def test_login(self):
        login_page = l_page.LoginPage(self.driver)
        login_page.enter_text("test_user@gmail.com", "password")
        login_page.click()
        print(__name__, ': TestClass.test_method_1()')
        home_page = h_page.HomePage(self.driver)
        self.assertTrue(home_page.visible_logo().is_displayed())

    def test_login_invalid_id(self):
        print(__name__, ': TestClass.test_method_2()')

'''
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome(executable_path = '/home/amarpreet911/Documents/Selenium/Selenium_Files/chromedriver')
        cls.driver.get("http://facebook.com")
        print(__name__, ': TestClass.setup_class() ----------')

    @classmethod
    def teardown_class(cls):
        cls.driver.close()  ########################
        print(__name__, ': TestClass.teardown_class() -------')
'''



'''

def test_search_in_python_org(self):

        # Load the main page. In this case the home page of Python.org.
        main_page = login_page.(self.driver)

        # Checks if the word "Python" is in title
        assert main_page.is_title_matches(), "python.org title doesn't match."

        # Sets the text of search textbox to "pycon"
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)

        # Verifies that the results page is not empty
        assert search_results_page.is_results_found(), "No results found."

'''
