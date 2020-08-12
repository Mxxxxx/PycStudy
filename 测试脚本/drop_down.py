import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("file:///F:/Python=Study/Html/drop_down.html")
time.sleep(6)
options = driver.find_elements_by_tag_name("option")
for option in options:
    if option.get_attribute("value") == "9.03":
        option.click()
time.sleep(6)
driver.quit()
