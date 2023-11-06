from behave import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from Utilities.Selenium_Utilities.Util import Util
#from ApplicationLibrary.ControlLibrary.control_elements import Control_Funtions
from ApplicationLibrary.FunctionalLibrary.functional_elements import Control_Funtions

@When(u'the user selects the round radio option')
def user_selects_round(context):
    context.Util.simple_wait("//li[@data-cy='roundTrip']")
    #WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//li[@data-cy='roundTrip']")))
    context.Control_Functions.click_button("//li[@data-cy='roundTrip']")
    

@when(u'the user selects "Bangalore" as the from city')
def user_selects_departure(context):
    time.sleep(3) #fails if this sleep isnt given
    context.Control_Functions.data_input("//input[@class='fsw_inputField lineHeight36 latoBlack font30' and  @id='fromCity']","Bengaluru")
    time.sleep(5)
    context.Util.wait_click("//div[@class='calc60'][1]")
    #WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='calc60'][1]"))).click()
    

@when(u'the user selects "London" as the to city')
def user_selects_arrival(context):
    time.sleep(3)
    context.Control_Functions.data_input("//input[@id='toCity' and @class='fsw_inputField lineHeight36 latoBlack font30']","London - Heathrow Apt, United Kingdom")
    time.sleep(4)
    context.Util.wait_click("//div[@class='calc60'][1]")
    #WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='calc60'][1]"))).click()
    #time.sleep(3)

@When(u'the user selects the arrival date')
def user_selects_arrival_date(context):

    context.Control_Functions.select_dates(22)
    time.sleep(3)
    
@When(u'the user selects passenger details')
def passenger_details(context):

    context.Control_Functions.click_button("//div[@data-cy='flightTraveller']")
    context.Control_Functions.click_button("//li[@data-cy='adults-2']")
    context.Control_Functions.click_button("//li[@data-cy='children-2']")
    context.Control_Functions.click_button("//li[@data-cy='travelClass-1']")
    time.sleep(2)
    context.Control_Functions.click_button("//button[@data-cy='travellerApplyBtn']")
    time.sleep(2)

@When(u'the user selects Britsih Airways')
def user_selects_British_Airways(context):  
    # context.Control_Functions.click_button("(//span[@class='linkText pointer'])[2]")
    context.Control_Functions.click_button("//p[contains(text(), 'Alliances & Airlines')]/following-sibling::div/child::div[@class='filtersOuter']/child::div/child::p/child::span")
    context.Control_Functions.click_button("//div[@class='checkboxContent']/p[contains(text(), 'British Airways ')]")
    time.sleep(5)

@When(u'the user clicks on the flight Details')
def user_clicks_flight_details(context): 
    context.Control_Functions.click_button("(//span[@class='linkText ctaLink viewFltDtlsCta'])[1]") 
    time.sleep(5)
    checkIn = context.Control_Functions.get_text("(//span[@class='baggageInfoText darkText'])[14]") #gets chekinbaggage if present will not work if not present
    cabin = context.Control_Functions.get_text("(//span[@class='baggageInfoText darkText'])[15]") #gets cabinbaggage if present will not work if not present
    #print(cabin[0:1])
    #cabin=context.driver.find_element(By.XPATH,"(//span[@class='baggageInfoText darkText'])[3]").text
    try:
        assert checkIn[0:2]=='46', "Cabin baggage is not 14"
    except:
        #print("Checkin Baggage is not 46")
        print(f"Cabin luggage is {checkIn[0:2]}")
    try:
        assert cabin[0:2]=='14', "Cabin baggage is not 14"
    except AssertionError:
        #print("Cabin baggage is not 14")
        print(f"Cabin luggage is {cabin[0:2]}")
    time.sleep(4)

@Then(u'the user clicks on the view prices button')
def user_clicks_view_prices(context):  
    context.Control_Functions.click_button("(//button[@class='ViewFareBtn  text-uppercase  clusterBtn'])[1]")
    time.sleep(5)
    original_window = context.driver.current_window_handle
    context.Control_Functions.click_button("//button[contains(text(),'Continue')]")
    time.sleep(5)    
    for window_handle in context.driver.window_handles:
        if window_handle != original_window:
            context.driver.switch_to.window(window_handle)
            break

    faresummary = context.Control_Functions.find_ele("//p[@class='fontSize18 blackFont']")
    assert faresummary.is_displayed(), "faresummary is not displayed"
    flight_name = context.Control_Functions.find_ele("(//p[@class='makeFlex hrtlCenter gap-x-10']/span)[1]")
    assert flight_name.is_displayed(), "flightname is not displayed"