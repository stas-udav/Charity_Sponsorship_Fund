#! /usr/bin/env python3
from base_page import *
from selenium import webdriver

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
     


#     home_page = HomePage(webdriver.Chrome())
#     HomePage.open("https://warvictimsfund.com/")

#     #! /usr/bin/env python3
# from base_page import BasePage
# from selenium import webdriver

# class HomePage(BasePage):
#     def __init__(self, driver):
#         super().__init__(driver)

#     def open_home_page(self, url):
#         self.open(url)

# if __name__ == "__main__":
#     driver = webdriver.Chrome()
#     home_page = HomePage(driver)
#     home_page.open_home_page("https://warvictimsfund.com/")
