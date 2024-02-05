#! /usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver) -> None:
        self.driver = driver
        # Header and footer cross all pages 
        self.header = self.driver.find_element(By.XPATH, '//div[@class="w-section__inner section__inner_16_"]')
        self.footer = self.driver.find_element(By.XPATH, '//section[@class="footer w-section--footer w-section--no-v-padding"]')

    # Create a new browser instance   
    def open(self, url):        
        # Full screen browser    
        self.driver.maximize_window()   
        # Open the website  
        self.driver.get(url)

    # Close browser instance
    def close(self):
        self.driver.quit()

    # Scroll
    def scroll(self, horizont, vert):
        self.driver.execute_script(f"window.scrollTo({horizont}, {vert});")

    # Check if page loaded 
    def loading_check(self):
        wait = WebDriverWait(self.driver, 3)
        wait.until(lambda driver: driver.find_element(By.XPATH, '//section[@class="footer w-section--footer w-section--no-v-padding"]'))      
        assert self.driver.find_element(By.XPATH, '//section[@class="footer w-section--footer w-section--no-v-padding"]'), "Error - page not downloaded"

    