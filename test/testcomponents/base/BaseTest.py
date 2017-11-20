from selenium import webdriver


class BaseTest(object):

    def __init__(self, driver):
        self.driver = driver

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
    def abc(self):
        print("a")

    def setUp(self):
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome(executable_path = '/home/amarpreet911/Documents/Selenium/Selenium_Files/chromedriver')
        self.driver.get("http://facebook.com")

    def test(self):
        a = 1 + 2
        print(a)
'''


