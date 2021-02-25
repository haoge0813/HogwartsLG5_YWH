from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.page.base_page.base_page import BasePage
from test_appium.page.main_page import MainPage


class App(BasePage):




    def start(self):
        if not self.driver:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["noReset"] = "true"
            caps["appActivity"] = ".launch.WwMainActivity"
            caps["appPackage"] = "com.tencent.wework"
            caps["ensureWebviewsHavePages"] = True
            caps["settings[waitForIdleTimeout]"] = 0

            print("=======hahha======")
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

            self.driver.wait_activity(".launch.WwMainActivity", 10)
            self.wait = WebDriverWait(self.driver, 10, 1)
        else:
            self.driver.launch_app()

        return self

    def restart(self):
        self.driver.quit()
        self.driver.launch_app()


    def stop(self):
        self.driver.quit()


    def go_to_main(self):

        return MainPage(self.driver)