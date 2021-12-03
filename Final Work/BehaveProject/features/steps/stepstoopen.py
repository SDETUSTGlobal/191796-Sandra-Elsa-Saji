from OpenSSL.rand import status
from behave import *
from selenium import webdriver


@given('Launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(executable_path="C:\Software\chromedriver_win32\chromedriver.exe")


@when('Open orange hrm homepage')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@then('verify that the logo present on page')
def verifyLogo(context):
    context.driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/img").is_displayed()
    #assert status is True


@then('close browser')
def closeBrowser(context):
    context.driver.close()
