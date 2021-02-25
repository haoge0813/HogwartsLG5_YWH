from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.add_member_type_page import AddMemberTypePage
from test_appium.page.base_page.base_page import BasePage

class MailListPage(BasePage):
    def add_member_click(self):
        self.wait_find_element(*(MobileBy.XPATH, "//*[@text='添加成员']")).click()

        return AddMemberTypePage(self.driver)