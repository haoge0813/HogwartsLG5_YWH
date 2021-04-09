from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.mail_list_page.mail_list_page import MailListPage

from test_appium.page.base_page.base_page import BasePage


class MainPage(BasePage):
    pass

    def mail_list_click(self):
        self.run_steps(__file__,"mail_list_click")
        return MailListPage(self.driver)