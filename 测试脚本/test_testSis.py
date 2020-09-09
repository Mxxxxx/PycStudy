import unittest, time, re
from selenium import webdriver


class testSis(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8080/sis/public/index.html"
        self.verificationErros = []
        self.accept_next_alert = True

    def test_login(self):
        driver = self.driver
        driver.get(self.base_url + '/')
        driver.maximize_window()
        time.sleep(5)
        driver.quit()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":  # 执行用例
    unittest.main(verbosity=2)
