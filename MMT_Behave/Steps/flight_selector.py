from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.Selenium_Utilities.Util import Util
#from ApplicationLibrary.ControlLibrary.control_elements import Control_Funtions
from ApplicationLibrary.FunctionalLibrary.functional_elements import Control_Funtions

@when(u'the user selects flights with lowest price and time')
def user_selects_flight(context):
    
    #context.Util.simple_wait("//input[@id='listingFilterCheckbox'])[1]")
    #WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH,"(//input[@id='listingFilterCheckbox'])[1]")))
    #context.Control_Functions.click_button("(//input[@id='listingFilterCheckbox'])[1]")
    context.Util.simple_wait("//*[contains(text(),'You May Prefer')]")
    #WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//*[contains(text(),'You May Prefer')]")))
    context.Control_Functions.click_button("//*[contains(text(),'You May Prefer')]")

@Then(u'the user Validates the flight name and Fare Summary')
def user_validates_fare(context):
    context.Control_Functions.click_button("(//span[@class='appendRight8'])[1]")
    time.sleep(3)
    original_window = context.driver.current_window_handle
    context.Control_Functions.click_button("(//button[@class='button corp-btn latoBlack buttonPrimary fontSize13  '])[1]")
    time.sleep(5)
    for window_handle in context.driver.window_handles:
        if window_handle != original_window:
            context.driver.switch_to.window(window_handle)
            break
    faresummary = context.Control_Functions.find_ele("//p[@class='fontSize18 blackFont']")
    #faresummary=context.driver.find_element(By.XPATH,"//p[@class='fontSize18 blackFont']")
    assert faresummary.is_displayed(), "faresummary is not displayed"
    flight_name = context.Control_Functions.find_ele("(//p[@class='makeFlex hrtlCenter gap-x-10']/span)[1]")
    #flight_name=context.driver.find_element(By.XPATH,"(//p[@class='makeFlex hrtlCenter gap-x-10']/span)[1]")
    assert flight_name.is_displayed(), "flightname is not displayed"