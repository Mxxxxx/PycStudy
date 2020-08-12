import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("file:///F:/Python=Study/Html/checkbox.html")
time.sleep(6)
inputs = driver.find_elements_by_tag_name("input")
for input in  inputs:
    if input.get_attribute("type")=="radio":
        input.click()

time.sleep(6)