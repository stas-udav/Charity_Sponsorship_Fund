#! /usr/bin/env python3
from functions import *

# Create a new browser instance 
driver = webdriver.Chrome()
open_website(driver, "https://warvictimsfund.com/donate")

payment_redirect(driver)

time.sleep(2)