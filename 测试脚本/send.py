from selenium import webdriver

driver = webdriver.Firefox()
driver.get("file:///F:/Python=Study/Html/send.html")
driver.find_element_by_tag_name("input").click()


