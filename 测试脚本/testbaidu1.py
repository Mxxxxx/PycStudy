import os

from ddt import ddt, data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


# -*- coding: utf-8 -*

@ddt
class Baidu1(unittest.TestCase):
    # 测试固件
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"
        self.verificationErros = []
        self.accept_next_alert = True

    # 数据驱动使用

    @data("你好", "守望")
    def test_baidusearch(self, value):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(value)
        driver.find_element_by_id("su").click()

        # 断言测试
        # time.sleep(6)
        # try:
        #     self.assertEqual("守望先锋_百度",driver.title,msg="网页未打开")
        # except:
        #     self.savescreenshot(driver,"baiduerror.png")
        time.sleep(3)
        driver.quit()

    @unittest.skip('skipping')
    def test_hao(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("hao123").click()
        try:
            self.assertEqual(u"hao123_上网从这里开始码", driver.title)
        except:
            self.savescreenshot(driver, "hao123Error.png")
        time.sleep(6)
        driver.quit()

    def savescreenshot(self, driver, file_name):
        if not os.path.exists('./errorImage'):
            os.makedirs("./errorImage")
        now = time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))
        driver.get_screenshot_as_file("./errorImage/" + now + file_name)
        time.sleep(3)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    # 判断alert是否存在，可删除
    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    # 关闭alert，可删除
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

        # test fixture，清除环境
        # 测试固件

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    if __name__ == "__main__":  # 执行用例
        unittest.main(verbosity=2)
