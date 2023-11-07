
from behave import *
import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from Utilities.Selenium_Utilities.Util import Util
from ApplicationLibrary.FunctionalLibrary.functional_elements import Control_Funtions
from ApplicationLibrary.ControlLibrary.control_elements import xpath_store

xpaths = xpath_store()

@given('User is on the MMT website')

def step_user_on_mmt_website(context):

    options=Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])   #required for automation otherwise continue button stops working
    context.driver = webdriver.Edge(options=options)
    context.Control_Functions = Control_Funtions(context.driver)
    context.Util = Util(context.driver)
    context.Control_Functions.navigate_url("https://www.makemytrip.com/")
    context.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")  #also required for automation but stopped working after one time (for continue button)
    context.Control_Functions.maximize()
    time.sleep(5)
    context.Util.frame_switch(xpaths.iframe)
    context.Control_Functions.click_button(xpaths.close_iframe_banner)
    context.Util.return_frame()
    context.Control_Functions.click_button(xpaths.close_modal_login)
    time.sleep(3)


@then('User validates the URL is "{expected_url}"')
def validate_url(context, expected_url):
    context.Control_Functions.validate_url(expected_url)


 
@then('User validates the presence of the MMT logo')
def validate_logo_element(context):
    context.Control_Functions.validate_logo(xpaths.logo)


@then(u'the user validates the title is present')
def validate_title(context):
    expected_title = "MakeMyTrip - #1 Travel Website 50% OFF on Hotels, Flights & Holiday"
    actual_title = context.driver.title
    context.Control_Functions.validate_title(expected_title,actual_title)


@then(u'the user validates the Login button is present')
def validate_login_button(context):
    context.Control_Functions.validate_login(xpaths.account_button)


   

     