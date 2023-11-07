from behave import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from Utilities.Selenium_Utilities.Util import Util
from ApplicationLibrary.ControlLibrary.control_elements import xpath_store
from ApplicationLibrary.FunctionalLibrary.functional_elements import Control_Funtions

xpaths = xpath_store()

@When(u'the user selects the round radio option')
def user_selects_round(context):
    context.Util.simple_wait(xpaths.round)
    context.Control_Functions.click_button(xpaths.round)
    

@when(u'the user selects "Bangalore" as the from city')
def user_selects_departure(context):
    time.sleep(3) #fails if this sleep isnt given
    context.Control_Functions.data_input(xpaths.fromcity,"Bengaluru")
    time.sleep(5)
    context.Util.wait_click(xpaths.airport_selector)
    

@when(u'the user selects "London" as the to city')
def user_selects_arrival(context):
    time.sleep(3)
    context.Control_Functions.data_input(xpaths.tocity,"London - Heathrow Apt, United Kingdom")
    time.sleep(4)
    context.Util.wait_click(xpaths.airport_selector)

@When(u'the user selects the arrival date')
def user_selects_arrival_date(context):

    context.Control_Functions.select_dates(22)
    time.sleep(3)
    
@When(u'the user selects passenger details')
def passenger_details(context):

    context.Control_Functions.click_button(xpaths.flight_traveller)
    context.Control_Functions.click_button(xpaths.adults)
    context.Control_Functions.click_button(xpaths.children)
    context.Control_Functions.click_button(xpaths.travel_class)
    time.sleep(2)
    context.Control_Functions.click_button(xpaths.traveller_apply)
    time.sleep(2)

@When(u'the user selects Britsih Airways')
def user_selects_British_Airways(context):  
    #context.Control_Functions.click_button("(//span[@class='linkText pointer'])[2]")
    context.Control_Functions.click_button(xpaths.more_airlines)
    context.Control_Functions.click_button(xpaths.british_airways)
    time.sleep(5)

@When(u'the user clicks on the flight Details')
def user_clicks_flight_details(context): 
    context.Control_Functions.click_button(xpaths.view_flight_details) 
    time.sleep(5)
    checkIn = context.Control_Functions.get_text(xpaths.checkin) #gets chekinbaggage if present will not work if not present
    cabin = context.Control_Functions.get_text(xpaths.cabin) #gets cabinbaggage if present will not work if not present
    #cabin=context.driver.find_element(By.XPATH,"(//span[@class='baggageInfoText darkText'])[3]").text
    try:
        assert checkIn[0:2]=='46', "Cabin baggage is not 14"
    except:
        print(f"Cabin luggage is {checkIn[0:2]}")
    try:
        assert cabin[0:2]=='14', "Cabin baggage is not 14"
    except AssertionError:
        print(f"Cabin luggage is {cabin[0:2]}")
    time.sleep(4)

@Then(u'the user clicks on the view prices button')
def user_clicks_view_prices(context):  
    context.Control_Functions.click_button(xpaths.view_round_fare)
    time.sleep(5)
    original_window = context.driver.current_window_handle
    context.Control_Functions.click_button(xpaths.round_continue)
    time.sleep(5)    
    for window_handle in context.driver.window_handles:
        if window_handle != original_window:
            context.driver.switch_to.window(window_handle)
            break

    faresummary = context.Control_Functions.find_ele(xpaths.fare_summary)
    assert faresummary.is_displayed(), "faresummary is not displayed"
    flight_name = context.Control_Functions.find_ele(xpaths.flight_name)
    assert flight_name.is_displayed(), "flightname is not displayed"