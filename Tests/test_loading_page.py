#! /usr/bin/env python3
from functions import *

# Create a new browser instance 
driver = webdriver.Chrome()

# Verify that the homepage loads without errors and link is correct
url_list = ["https://warvictimsfund.com/", "https://warvictimsfund.com/about-us", "https://warvictimsfund.com/campaigns", "https://warvictimsfund.com/blog", 
"https://warvictimsfund.com/reports", "https://warvictimsfund.com/conacts", "https://warvictimsfund.com/volunteer", "https://warvictimsfund.com/partners",
"https://warvictimsfund.com/donate", "https://warvictimsfund.com/policy-priorities", "https://warvictimsfund.com/donate"]
url_error_dict = {}
for url in url_list:
    open_url = open_website(driver, url)
    if url == open_url:
        print("Page downloaded correctly", url)
    else:
        url_error_dict[url] = driver.current_url
        print("Error")
        report_json(driver, "url_error_report.json", url_error_dict)
time.sleep(0.5) 

# Ensure the logo redirects to the homepage
click_logo(driver,"https://warvictimsfund.com/policy-priorities")

# Social media check
social_media(driver, "https://warvictimsfund.com/")

