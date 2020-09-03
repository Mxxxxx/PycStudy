import csv
import os
import sys

from ddt import ddt, data, unpack, file_data
from selenium import webdriver
from selenium.webdriver import ActionChains
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
        self.base_url = "http://localhost:8080/sis/public/index.html"
        self.verificationErros = []
        self.accept_next_alert = True

    # 数据驱动
    # @data(["你好", u"你好_百度搜索"], ["守望", u"守望啊_百度"])
    # @unpack

    # @file_data读取json
    # @file_data('testjson.json')

    # 文件读取
    # @data(*getText('test_baidu.txt'))
    @unpack
    def test_baidusearch(self):
        self.driver.get(self.base_url+'/')
        self.driver.set_window_size(1488, 878)
        self.driver.find_element(By.NAME, "username").click()
        self.driver.find_element(By.NAME, "username").click()
        element = self.driver.find_element(By.NAME, "username")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.ID, "login_container").click()
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").click()
        element = self.driver.find_element(By.NAME, "password")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.NAME, "password").send_keys("123456")
        self.driver.find_element(By.CSS_SELECTOR, "#login_form .btn-success").click()
        self.driver.find_element(By.NAME, "username").click()
        self.driver.find_element(By.CSS_SELECTOR, ".mt-2:nth-child(5)").click()
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").click()
        element = self.driver.find_element(By.NAME, "password")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").click()
        element = self.driver.find_element(By.NAME, "password")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.NAME, "password").send_keys("123")
        self.driver.find_element(By.CSS_SELECTOR, "#login_form .btn-success").click()
        self.driver.find_element(By.CSS_SELECTOR, ".mr-auto").click()
        self.driver.find_element(By.ID, "stu_tab").click()
        element = self.driver.find_element(By.ID, "stu_tab")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) > td:nth-child(2)").click()
        self.driver.find_element(By.ID, "stu_table_toolbar_update").click()
        element = self.driver.find_element(By.ID, "stu_table_toolbar_update")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.ID, "stu_table_toolbar_update_form_studentName").click()
        self.driver.find_element(By.ID, "stu_table_toolbar_update_form_studentName").send_keys("小小的梦想🐷B1d")
        self.driver.find_element(By.ID, "stu_table_toolbar_update_form_submit").click()
        self.driver.find_element(By.CSS_SELECTOR, "#stu_table_toolbar_update_modal_dialog .ml-1 > .btn").click()
        self.driver.find_element(By.NAME, "btSelectItem").click()
        self.driver.find_element(By.ID, "stu_table_toolbar_add").click()
        element = self.driver.find_element(By.ID, "stu_table_toolbar_add")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        element = self.driver.find_element(By.ID, "stu_table_toolbar_add_form_studentName")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.ID, "stu_table_toolbar_add_form_studentName")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.ID, "stu_table_toolbar_add_form_studentName")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.ID, "stu_table_toolbar_add_form_studentName").click()
        self.driver.find_element(By.ID, "stu_table_toolbar_add_form_studentName").send_keys("dsd")
        self.driver.find_element(By.ID, "stu_table_toolbar_add_form_idCard").click()
        self.driver.find_element(By.ID, "stu_table_toolbar_add_form_idCard").send_keys("ds")
        self.driver.find_element(By.ID, "stu_table_toolbar_add_form_studentEmail").click()
        self.driver.find_element(By.ID, "stu_table_toolbar_add_form_studentEmail").send_keys("dsds")
        self.driver.find_element(By.ID, "stu_table_toolbar_add_form_studentNo").click()
        self.driver.find_element(By.ID, "stu_table_toolbar_add_form_studentNo").send_keys("dsd")
        self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(4) .filter-option-inner-inner").click()
        self.driver.find_element(By.CSS_SELECTOR, ".show > .inner > .dropdown-menu > li:nth-child(1) .text").click()
        dropdown = self.driver.find_element(By.ID, "stu_table_toolbar_add_form_classes.id")
        dropdown.find_element(By.XPATH, "//option[. = '幼儿园😂大班']").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 "#stu_table_toolbar_add_form > .form-group:nth-child(6) .filter-option-inner-inner").click()
        self.driver.find_element(By.ID, "stu_table_toolbar_add_form_submit").click()
        self.driver.find_element(By.LINK_TEXT, "3").click()

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
