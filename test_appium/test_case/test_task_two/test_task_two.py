import pytest

from commond.io import get_yaml_data
from test_appium.app import App


class TestTaskTwo():


    def setup(self):
        pass
        self.app=App()
        self.main=self.app.start().go_to_main()

    @pytest.mark.parametrize("name,account,nickname,phone", get_yaml_data(__file__))
    def test_task(self,name,account,nickname,phone):

        add_member=self.main.mail_list_click().add_member_click().input_add_click()

        add_member.name_send_keys(name)
        add_member.account_send_keys(account)
        add_member.nickname_send_keys(nickname)
        add_member.sex_click()
        add_member.phone_send_keys(phone)
        element=add_member.save().get_tost()
        assert element.text=="添加成功"



    def teardown(self):
        self.app.stop()