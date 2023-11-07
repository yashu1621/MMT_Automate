from behave import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.Selenium_Utilities.Util import Util
from ApplicationLibrary.FunctionalLibrary.functional_elements import Control_Funtions
from ApplicationLibrary.ControlLibrary.control_elements import xpath_store

xpaths = xpath_store()

@when(u'the user enters invalid username and password')
def user_enters_invalid_details(context):
    context.Util.wait_click(xpaths.account_button)
    context.Util.simple_wait(xpaths.username)
    context.Control_Functions.data_input(xpaths.username,"testa@gmail.com")
    context.Control_Functions.click_button(xpaths.continue_btn)
    context.Util.simple_wait(xpaths.password)
    context.Control_Functions.data_input(xpaths.password,"12345678")
    context.Util.wait_click(xpaths.login_btn)
    WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.XPATH,xpaths.server_error)))
    context.Control_Functions.click_button(xpaths.close_login)
    time.sleep(3)

@when(u'the user enters valid username and password')
def user_enters_valid_details(context):

    context.Util.wait_click(xpaths.account_button)
    context.Util.simple_wait(xpaths.username)
    context.Control_Functions.data_input(xpaths.username,"somayaji.yashodhara@gmail.com")
    context.Control_Functions.click_button(xpaths.continue_btn)
    context.Util.simple_wait(xpaths.password)
    context.Control_Functions.data_input(xpaths.password,"Shell@1234")
    context.Util.wait_click(xpaths.login_btn)
    ele=context.Util.simple_wait(xpaths.otp)
    assert ele.is_displayed(), "otp is not displayed"
    time.sleep(3)
    context.Control_Functions.click_button(xpaths.close_login)
    time.sleep(5)
    context.Control_Functions.click_button(xpaths.close_modal_login)
    time.sleep(5)