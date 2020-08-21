from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Email(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://mail.qq.com/"
        self.verificationErros = []
        self.accept_next_alert = True

    def test_email(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()
        driver.find_element_by_id("qqLoginTab").click()
        div1=driver.find_element_by_id("web_qr_login")
        div2=div1.find_element_by_id("web_qr_login_show")
        div3=div2.find_element_by_id("web_login")


