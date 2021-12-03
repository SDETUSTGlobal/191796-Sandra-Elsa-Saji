from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys  
print("test case started")  
driver = webdriver.Chrome("C:\Software\SeleniumTest\Browsers\chromedriver.exe")  
driver.maximize_window()    
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="login1"]').send_keys("elsageoge2000")
driver.find_element_by_name('passwd').send_keys("812000@Ss")
driver.find_element_by_xpath('//*[@id="login1"]').click()
time.sleep(2)
driver.close()
print("sample test case successfully completed")