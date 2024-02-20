from Pages.contacts_page.contact_form import ContactForm
from selenium import webdriver
import pytest
import allure
import time
import re
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
        "phone": "sdfsfsdf35353",
        "email": "johndoe@example.com",
        "message": "This is my message"
    }])
def test_input(field_data_dict, driver):
    contact_page = ContactForm(driver)
    input_name = contact_page.input_field("//input[@placeholder='Your Name*']")
    input_name.send_keys(field_data_dict["name"])
    value_name = input_name.get_attribute("value")
    # Input name field contains letters   
    allure.attach(driver.get_screenshot_as_png(), name="input_name_field", attachment_type=allure.attachment_type.PNG)
    assert value_name is not None and re.match(r'\D+', value_name)    
    input_phone = contact_page.input_field("//input[@placeholder='Phone number*']")
    input_phone.send_keys(field_data_dict["phone"])
    value_phone = input_phone.get_attribute("value")
    # Input phone field contains digits and/or "+"
    allure.attach(driver.get_screenshot_as_png(), name="input_phone_field", attachment_type=allure.attachment_type.PNG)
    assert value_phone is not None and re.match(r'^\+?\d+$', value_phone) and not re.search(r'[a-zA-Z]', value_phone), "Phone contains letter or empty"
    # Input email field contains letters and "@"  
    



