
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.webelement import WebElement

class TestTaskOne():

    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["noReset"] = "true"
        caps["appActivity"] = ".launch.WwMainActivity"
        caps["appPackage"] = "com.tencent.wework"
        caps["ensureWebviewsHavePages"] = True
        caps["settings[waitForIdleTimeout]"]=0
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.wait_activity(".launch.WwMainActivity",10)
        self.wait=WebDriverWait(self.driver,10,1)
    def tesrdown(self):
        self.driver.quit()
        pass

    def wait_find_element(self,*locat)->WebElement:
        return self.wait.until(lambda x:x.find_element(*locat))

    def test_task(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/en5' and @text='通讯录']").click()
        self.wait_find_element(*(MobileBy.XPATH,"//*[@text='添加成员']")).click()

        self.wait_find_element(*(MobileBy.XPATH,"//*[@text='手动输入添加']")).click()

        self.wait_find_element(*(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/et5']/android.widget.RelativeLayout/android.widget.EditText")).send_keys("张三")
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/err']/android.widget.RelativeLayout/android.widget.EditText").send_keys("164773018")
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@resource-id='com.tencent.wework:id/esh']/android.widget.RelativeLayout/android.widget.EditText").send_keys(
            "憨憨")

        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@resource-id='com.tencent.wework:id/d_d']/android.widget.RelativeLayout").click()
        self.wait_find_element(*(MobileBy.XPATH,
                                 "//*[@resource-id='android:id/content']//*[@text='女']")).click()
        self.wait_find_element(*(MobileBy.ID,
                                 "com.tencent.wework:id/fwi")).send_keys("13189411186")

        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@resource-id='com.tencent.wework:id/b8g' and @text='设置部门']").click()
        self.wait_find_element(*(MobileBy.XPATH,
                                 "//*[@text='admin']")).click()
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'确定')]").click()

        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("保存").instance(0));').click()

        element=self.wait_find_element(*(MobileBy.XPATH, "//*[@class='android.widget.Toast']"))

        assert element.text=="添加成功"





