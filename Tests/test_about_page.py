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

# Checking if e-mail is present and clickable
@pytest.mark.parametrize("xpath", ['//a[@href="mailto:HELP@WARVICTIMSFUND.COM"]'])
def test_email(xpath, driver):
    about_page = AboutPage(driver)
    email = about_page.find_element(xpath)
    driver.execute_script("arguments[0].scrollIntoView(true);", email)
    email_value = email.text
    assert email_value == "HELP@WARVICTIMSFUND.COM"
    allure.attach(driver.get_screenshot_as_png(), name="email", attachment_type=allure.attachment_type.PNG)
    # assert email.click()
    
# Checking if phone is present and clickable
@pytest.mark.parametrize("xpath", ['//a[@href="tel:+37067045284"]'])
def test_phone_present(xpath, driver):    
    about_page = AboutPage(driver)
    phone = about_page.find_element(xpath)
    phone_text = phone.text
    assert phone_text == "+ 37067045284"
    print(phone_text)
    assert phone.click
    allure.attach(driver.get_screenshot_as_png(), name="Phone", attachment_type=allure.attachment_type.PNG)
# Checking if business address is correct
@pytest.mark.parametrize("xpath", ['//span[@style="font-size:18px" and contains(text(), "ŽIRNIŲ STR. 10, VILNIUS 02120, LITHUANIA")]'])
def test_address(xpath, driver):
    about_page = AboutPage(driver)
    address = about_page.find_element(xpath)
    address_value = address.text
    assert address_value == "ŽIRNIŲ STR. 10, VILNIUS 02120, LITHUANIA"
    allure.attach(driver.get_screenshot_as_png(), name="address", attachment_type=allure.attachment_type.PNG)

    print(address_value) 
    