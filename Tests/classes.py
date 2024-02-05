#! /usr/bin/env python3
from functions import *

class ReportsPage:
    def __init__(self, driver):
        self.driver = driver
    def open(self):
        # Create a new browser instance      
        self.driver.maximize_window() # Full screen browser       
        self.driver.get("https://warvictimsfund.com/reports") # Open the website
    def loading_check(self):
        time.sleep(1)
        # wait = WebDriverWait(self.driver, 3) 
        # # Wait for the page to load
        # wait.until(lambda driver: driver.find_element(By.XPATH, '//section[@class="footer w-section--footer w-section--no-v-padding"]'))
        assert self.driver.find_element(By.XPATH, '//section[@class="footer w-section--footer w-section--no-v-padding"]'), "Error - page not downloaded "

