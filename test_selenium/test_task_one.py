from selenium.webdriver.common.by import By

from base_case import BaseCase
import time

import selenium
from selenium import webdriver
import pytest
class TestWechat(BaseCase):


    @pytest.mark.run(order=1)
    def test_login(self):

        url="https://work.weixin.qq.com/"
        self.driver.get(url)
        self.driver.find_element(By.CSS_SELECTOR,".index_top_operation_loginBtn").click()
        time.sleep(10)
        assert self.driver.current_url=="https://work.weixin.qq.com/wework_admin/frame","登录失败"
        pass

    @pytest.mark.run(order=2)
    def test_login_cookies(self):
        self.write_cookies()

        #重新开个口子
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()

        cookies=self.read_cookies()
        self.request_to_cookies(url="https://work.weixin.qq.com/",cookies=cookies)
        driver.get("https://work.weixin.qq.com/wework_admin/frame")
        assert driver.current_url == "https://work.weixin.qq.com/wework_admin/frame", "登录失败"

    @pytest.mark.run(order=3)
    def test_task_one(self):
        self.driver.find_element(By.ID,"menu_customer").click()
        pass





# import json
# from time import sleep
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
#
# class TestTestbaidu():
#     def setup_method(self):
#         chrome_args = webdriver.ChromeOptions()
#         chrome_args.debugger_address = "127.0.0.1:9222"
#         self.driver = webdriver.Chrome(options=chrome_args)
#
#     # def teardown_method(self):
#     #     self.driver.quit()
#
#     def test_cookie(self):
#         self.driver.
#         # 获取  cookie
#         # cookies = self.driver.get_cookies()
#         # 以文件流的形式打开文件
#         # with open("cookie.json", "w") as f:
#             # 存储 cookie 到 cookie.json
#         #     json.dump(cookies, f)
#
#         # self.driver.get("https://work.weixin.qq.com/")
#         # # 以文件流的形式打开文件
#         # with open("cookie.json", "r") as f:
#         #     # 读取 cookies
#         #     cookies = json.load(f)
#         # # 注入 cookies
#         # for cookie in cookies:
#         #     self.driver.add_cookie(cookie)
#         # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
#         # sleep(3)
#         # self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()
#         pass
#
#     def test_testbaidu(self):
#         self.driver.get("https://work.weixin.qq.com/")
#         sleep(15)
#         self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()
#         self.driver.find_element(By.XPATH, '//*[@id="menu_customer"]').click()
#         self.driver.find_element(By.ID, "kw").send_keys(Keys.ENTER)
#
