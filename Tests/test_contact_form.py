from Pages.contacts_page.contact_form import ContactForm
from selenium import webdriver
import pytest
import allure
import time
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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

@allure.suite("Contact Form Tests")
@pytest.mark.parametrize("field_data_dict", [{
        "name": "John Doe",
        "phone": "35353",
        "email": "johndoe@example.com",
        "message": "This is my message"
    },
    {
        "name": "віаіа",
        "phone": "fdgdfg",
        "email": "johnd@oeexample.com",
        "message": "Thапвпge"   
        },
        
    {
        "name": "Stan",
        "phone": "+35635353",
        "email": "johndoeexample.com",
        "message": "Thапвпge"   
        }])
def test_input(field_data_dict, driver):
    contact_page = ContactForm(driver)
    driver.execute_script("window.scrollTo(0, 250);")
    time.sleep(1)    
    with allure.step(f"Input name: {field_data_dict['name']}"):
        input_name = contact_page.input_field("//input[@placeholder='Your Name*']")
        input_name.send_keys(Keys.CONTROL + "a")
        input_name.send_keys(Keys.DELETE)
        input_name.send_keys(field_data_dict["name"])
        value_name = input_name.get_attribute("value")
   
        # Input name field contains letters   
        allure.attach(driver.get_screenshot_as_png(), name="input_name_field", attachment_type=allure.attachment_type.PNG)
        assert value_name is not None and re.match(r'\D+', value_name)
    # input_name.clear()   
    with allure.step(f"Input phone: {field_data_dict['phone']}"):
        # Input phone field contains digits and/or "+"
        input_phone = contact_page.input_field("//input[@placeholder='Phone number*']")
        input_phone.send_keys(Keys.CONTROL + "a")
        input_phone.send_keys(Keys.DELETE)
        # input_phone.clear()
        # WebDriverWait(driver, 3).until(lambda driver: input_phone.get_attribute("value") == "")
        input_phone.send_keys(field_data_dict["phone"])
        value_phone = input_phone.get_attribute("value")
        allure.attach(driver.get_screenshot_as_png(), name="input_phone_field", attachment_type=allure.attachment_type.PNG)
        assert value_phone == field_data_dict["phone"]    
        # assert value_phone is not None and re.match(r'^\+?\d+$', value_phone) and not re.search(r'[a-zA-Z]', value_phone), "Phone contains letter or empty"
    with allure.step(f"Input email: {field_data_dict['email']}"):
        # Input email field contains letters and "@"  
        email_input = contact_page.find_element ("//input[@placeholder='Email*']")
        email_input.send_keys(Keys.CONTROL + "a")
        email_input.send_keys(Keys.DELETE)
        email_input.send_keys(field_data_dict["email"])
        email_value = email_input.get_attribute("value")
        allure.attach(driver.get_screenshot_as_png(), name="email_input_field", attachment_type=allure.attachment_type.PNG)
        assert email_value is not None and re.match(r'^.+@.+\..+$', email_value), "Error - Email missing '@'"
        # email_input.clear()
   
    # Input message field
    driver.execute_script("window.scrollTo(0, 250);")    
    message_input = contact_page.find_element("//textarea[@class='w-form__input w-form__input--textarea ui-input ui-input--size-md']")
    # message_input.clear()
    try:
        message_input.send_keys(Keys.CONTROL + "a")
        message_input.send_keys(Keys.DELETE)
        message_input.send_keys(field_data_dict["message"])
        allure.attach(driver.get_screenshot_as_png(), name="input_massage", attachment_type=allure.attachment_type.PNG)
    except AssertionError:
        print("Send letters not working")
        return None
    driver.execute_script("window.scrollTo(0, 450);")
    # driver.find_element(By.XPATH, "//span[@class='w-form-button__text'][contains(text(), 'Send question ')]").click()
    # time.sleep(1)


