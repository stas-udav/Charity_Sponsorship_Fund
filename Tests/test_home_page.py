from Pages.home_page import HomePage
from selenium import webdriver
import pytest
import time
from openpyxl import Workbook

# Create a new browser instance 
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

def test_loading_check(driver):
    homepage = HomePage(driver)
    homepage.loading_check()