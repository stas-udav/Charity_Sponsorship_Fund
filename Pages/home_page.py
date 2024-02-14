#! /usr/bin/env python3
from Pages.base_page import *
from selenium import webdriver

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)  

