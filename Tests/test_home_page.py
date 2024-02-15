from Pages.home_page import HomePage
from selenium import webdriver
import pytest
import allure

# Create a new browser instance (fixture "module" used for creating 1 browser
#                                instance for all test functions)
@pytest.fixture(scope="module")
def driver():
    # Setup
    driver = webdriver.Chrome()
    yield driver
    # Teardown
    driver.quit()

@pytest.mark.parametrize("url", ["https://warvictimsfund.com/"])
def test_open_page(url, driver):
   homepage = HomePage(driver)
   # Full screen browser    
   homepage.driver.maximize_window() 
   # Open the website  
   homepage.driver.get(url)

@allure.step("loading_check")
def test_loading_check(driver):
   homepage = HomePage(driver)
   homepage.loading_check()   
   
# Ensure the logo redirects to the homepage
def test_logo_redirect(driver):
   homepage = HomePage(driver)
   homepage.click_logo()

# Social media icon\links check   
def test_social_media(driver):
   homepage = HomePage(driver)
   homepage.social_media()

         