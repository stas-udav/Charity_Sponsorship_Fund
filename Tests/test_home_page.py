from Pages.home_page import HomePage
from selenium import webdriver
import pytest

# Create a new browser instance 
driver = webdriver.Chrome()
@pytest.mark.parametrize("url", ["https://warvictimsfund.com/"])
def test_open_page(url):
     # Full screen browser    
        driver.maximize_window()   
        # Open the website  
        driver.get(url)
