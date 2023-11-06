from behave import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.Selenium_Utilities.Util import Util
#from ApplicationLibrary.ControlLibrary.control_elements import Control_Funtions
from ApplicationLibrary.FunctionalLibrary.functional_elements import Control_Funtions

@when(u'the user enters invalid username and password')
def user_enters_invalid_details(context):
    context.Util.wait_click("//li[@data-cy='account']")
    context.Util.simple_wait("//input[@id='username']")
    context.Control_Functions.data_input("//input[@id='username']","testa@gmail.com")
    context.Control_Functions.click_button("//button[@class='capText font16']")
    context.Util.simple_wait("//input[@id='password']")
    context.Control_Functions.data_input("//input[@id='password']","12345678")
    context.Util.wait_click("//button[@data-cy='login']")
    WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//span[@data-cy='serverError']")))
    context.Control_Functions.click_button("//span[@data-cy='CommonModal_3']")
    time.sleep(3)

@when(u'the user enters valid username and password')
def user_enters_valid_details(context):

    context.Util.wait_click("//li[@data-cy='account']")
    context.Util.simple_wait("//input[@id='username']")
    context.Control_Functions.data_input("//input[@id='username']","somayaji.yashodhara@gmail.com")
    context.Control_Functions.click_button("//button[@class='capText font16']")
    context.Util.simple_wait("//input[@id='password']")
    context.Control_Functions.data_input("//input[@id='password']","Shell@1234")
    context.Util.wait_click("//button[@data-cy='login']")
    ele=context.Util.simple_wait("//input[@id='otp']")
    assert ele.is_displayed(), "otp is not displayed"
    time.sleep(3)
    context.Control_Functions.click_button("//span[@data-cy='CommonModal_3']")
    time.sleep(5)
    context.Control_Functions.click_button("//span[@data-cy='closeModal']")
    time.sleep(5)