from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

print("sample test case started")
driver = webdriver.Chrome("C:\Software\SeleniumTest\Browsers\chromedriver.exe")
driver.maximize_window()
# navigate to the url
driver.get("http://127.0.0.1:5000/")
time.sleep(2)
driver.find_element_by_id("name").send_keys("Elsa George")
driver.find_element_by_id("uid").send_keys("191795")
driver.find_element_by_id("cname").send_keys("UST Global")
driver.find_element_by_id("email").send_keys("sandrasaji@yahoo.co.in")
time.sleep(2)

driver.find_element_by_id("submit").send_keys(Keys.ENTER)
time.sleep(3)
# close the browser
driver.close()
print("test case successfully completed")
