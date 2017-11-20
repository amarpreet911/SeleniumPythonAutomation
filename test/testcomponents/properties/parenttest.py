from selenium import webdriver
import unittest


class BaseTest(unittest.TestCase, object):

    def __init__(self, driver):
        self.driver = driver

    def abc(self):
        print("a")

    @classmethod
    def setup_class(cls, self):
        # self.driver = webdriver.Firefox()

        self.driver = webdriver.Chrome(executable_path = '/home/amarpreet911/Documents/Selenium/Selenium_Files/chromedriver')
        self.driver.get("http://facebook.com")

    def test(self):
        a = 1 + 2
        print(a)