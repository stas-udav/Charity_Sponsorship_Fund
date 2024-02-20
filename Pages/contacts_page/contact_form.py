#! /usr/bin/env python3
# from .Tests.functions import *
from Pages.base_page import *
class ContactForm(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Submit button method
    def scroll_to_submit(self):   
        self.find_element(By.XPATH, '//button[@type="submit"]').click()    
        self.driver.execute_script("arguments[0].scrollIntoView();", (By.XPATH, '//button[@type="submit"]'))
    
    # Create a new browser instance   
    def open(self, url):        
        # Full screen browser    
        self.driver.maximize_window()   
        # Open the website  
        self.driver.get(url) 

    # Check if page loaded 
    def loading_check(self):
        wait = WebDriverWait(self.driver, 3)
        wait.until(lambda driver: driver.find_element(By.XPATH, '//section[@class="footer w-section--footer w-section--no-v-padding"]'))      
        assert self.driver.find_element(By.XPATH, '//section[@class="footer w-section--footer w-section--no-v-padding"]'), "Error - page not downloaded "
    
    # Send data to the input field
    def input_field(self, xpath):
        # argument it's a dictionary of date for all 
        # field, should be like 
        # input_data = {
        #     "name": "John Doe",
        #     "phone": "1234567890",
        #     "email": "johndoe@example.com",
        #     "message": "This is my message",
        #  }
        # field_data_dict["message"] - dict input
        field = self.driver.find_element (By.XPATH, xpath)
        # name_input_field = self.driver.find_element (By.XPATH, "//input[@placeholder='Your Name*']") 
        # phone_input_field = self.driver.find_element (By.XPATH,"//input[@placeholder='Phone number*']")
        # email_input_field = self.driver.find_element (By.XPATH,"//input[@placeholder='Email*']")
        # message_input_field = self.driver.find_element (By.XPATH,"//textarea[@class='w-form__input w-form__input--textarea ui-input ui-input--size-md']")
        # return(name_input_field, phone_input_field, email_input_field, message_input_field)
        return(field)
        