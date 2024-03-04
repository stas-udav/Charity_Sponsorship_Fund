#! /usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import logging
import re
import time
import json
from Pages.config_charity import *


class BasePage:
    def __init__(self, driver) -> None:
        self.driver = driver

    # Header and footer cross all pages 
    def find_header_footer(self):    
        header = self.driver.find_element(By.XPATH,xpath_header)
        footer = self.driver.find_element(By.XPATH, xpath_footer)    
        return header, footer
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
        wait.until(lambda driver: driver.find_element(By.XPATH, xpath_footer))      
        # _, footer = self.find_header_footer()
        elements = self.driver.find_elements(By.XPATH, xpath_footer)
        assert len(elements) == 1, "Error - page not downloaded"
        # assert self.driver.find_element(By.XPATH, '//section[@class="footer w-section--footer w-section--no-v-padding"]'), "Error - page not downloaded"

    # Payment button
    def donate_button(self):
        # Find all payment buttons on the page
        donate_buttons = self.driver.find_elements(By.XPATH, xpath_donate)
        return donate_buttons
    
    # Social media icon\links check
    def social_media(self):
        # Find all social media icons
        social_media_icons = self.driver.find_elements(By.XPATH, xpath_social_media_icon)

        # Create a list of social media icons
        social_media_list = []
        for icon in social_media_icons:
            social_media_list.append(icon.get_attribute("href"))

        # Print the list of social media icons separated by new line
        print("\n".join(social_media_list))

    def report_json(self, file_name, report_list):
        # getting data and time when report will be created
        now = time.strftime("%Y-%m-%d_%H-%M")
        new_filename = f"{reports_directory}/{now}_{file_name}"
        with open(new_filename,"w") as json_file:
            json.dump(report_list, json_file) 

    # Ensure the logo redirects to the homepage
    def click_logo(self):
        self.driver.find_element(By.XPATH, xpath_logo).click()
        current_url = self.driver.current_url
        assert current_url == home_url, "expected url {}, received url {}.".format(home_url, current_url)
        print(current_url)

    # Find element
    def find_element(self, xpath):
        wait = WebDriverWait(self.driver, 3)
        wait.until(lambda driver: driver.find_element(By.XPATH, xpath))  
        element = self.driver.find_element(By.XPATH, xpath)
        return element