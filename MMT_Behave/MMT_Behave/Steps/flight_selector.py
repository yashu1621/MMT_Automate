from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.Selenium_Utilities.Util import Util
from ApplicationLibrary.ControlLibrary.control_elements import xpath_store
from ApplicationLibrary.FunctionalLibrary.functional_elements import Control_Funtions

xpaths=xpath_store()

@when(u'the user selects flights with lowest price and time')
def user_selects_flight(context):
    
    #context.Util.simple_wait("//input[@id='listingFilterCheckbox'])[1]")
    #context.Control_Functions.click_button("(//input[@id='listingFilterCheckbox'])[1]")
    context.Util.simple_wait(xpaths.prefer_selector)
    context.Control_Functions.click_button(xpaths.prefer_selector)

@Then(u'the user Validates the flight name and Fare Summary')
def user_validates_fare(context):
    context.Control_Functions.click_button(xpaths.view_price)
    time.sleep(3)
    original_window = context.driver.current_window_handle
    context.Control_Functions.click_button(xpaths.book_now)
    time.sleep(5)
    for window_handle in context.driver.window_handles:
        if window_handle != original_window:
            context.driver.switch_to.window(window_handle)
            break
    faresummary = context.Control_Functions.find_ele(xpaths.fare_summary)
    assert faresummary.is_displayed(), "faresummary is not displayed"
    flight_name = context.Control_Functions.find_ele(xpaths.flight_name)
    assert flight_name.is_displayed(), "flightname is not displayed"