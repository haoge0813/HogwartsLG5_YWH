import os

import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():



    def __init__(self,driver:WebDriver = None):
        self.driver = driver
        if driver:
            self.wait = WebDriverWait(self.driver, 10, 1)
        else:
            self.wait = None


    def wait_find_element(self , *locat) -> WebElement:
        return self.wait.until(lambda x:x.find_element(*locat))

    def find(self,*locat):
        return self.driver.find_element(*locat)


