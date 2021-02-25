from appium.webdriver.common.mobileby import MobileBy


from test_appium.page.base_page.base_page import BasePage


class AddMemberTypePage(BasePage):


    def input_add_click(self):
        from test_appium.page.add_member_page import AddMemberPage
        self.wait_find_element(*(MobileBy.XPATH, "//*[@text='手动输入添加']")).click()
        return AddMemberPage(self.driver)

    def get_tost(self):
        return self.wait_find_element(*(MobileBy.XPATH, "//*[@class='android.widget.Toast']"))