from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys  
print("test case started")  
driver = webdriver.Chrome("C:\Software\SeleniumTest\Browsers\chromedriver.exe")  
driver.maximize_window()    
driver.get("https://www.myntra.com/")
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div/div/header/div[2]/div[3]/input").send_keys("Top")
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div/div/header/div[2]/div[3]/a/span").click()
time.sleep(2)
driver.get("https://www.myntra.com/tops/sassafras/sassafras-black-high-neck-cropped-top/12222036/buy")
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/main/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/button/p/div").click()
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/main/div[2]/div[2]/div[3]/div/div[1]").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/header/div[2]/div[2]/a[2]/span[3]").click()
time.sleep(2)
driver.close()
print("sample test case successfully completed")