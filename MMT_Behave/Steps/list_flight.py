from behave import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.Selenium_Utilities.Util import Util
#from ApplicationLibrary.ControlLibrary.control_elements import Control_Funtions
from ApplicationLibrary.FunctionalLibrary.functional_elements import Control_Funtions

@when(u'the user selects the one-way radio option')
def user_selects_oneway(context):
    context.Util.simple_wait("//li[@data-cy='oneWayTrip']")
    #WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//li[@data-cy='oneWayTrip']")))
    context.Control_Functions.click_button("//li[@data-cy='oneWayTrip']")

@when(u'the user selects "Delhi" as the from city')
def user_selects_city(context):
    
    time.sleep(3) #fails if this sleep isnt given
    context.Control_Functions.data_input("//input[@class='fsw_inputField lineHeight36 latoBlack font30' and  @id='fromCity']","New Delhi")
    time.sleep(3)
    context.Util.wait_click("//div[@class='calc60'][1]")
    #WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='calc60'][1]"))).click()
    

@when(u'the user selects "Bangalore" as the to city')
def user_selects_city(context):
    
    context.Control_Functions.data_input("//input[@id='toCity' and @class='fsw_inputField lineHeight36 latoBlack font30']","Bengaluru")
    time.sleep(3)
    context.Util.wait_click("//div[@class='calc60'][1]")
    #WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='calc60'][1]"))).click()
    time.sleep(3)

@when(u'the user selects the departure date')
def user_selects_date(context):

    context.Control_Functions.select_dates(15)
    time.sleep(3)

@when(u'the user clicks on the Search button')
def step_user_selects_search(context):

    context.Control_Functions.click_button("//a[@class='primaryBtn font24 latoBold widgetSearchBtn ']")
    time.sleep(15) # long wait needed because of error in loading site
    context.Control_Functions.click_button("//span[@class='bgProperties icon20 overlayCrossIcon']")
    time.sleep(10)
    #used to handle a random pop up that comes

@then(u'the user captures the flight names')
def step_user_details(context):
    flights= context.Control_Functions.find_multiple("//p[contains(@class, 'airlineName')]")
    flight_details= context.Control_Functions.find_multiple("//p[contains(@class, 'fliCode')]")
    
    with open('list.txt', 'w') as l:
        for i in range (len(flight_details)):
           l.write(flights[i].text +" - "+flight_details[i].text + "\n")