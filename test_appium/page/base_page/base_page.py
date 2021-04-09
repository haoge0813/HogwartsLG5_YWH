import os

import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from commond.io import *

class BasePage():



    def __init__(self,driver:WebDriver = None):
        self.driver = driver
        if driver:
            self.wait = WebDriverWait(self.driver, 10, 1)
        else:
            self.wait = None


    def wait_find_element(self , locat) -> WebElement:
        return self.wait.until(lambda x:x.find_element(*locat))

    def wait_find_and_click(self,locat):
        self.wait_find_element(locat).click()

    def wait_find_and_send(self,content,locat):
        self.wait_find_element(locat).send_keys(content)


    def find(self,locat)->WebElement:
        return self.driver.find_element(*locat)

    def find_and_click(self,locat):
        self.find(locat).click()

    def find_and_send(self,contene,locat):
        self.find(locat).send_keys(contene)

    def run_steps(self,yaml_path,key:str=None,content:str=None):

        data=get_yaml_data(yaml_path,key=key)

        for item in data :
            action = item["action"]
            if action=="find_and_click":
                self.find_and_click(item["locator"])
            elif action=="find_and_send":
                self.find_and_send(content if content else item["content"],item["locator"])
            elif action == "wait_find_and_click":
                self.wait_find_and_click(item["locator"])
            elif action=="wait_find_and_send":
                self.wait_find_and_send(content if content else item["content"],item["locator"])





