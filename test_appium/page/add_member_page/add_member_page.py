from test_appium.page.add_member_type_page.add_member_type_page import AddMemberTypePage
from test_appium.page.base_page.base_page import BasePage


class AddMemberPage(BasePage):
    pass
    def name_send_keys(self,name):

        '''
        姓名输入
        :return:
        '''
        self.run_steps(__file__, key="name_send_keys",content=name)
        pass

    def account_send_keys(self,account):
        '''
        帐号输入
        :return:
        '''
        self.run_steps(__file__, key="account_send_keys", content=account)
        pass

    def nickname_send_keys(self,nickname):
        '''
        昵称输入
        :return:
        '''
        self.run_steps(__file__, key="nickname_send_keys", content=nickname)
        pass

    def sex_click(self):
        '''
        性别点击
        :return:
        '''
        self.run_steps(__file__, key="sex_click")
        pass

    def phone_send_keys(self,phone):
        '''
        电话号码输入
        :return:
        '''
        self.run_steps(__file__, key="phone_send_keys",content=phone)
        pass

    def save(self):
        '''
        保存按钮点击
        :return:
        '''
        self.run_steps(__file__, key="save")
        return AddMemberTypePage(self.driver)