from selenium.webdriver.common.by import By

import sys
sys.path.insert(0, '/home/amarpreet911/Documents/Python/Work_Space/SeleniumPython/PageObModel/test/testcomponents/base')
import BasePage as base


class HomePage(base.BasePage):
    logo_home = (By.XPATH, '//*[@id="u_0_d"]')

    def visible_logo(self):
        element = self.driver.find_element(*self.logo_home)
        return element
