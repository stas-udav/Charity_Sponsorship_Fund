from Pages.contacts_page.contact_form import ContactForm
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

@pytest.mark.parametrize("url", ["https://warvictimsfund.com/conacts"])
def test_open_page(url, driver):
   contact_page = ContactForm(driver)
   # Full screen browser    
   contact_page.driver.maximize_window() 
   # Open the website  
   contact_page.driver.get(url)

@pytest.mark.parametrize("field_data_dict", [{
        "name": "John Doe",
        "phone": "1234567890",
        "email": "johndoe@example.com",
        "message": "This is my message"
    }])
def test_input(field_data_dict):
    contact_page = ContactForm(driver)
    contact_page.input_field(field_data_dict)
