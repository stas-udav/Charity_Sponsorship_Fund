#! /usr/bin/env python3
from Pages.base_page import *
from selenium import webdriver

class AboutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)  

    # Check if email link is present and correct 
    # def check_email(self, xpath):
    #     email = self.find_element(By.XPATH, xpath)
    #     return email        