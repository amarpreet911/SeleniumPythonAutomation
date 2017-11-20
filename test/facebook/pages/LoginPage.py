from selenium.webdriver.common.by import By

import sys
sys.path.insert(0, '/home/amarpreet911/Documents/Python/Work_Space/SeleniumPython/PageObModel/test/testcomponents/base')
import BasePage as base
# from PageObModel.test.testcomponents.base import BasePage as base
from selenium.webdriver.common.keys import Keys
# from selenium import webdriver


class LoginPage(base.BasePage):
# base.BasePage
    email = (By.XPATH, '//*[@id="email"]')
    password = (By.XPATH, '//*[@id="pass"]')
    login_button = (By.XPATH, '//*[@id="loginbutton"]')

    def enter_text(self, user_email, user_password):
        element = self.driver.find_element(*self.email)
        element.send_keys(user_email)
        element = self.driver.find_element(*self.password)
        element.send_keys(user_password)

    def click(self):
        element = self.driver.find_element(*self.login_button)
        element.click()
