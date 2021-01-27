import json

from selenium import webdriver


class BaseCase():
    def setup_method(self):
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_args)
        self.driver.implicitly_wait(10)

        # self.driver.maximize_window()

    def write_cookies(self):
        cookies = self.driver.get_cookies()
        with open("cookie.json", "w") as f:
            json.dump(cookies, f)


    def read_cookies(self):
        with open("cookie.json", "r") as f:
            # 读取 cookies
            cookies = json.load(f)
        return cookies

    def request_to_cookies(self,url:str,cookies:dict):
        self.driver.get(url)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
