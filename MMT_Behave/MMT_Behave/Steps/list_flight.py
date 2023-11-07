from behave import *
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.Selenium_Utilities.Util import Util
from ApplicationLibrary.ControlLibrary.control_elements import xpath_store
from ApplicationLibrary.FunctionalLibrary.functional_elements import Control_Funtions

xpaths=xpath_store()

@when(u'the user selects the one-way radio option')
def user_selects_oneway(context):

    context.Util.simple_wait(xpaths.oneway)
    context.Control_Functions.click_button(xpaths.oneway)

@when(u'the user selects "Delhi" as the from city')
def user_selects_city(context):
    
    time.sleep(3) #fails if this sleep isnt given
    context.Control_Functions.data_input(xpaths.fromcity,"New Delhi")
    time.sleep(3)
    context.Util.wait_click(xpaths.airport_selector)
    

@when(u'the user selects "Bangalore" as the to city')
def user_selects_city(context):
    
    context.Control_Functions.data_input(xpaths.tocity,"Bengaluru")
    time.sleep(3)
    context.Util.wait_click(xpaths.airport_selector)
    time.sleep(3)

@when(u'the user selects the departure date')
def user_selects_date(context):

    context.Control_Functions.select_dates(15)
    time.sleep(3)

@when(u'the user clicks on the Search button')
def step_user_selects_search(context):

    context.Control_Functions.click_button(xpaths.search)
    time.sleep(15) # long wait needed because of error in loading site
    context.Control_Functions.click_button(xpaths.overlay_cross)
    time.sleep(10)
    #used to handle a random pop up that comes

@then(u'the user captures the flight names')
def step_user_details(context):
    
    flights= context.Control_Functions.find_multiple(xpaths.airline_name)
    flight_details= context.Control_Functions.find_multiple(xpaths.airline_code)
    
    save_path = "C:\\Users\\Yashodhara.Somayaji\\Desktop\\FE assessment\\MMT_Behave\\TestResults"
    full_path = os.path.join(save_path, "list.txt") 
    with open(full_path, 'w') as l:
        for i in range (len(flight_details)):
           l.write(flights[i].text +" - "+flight_details[i].text + "\n")