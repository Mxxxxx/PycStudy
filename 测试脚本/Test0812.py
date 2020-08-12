import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
# 最大化浏览器
driver.maximize_window()
time.sleep(4)

# # 搜索
# driver.find_element_by_css_selector("#kw").send_keys("你好")
# driver.find_element_by_css_selector("#su").click()
# time.sleep(6)
# # 清除搜索内容
# driver.find_element_by_name("wd").clear()
# time.sleep(3)
# # 重新搜索
# driver.find_element_by_css_selector("#kw").send_keys("守望先锋")
# # 提交查询内容
# driver.find_element_by_id("su").submit()

# driver.find_element_by_id("s-bottom-layer-left")
# print("text=" + driver.find_element_by_id("s-bottom-layer-left"))

# driver.find_element_by_id("kw").send_keys("守望先锋")
# driver.find_element_by_id("su").submit()
# time.sleep(4)
# driver.minimize_window()
# # 设置浏览器大小
# time.sleep(4)
# driver.set_window_size(400,800)
# driver.maximize_window()
# # 浏览器后退
# driver.back()
# time.sleep(6)
# # 浏览器前进
# driver.forward()
# js="var q=document.documentElement.scrollTop=100000"
# driver.execute_script(js)


# driver.implicitly_wait(10)
# driver.find_element_by_link_text("owl直播_2020守望先锋职业联赛直播间_虎牙直播").click()

# title = driver.title
# print("title=" + title)
# url = driver.current_url
# print("url=" + url)

# driver = webdriver.Firefox()
# driver.get("http://127.0.0.1:88/biz/user-login-L2Jpei8=.html")
#
# driver.maximize_window()
# # 输入账户
# driver.find_element_by_id("account").send_keys("admin")
# driver.find_element_by_id("account").send_keys(Keys.TAB)
# # 输入密码
# driver.find_element_by_name("password").send_keys("mx199846")
# driver.find_element_by_name("password").send_keys(Keys.ENTER)

# 复制
driver.find_element_by_css_selector("#kw").send_keys("你好")
time.sleep(6)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')

# 剪贴
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')

time.sleep(6)
driver.quit()
