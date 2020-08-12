from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
# 最大化浏览器
driver.maximize_window()
time.sleep(6)
    # # 通过元素id查询
    # driver.find_element_by_id("kw").send_keys("你好")
    # driver.find_element_by_id("su").click()
    #
    # # 通过name定位
    # driver.find_element_by_name("wd").send_keys("hello")
    # driver.find_element_by_id("su").click()
    #
    # # 通过class_name定位无法成功，以为该元素内容过多,无法定位  前提：元素数量唯一，否则出错
    # driver.find_element_by_class_name("s_ipt")
    #
    # # 通过tag name定位,前提：元素数量唯一，否则出错
    # driver.find_element_by_tag_name("input").send_keys("nih")
    # driver.find_element_by_id("su").click()
    #
    # # 通过link text定位  数量唯一
    # driver.find_element_by_link_text("视频").click()
    #
    # # xpath定位
    # driver.find_element_by_xpath("//*[@id='kw']").send_keys("he")
    # driver.find_element_by_xpath("//*[@id='su']").click()
    #
    # # css定位
    # driver.find_element_by_css_selector("#kw").send_keys("aaa")
    # driver.find_element_by_css_selector("#su").click()


time.sleep(6)
driver.quit()
