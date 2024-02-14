from Pages.about_page import AboutPage
from selenium import webdriver
import pytest
import allure
import time
# Create a new browser instance 
@pytest.fixture(scope="module")
def driver():
    # Setup
    driver = webdriver.Chrome()
    yield driver
    # Teardown
    driver.quit()

@pytest.mark.parametrize("url", ["https://warvictimsfund.com/about-us"])
def test_open_page(url, driver):
   about_page = AboutPage(driver)
   # Full screen browser    
   about_page.driver.maximize_window() 
   # Open the website  
   about_page.driver.get(url)

@pytest.mark.parametrize("xpath", ['//a[@href="mailto:HELP@WARVICTIMSFUND.COM"]'])
def test_email(xpath, driver):
    about_page = AboutPage(driver)
    test_email = about_page.find_element(xpath)
    driver.execute_script("arguments[0].scrollIntoView(true);", test_email)
    test_email.click()
    
