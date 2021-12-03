from behave import *
from selenium import webdriver


@given('Launch chrome browser1')
def launchBrowser(context):
    context.driver = webdriver.Chrome(executable_path="C:\Software\chromedriver_win32\chromedriver.exe")


@when('Open orange hrm homepage1')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when('Enter username "admin" and password "admin123"')
def verifyLogin(context):
    context.driver.find_element_by_id("txtUsername").send_keys("Admin")
    context.driver.find_element_by_id("txtPassword").send_keys("admin123")


@when('Click on login button')
def click(context):
    context.driver.find_element_by_id("ctl00$MainContent$login_button").click()


@then('User must successfully login to Dashboard')
def Browser(context):
    context.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[1]/h1").text
    context.driver.close()
