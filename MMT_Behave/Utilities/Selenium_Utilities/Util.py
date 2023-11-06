from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Util:
    def __init__(self, driver):
        self.driver = driver

    def wait_click(self,xpath):
        return WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,xpath))).click()
    
    def simple_wait(self,xpath):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,xpath)))
    
    def frame_switch(self,xpath):
        return  WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,xpath)))
    
    def return_frame(self):
        return self.driver.switch_to.default_content()
