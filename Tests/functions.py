#! /usr/bin/env python3
from libraries import *
log_file_path = r'C:\QA\selenium_test\Charity-and-Sponsorship-Fund\Tests\reports\test_log.txt'
logging.basicConfig(filename=log_file_path, level=logging.INFO) # Logging settings 
reports_directory = r'C:\QA\selenium_test\Charity-and-Sponsorship-Fund\Tests\reports'
def open_website(driver, link):
        # Create a new browser instance      
    driver.maximize_window() # Full screen browser       
    driver.get(link) # Open the website  

# Waiting for the page to load
    try:
        wait = WebDriverWait(driver, 10)     
        # Wait for the page to load
        wait.until(lambda driver: driver.find_element(By.XPATH, '//section[@class="footer w-section--footer w-section--no-v-padding"]'))
         # Return the current URL after successful loading 
        return driver.current_url  
    except TimeoutException:
        print("page loading error")
        return None

# Url check
def url_check(driver,link):
    xpath_selector = f"//a[@href='{link}']" 
    try:
        element = driver.find_element(By.XPATH, xpath_selector)
        print(element, xpath_selector)
        return(element)
    except NoSuchElementException:
        logging.error(f"URL check: Element not found for link {link}.")
        return None
# Report if error
def report_json(driver, file_name, report_list):
    # getting data and time when report will be created
    now = time.strftime("%Y-%m-%d_%H-%M")
    new_filename = f"{reports_directory}/{now}_{file_name}"
    with open(new_filename,"w") as json_file:
        json.dump(report_list, json_file) 

# Ensure the logo redirects to the homepage
def click_logo(driver, url):
    driver.find_element(By.XPATH, "//img[@class='logo-image_HXE image-logo_cI-']").click()
    current_url = driver.current_url
    assert current_url == "https://warvictimsfund.com/", "expected url https://warvictimsfund.com/, received url {}.".format(current_url)
    print(current_url)

# Social media icon\links check
def social_media(driver, url):
    # Find all social media icons
    social_media_icons = driver.find_elements(By.XPATH, "//a[@class='social-icons__icon_1W1']")

    # Create a list of social media icons
    social_media_list = []
    for icon in social_media_icons:
        social_media_list.append(icon.get_attribute("href"))

    # Print the list of social media icons separated by new line
    print("\n".join(social_media_list))

    
# Payment button check
def payment_redirect(driver):
     # Find all payment buttons on the page
    payment_buttons = driver.find_elements(By.XPATH, "//a[.//span[@class='button__content_1_I']]")

    payment_buttons_dict = {}
    for button in payment_buttons:
        link = button.get_attribute("href")
        payment_name = re.search(r'/(.+/)', link).group(1)  # Extract payment name
        payment_buttons_dict[payment_name] = link
    
    for payment_name, link in payment_buttons_dict.items():
        # Click on link from dict
        driver.get(link)

        # Getting opened url
        current_url = driver.current_url

        # Check if opened link == link from dict(website page)
        if current_url == link:
            
            print(f"Success: {payment_name}")
        else:
            print(f"Failed : {payment_name}.link: {current_url}")
            
    return payment_buttons_dict 

# Find  input field in feedback form
def find_input_field (driver, place_holder_name, input_data):    
    xpath_selector = f"//input[@placeholder='{place_holder_name}']"
    element = driver.find_element(By.XPATH, xpath_selector)
    driver.execute_script("window.scrollTo(0, 30);")
    element.click()
    time.sleep(0.5)
    element.send_keys(input_data)
    time.sleep(0.5)
    return element

# def test_feedback_form(driver, name, phone, email, expected_result):
    