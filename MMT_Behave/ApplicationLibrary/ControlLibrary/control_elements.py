from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from datetime import datetime, timedelta

# class Control_Funtions:
#     def __init__(self, driver):
#         self.driver = driver

#     def maximize(self):
#         self.driver.maximize_window()

#     def validate_url(self, expected_url):
#         current_url = self.driver.current_url
#         assert current_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {current_url}"

#     def navigate_url(self, url):
#         self.driver.get(url)

#     def validate_logo(self,xpath):
#         logo = self.driver.find_element(By.XPATH, xpath)
#         assert logo.is_displayed(), "logo is not displayed on the page"

#     def validate_title(self,expected_title,actual_title):
#         assert actual_title in expected_title, f"Expected title: {expected_title}, Actual title: {actual_title}"
        
#     def validate_login(self,xpath):
#         login = self.driver.find_element(By.XPATH,xpath)
#         assert login.is_displayed(), "Login button is not displayed on the page"

#     def quit_driver(self):
#         self.driver.quit()


#     def data_input(self,xpath,email):
#         data_in=self.driver.find_element(By.XPATH,xpath)
#         data_in.send_keys(email)

#     def click_button(self,xpath):
#         clk_button=self.driver.find_element(By.XPATH,xpath)
#         clk_button.click()
    
#     def element_displayed(self,xpath):
#         invalid_button=self.driver.find_element(By.XPATH,xpath)
#         assert invalid_button.is_displayed()
    
#     def select_dates(self,dy):
#         current_date = datetime.now() 
#         future_date = current_date + timedelta(days=dy)
#         fdate=future_date.strftime('%a %b %d %Y')
#         s1=f"//div[@aria-label='{fdate}']"
#         self.driver.find_element(By.XPATH,f'{s1}').click()

#     def find_multiple(self,xpath):
#         return self.driver.find_elements(By.XPATH,xpath)
    
#     def find_ele(self,xpath):
#         return self.driver.find_element(By.XPATH,xpath)
    
#     def get_text(self,xpath):
#         return self.driver.find_element(By.XPATH,xpath).text

class xpath_store:
    iframe = "//iframe[@id='webklipper-publisher-widget-container-notification-frame']"
    close_iframe_banner = "//a[@id='webklipper-publisher-widget-container-notification-close-div']"
    close_modal_login = "//span[@data-cy='closeModal']"
   