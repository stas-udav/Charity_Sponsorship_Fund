#! /usr/bin/env python3
from functions import *
from classes import *

# Getting date ! 
now = datetime.datetime.now()

logging.info("Date: %s", now.strftime("%Y-%m-%d %H:%M"))
test_data = [["Test", "1234", "tes@sd.com"],
            ["Test", "ok", "1234tes@sd.com"],
            ["Test", "1234", "1234"],
            ["1234", "1234", "tes@sd.com"],
]
for test in test_data:
    # Create a new browser instance 
    driver = webdriver.Chrome()
    open_website(driver, "https://warvictimsfund.com/conacts")

    # Send a message through the feedback form  with valid data

    name = find_input_field (driver, "Your Name*", test[0]) 
    phone = find_input_field (driver, "Phone number*", test[1])
    # assert re.match("[a-zA-Z]+", phone.get_attribute("value")) is None
    try:
        assert re.match("^[0-9]+", phone.get_attribute("value")) is not None
    except AssertionError:
        logging.error(f"ERROR: Submitted with letters in phone field: {test[1]}", exc_info=True)
        print("ERROR")        
    email = find_input_field (driver, "Email*", test[2])
    # # Click on submit button
    driver.execute_script("window.scrollTo(0, 500);")
    time.sleep(0.2)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()  
    time.sleep(2)
    try:
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//*[text()='Thank you!']")))
        assert True, "Submitted"
    except TimeoutException:
        logging.info("Element not found")
        logging.info("Name: %s", test[0])
        logging.info("Phone: %s", test[1])
        logging.info("Email: %s", test[2] )
        print("Error")
    driver.quit()
