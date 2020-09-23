import HTMLTestRunner
import os
import sys
import time
import unittest

from selenium import webdriver


class Baidu3(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://47.92.97.206:8080/sis/public/index.html"

    def test_baiduSearch(self):
        driver = self.driver
        driver.get(self.base_url + '/')
        time.sleep(6)
        # driver.find_element_by_id("kw").send_keys("测试")
        # driver.find_element_by_id("su").click()
        # try:
        #     self.assertEqual("测试_百度", driver.title, msg="网页未打开")
        # except:
        #     self.savescreenshot(driver, "baiduerror.png")
        # time.sleep(3)
        driver.quit()
    # 生成测试截图
    def savescreenshot(self, driver, file_name):
        if not os.path.exists('./测试截图'):
            os.makedirs("./测试截图")
        now = time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))
        driver.get_screenshot_as_file("./测试截图/" + now + file_name)
        time.sleep(3)

# 测试报告
# if __name__ == "__main__":
#     # 当前文件所在得到文件夹的绝对路径
#     curpath = sys.path[0]
#     if not os.path.exists(curpath + '/测试报告'):
#         os.makedirs(curpath + '/测试报告')
#
#     now = time.strftime("%Y-%m-%d-%H %M %S", time.localtime(time.time()))
#     print("------------")
#     print(time.time())
#     print("------------")
#     print(time.localtime(time.time()))
#     print("------------")
#     print(now)
#
#     filename = curpath + '/resultreport/' + now + 'resultreport.html'
#     with open(filename, 'wb+') as fp:
#         runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"测试报告", description=u"用例报告", verbosity=2)
#         suite = creatsuit()
#         runner.run(suite)
