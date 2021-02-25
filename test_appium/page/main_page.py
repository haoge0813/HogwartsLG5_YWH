from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.mail_list_page import MailListPage

from test_appium.page.base_page.base_page import BasePage


class MainPage(BasePage):
    pass

    def mail_list_click(self):
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@resource-id='com.tencent.wework:id/en5' and @text='通讯录']").click()

        return MailListPage(self.driver)