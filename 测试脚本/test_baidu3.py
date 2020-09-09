import os
import time
import unittest

from selenium import webdriver


class Baidu3(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"

    def test_baiduSearch(self):
        driver = self.driver
        driver.get(self.base_url + '/')
        driver.implicitly_wait(30)
        driver.find_element_by_id("kw").send_keys("测试")
        driver.find_element_by_id("su").click()
        try:
            self.assertEqual("测试_百度", driver.title, msg="网页未打开")
        except:
            self.savescreenshot(driver, "baiduerror.png")

    # 生成测试截图
    def savescreenshot(self, driver, file_name):
        if not os.path.exists('./测试截图'):
            os.makedirs("./测试截图")
        now = time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))
        driver.get_screenshot_as_file("./测试截图/" + now + file_name)
        time.sleep(3)
