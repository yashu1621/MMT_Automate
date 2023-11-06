
from behave import *
import time
# from selenium.webdriver.chrome.options import Options
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
    #context.driver.switch_to.default_content() 
    context.Control_Functions.click_button(xpaths.close_modal_login)
    time.sleep(3)


@then('User validates the URL is "{expected_url}"')
def validate_url(context, expected_url):
    context.Control_Functions.validate_url(expected_url)


 
@then('User validates the presence of the MMT logo')
def validate_logo_element(context):
    context.Control_Functions.validate_logo("//img[@src='//imgak.mmtcdn.com/pwa_v3/pwa_hotel_assets/header/mmtLogoWhite.png']")
    # logo_element = context.driver.find_element(By.XPATH, "//img[@src='//imgak.mmtcdn.com/pwa_v3/pwa_hotel_assets/header/mmtLogoWhite.png']")
    # assert logo_element.is_displayed(), "logo is not displayed on the page"

@then(u'the user validates the title is present')
def validate_title(context):
    expected_title = "MakeMyTrip - #1 Travel Website 50% OFF on Hotels, Flights & Holiday"
    actual_title = context.driver.title
    context.Control_Functions.validate_title(expected_title,actual_title)
    # assert actual_title in expected_title, f"Expected title: {expected_title}, Actual title: {actual_title}"


@then(u'the user validates the Login button is present')
def validate_login_button(context):
    context.Control_Functions.validate_login("//li[@data-cy='account']")
    # login_element=context.driver.find_element(By.XPATH, "//li[@data-cy='account']")
    # assert login_element.is_displayed(), "Login button is not displayed on the page"
    # context.driver.quit()


# @when(u'the user enters invalid username and password')
# def step_user_enters_invalid_details(context):
#     WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//li[@data-cy='account']"))).click()
#     # context.driver.find_element(By.XPATH, "//li[@data-cy='account']").click()
#     # time.sleep(3)
#     #context.driver.implicity_wait(3)
#     WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//input[@id='username']")))
#     context.driver.find_element(By.XPATH,"//input[@id='username']").send_keys("testa@gmail.com")
#     # context.driver.find_element(By.XPATH, "//input[@class='font14 fullWidth' and @id='username']").send_keys("test@gmail.com")
#     # time.sleep(3)
#     #WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[@data-cy='contiuneBtn']"))).click()
#     context.driver.find_element(By.XPATH, "//button[@class='capText font16']").click()
#     #time.sleep(3)
#     WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//input[@id='password']")))
#     context.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("12345678")
#     # context.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("12345678")
#     # time.sleep(3)
#     WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[@data-cy='login']"))).click()
#     # context.driver.find_element(By.XPATH, "//button[@class='capText font16']").click()
#     #time.sleep(3)
#     WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//span[@data-cy='serverError']")))
#     #context.driver.find_element(By.XPATH, "//span[@data-cy='serverError']").is_displayed()
#     context.driver.find_element(By.XPATH,"//span[@data-cy='CommonModal_3']").click()
#     time.sleep(3)
# @when(u'the user enters valid username and password')
# def step_user_enters_valid_details(context):
#     WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//li[@data-cy='account']"))).click()
#     # context.driver.find_element(By.XPATH, "//li[@data-cy='account']").click()
#     # time.sleep(3)
#     WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//input[@id='username']")))
#     context.driver.find_element(By.XPATH,"//input[@id='username']").send_keys("somayaji.yashodhara@gmail.com")
#     # context.driver.find_element(By.XPATH, "//input[@class='font14 fullWidth' and @id='username']").send_keys("somayaji.yashodhara@gmail.com")
#     # time.sleep(3)
#     context.driver.find_element(By.XPATH, "//button[@class='capText font16']").click()
#     #time.sleep(3)
#     WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//input[@id='password']")))
#     context.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Shell@1234")
#     #time.sleep(3)
#     WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[@data-cy='login']"))).click()
#     # context.driver.find_element(By.XPATH, "//button[@class='capText font16']").click()
#     # time.sleep(3)
#     ele=WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//input[@id='otp']")))
#     assert ele.is_displayed(), "otp is not displayed"
#     time.sleep(3)
#     context.driver.find_element(By.XPATH,"//span[@data-cy='CommonModal_3']").click()
#     time.sleep(5)
#     context.driver.find_element(By.XPATH, "//span[@data-cy='closeModal']").click()
#     #context.driver.find_element(By.XPATH, "//div[@class='imageSlideContainer']").click()
#     time.sleep(5)


# @when(u'the user selects the one-way radio option')
# def step_user_selects_oneway(context):
#     context.driver.find_element(By.XPATH,"//li[@data-cy='oneWayTrip']").click()
#     time.sleep(3)

# @when(u'the user selects "Delhi" as the from city')
# def step_user_selects_delhi(context):
#     # context.driver.find_element(By.XPATH,"//input[@data-cy='fromCity']").click()
#     # time.sleep(3)
#     # context.driver.find_element(By.XPATH,"//p[@class='font14 appendBottom5 blackText'])[1]").click()
#     # time.sleep(3)
#     context.driver.find_element(By.XPATH,"//input[@class='fsw_inputField lineHeight36 latoBlack font30' and  @id='fromCity']").send_keys('New Delhi')
#     time.sleep(3)
#     context.driver.find_element(By.XPATH,"//li[@id='react-autowhatever-1-section-0-item-0']").click()
#     time.sleep(3)

# @when(u'the user selects "Bangalore" as the to city')
# def step_user_selects_bangalore(context):
#     # time.sleep(3)
#     # context.driver.find_element(By.XPATH,"//input[@id='toCity' and @class='fsw_inputField lineHeight36 latoBlack font30']").send_keys('Bengaluru')
#     # time.sleep(3)
#     # context.driver.find_element(By.XPATH,"//li[@id='react-autowhatever-1-section-0-item-0']").click()
#     # time.sleep(3)
#     context.driver.find_element(By.XPATH,"//input[@id='toCity' and @class='fsw_inputField lineHeight36 latoBlack font30']").send_keys('Bengaluru')
#     time.sleep(3)
#     #context.driver.find_element(By.XPATH,"//li[@id='react-autowhatever-1-section-0-item-0']").click()
#     context.driver.find_element(By.XPATH,"//div[@class='calc60'][1]").click()
#     time.sleep(3)

# @when(u'the user selects the departure date 15 days from the current date')
# def step_user_selects_date(context):
    
#     current_date = datetime.now() 
#     future_date = current_date + timedelta(days=15)
#     fdate=future_date.strftime('%a %b %d %Y')
#     s1=f"//div[@aria-label='{fdate}']"
#     context.driver.find_element(By.XPATH,f'{s1}').click()
#     time.sleep(3)

# @when(u'the user clicks on the Search button')
# def step_user_selects_search(context):
#     context.driver.find_element(By.XPATH,"//a[@class='primaryBtn font24 latoBold widgetSearchBtn ']").click()
#     time.sleep(15)
#     context.driver.find_element(By.XPATH,"//span[@class='bgProperties icon20 overlayCrossIcon']").click()
#     time.sleep(10)
#     #used to handle a random pop up that comes
# @then(u'the user captures the flight names')
# def step_user_details(context):
#     flights = context.driver.find_elements(By.XPATH,"//p[contains(@class, 'airlineName')]")
#     flight_details=context.driver.find_elements(By.XPATH,"//p[contains(@class, 'fliCode')]")
#     # flights = context.driver.find_elements(By.XPATH,"//div[@class='appendBottom15 ']/div/div[2]/div/div/div/p[1]")
#     # flight_details=context.driver.find_elements(By.XPATH,"//div[@class='appendBottom15 ']/div/div[2]/div/div/div/p[2]")
#     with open('list.txt', 'w') as l:
#         for i in range (len(flight_details)):
#            l.write(flights[i].text +" - "+flight_details[i].text + "\n")
    

# @when(u'the user selects flights with lowest price and less travel time')
# def step_user_selcts_flight(context):
#     context.driver.find_element(By.XPATH,"(//input[@id='listingFilterCheckbox'])[1]").click()
#     time.sleep(5)
#     context.driver.find_element(By.XPATH,"//*[contains(text(),'You May Prefer')]").click()
#     time.sleep(5)

# @Then(u'the user Validates the flight name selected in the booking page and Fare Summary')
# def step_user_validates_fare(context):
#     context.driver.find_element(By.XPATH,"(//span[@class='appendRight8'])[1]").click()
#     time.sleep(3)
#     original_window = context.driver.current_window_handle
    
#     context.driver.find_element(By.XPATH,"(//button[@class='button corp-btn latoBlack buttonPrimary fontSize13  '])[1]").click()
#     time.sleep(5)
#     for window_handle in context.driver.window_handles:
#         if window_handle != original_window:
#             context.driver.switch_to.window(window_handle)
#             break
#     faresummary=context.driver.find_element(By.XPATH,"//p[@class='fontSize18 blackFont']")
#     assert faresummary.is_displayed(), "faresummary is not displayed or enabled"
#     flight_name=context.driver.find_element(By.XPATH,"(//p[@class='makeFlex hrtlCenter gap-x-10']/span)[1]")
#     assert flight_name.is_displayed(), "flightname is not displayed or enabled"

# @When(u'the user selects the round radio option')
# def step_user_selects_roundway(context):
#     context.driver.find_element(By.XPATH,"//li[@data-cy='roundTrip']").click()
#     time.sleep(2)

# @when(u'the user selects "Bangalore" as the from city')
# def step_user_selects_bangalore(context):
#     #time.sleep(3)
#     context.driver.find_element(By.XPATH,"//input[@class='fsw_inputField lineHeight36 latoBlack font30' and  @id='fromCity']").send_keys('Bengaluru')
#     time.sleep(5)
#     context.driver.find_element(By.XPATH,"//li[@id='react-autowhatever-1-section-0-item-0']").click()
#     time.sleep(5)

# @when(u'the user selects "London" as the to city')
# def step_user_selects_london(context):
#     #time.sleep(3)
#     # context.driver.find_element(By.XPATH,"//input[@id='toCity' and @class='fsw_inputField lineHeight36 latoBlack font30']").send_keys('London')
#     time.sleep(5)
#     #WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//input[@id='toCity' and @class='fsw_inputField lineHeight36 latoBlack font30']")))
#     #context.driver.implicity_wait(3)
#     context.driver.find_element(By.XPATH,"//input[@id='toCity' and @class='fsw_inputField lineHeight36 latoBlack font30']").send_keys('London')
#     time.sleep(3)
#     context.driver.find_element(By.XPATH,"//li[@id='react-autowhatever-1-section-0-item-0']").click()

#     time.sleep(5)

# @When(u'the user selects the arrival date 7 days from departure date')
# def step_user_selects_arrival_date(context):
#     current_date = datetime.now() 
#     future_date = current_date + timedelta(days=22)
#     fdate=future_date.strftime('%a %b %d %Y')
#     s1=f"//div[@aria-label='{fdate}']"
#     context.driver.find_element(By.XPATH,f'{s1}').click()
#     time.sleep(3)

# @When(u'the user selects passenger details')
# def step_passenger_details(context):
#     context.driver.find_element(By.XPATH,"//div[@data-cy='flightTraveller']").click()
#     time.sleep(2)
#     context.driver.find_element(By.XPATH,"//li[@data-cy='adults-2']").click()
#     time.sleep(2)
#     context.driver.find_element(By.XPATH,"//li[@data-cy='children-2']").click()
#     time.sleep(2)
#     context.driver.find_element(By.XPATH,"//li[@data-cy='travelClass-1']").click()
#     time.sleep(2)
#     context.driver.find_element(By.XPATH,"//button[@data-cy='travellerApplyBtn']").click()
#     time.sleep(2)

# # @When(u'the user clicks on the Search button for british airways')
# # def step_user_searches_britishairways(context):  
# #     context.driver.find_element(By.XPATH,"//a[@class='primaryBtn font24 latoBold widgetSearchBtn ']").click()

# @When(u'the user selects Britsih Airways')
# def step_user_selects_britishairways(context):    
#     context.driver.find_element(By.XPATH,"//p[contains(text(), 'British Airways')]").click()
#     time.sleep(5)
#     # context.driver.find_element(By.XPATH,"(//span[@class='linkText ctaLink viewFltDtlsCta'])[1]").click()
#     # time.sleep(3)

# @When(u'the user clicks on the flight Details')
# def step_user_clicks_flight_details(context):  
#     context.driver.find_element(By.XPATH,"(//span[@class='linkText ctaLink viewFltDtlsCta'])[1]").click()
#     time.sleep(5)
#     checkIn=context.driver.find_element(By.XPATH,"(//span[@class='baggageInfoText darkText'])[2]").text
#     cabin=context.driver.find_element(By.XPATH,"(//span[@class='baggageInfoText darkText'])[3]").text
#     assert checkIn[0:2]=='46',"Checkin Baggage is not 46"
#     assert cabin[0:1]=='7',"Cabin baggage is not 14"
#     time.sleep(4)

# @Then(u'the user clicks on the select button')
# def step_user_clicks_select_button(context):  
#     context.driver.find_element(By.XPATH,"(//button[@class='ViewFareBtn  text-uppercase  clusterBtn'])[1]").click()
#     time.sleep(3)
#     original_window = context.driver.current_window_handle
#     context.driver.find_element(By.XPATH,"//button[contains(text(),'Continue')]").click()
#     time.sleep(3)    
#     for window_handle in context.driver.window_handles:
#         if window_handle != original_window:
#             context.driver.switch_to.window(window_handle)
#             break
#     faresummary=context.driver.find_element(By.XPATH,"//p[@class='fontSize18 blackFont']")
#     assert faresummary.is_displayed(), "faresummary is not displayed"
#     flight_name=context.driver.find_element(By.XPATH,"(//p[@class='makeFlex hrtlCenter gap-x-10']/span)[1]")
#     assert flight_name.is_displayed(), "flightname is not displayed"
   

     