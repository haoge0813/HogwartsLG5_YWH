from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.add_member_type_page import AddMemberTypePage
from test_appium.page.base_page.base_page import BasePage


class AddMemberPage(BasePage):
    pass

    def name_send_keys(self,name):
        '''
        姓名输入
        :return:
        '''
        self.wait_find_element(*(MobileBy.XPATH,
                                 "//*[@resource-id='com.tencent.wework:id/et5']/android.widget.RelativeLayout/android.widget.EditText")).send_keys(
            name)
        pass

    def account_send_keys(self,account):
        '''
        帐号输入
        :return:
        '''
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@resource-id='com.tencent.wework:id/err']/android.widget.RelativeLayout/android.widget.EditText").send_keys(
            account)
        pass

    def nickname_send_keys(self,nickname):
        '''
        昵称输入
        :return:
        '''
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@resource-id='com.tencent.wework:id/esh']/android.widget.RelativeLayout/android.widget.EditText").send_keys(
            nickname)
        pass

    def sex_click(self):
        '''
        性别点击
        :return:
        '''
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@resource-id='com.tencent.wework:id/d_d']/android.widget.RelativeLayout").click()
        self.wait_find_element(*(MobileBy.XPATH,
                                 "//*[@resource-id='android:id/content']//*[@text='女']")).click()
        pass

    def phone_send_keys(self,phone):
        '''
        电话号码输入
        :return:
        '''
        self.wait_find_element(*(MobileBy.ID,
                                 "com.tencent.wework:id/fwi")).send_keys(phone)
        pass

    def save(self):
        '''
        保存按钮点击
        :return:
        '''
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("保存").instance(0));').click()
        return AddMemberTypePage(self.driver)