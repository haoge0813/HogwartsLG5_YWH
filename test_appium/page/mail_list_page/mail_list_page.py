from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.add_member_type_page.add_member_type_page import AddMemberTypePage
from test_appium.page.base_page.base_page import BasePage

class MailListPage(BasePage):
    def add_member_click(self):
        self.run_steps(__file__,"add_member_click")
        return AddMemberTypePage(self.driver)