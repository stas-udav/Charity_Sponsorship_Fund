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
    def input_field(self, field_data_dict):
        # argument it's a dictionary of date for all 
        # field, should be like 
        # input_data = {
        #     "name": "John Doe",
        #     "phone": "1234567890",
        #     "email": "johndoe@example.com",
        #     "message": "This is my message",
        #  }
        self.name_input = self.find_input_field ("Your Name*", field_data_dict["name"]) 
        self.phone_input = self.find_input_field ("Phone number*", field_data_dict["phone"])
        self.email_input = self.find_input_field ("Email*", field_data_dict["email"])
        self.message_input = self.find_input_field ("Your message", field_data_dict["message"])
    
        