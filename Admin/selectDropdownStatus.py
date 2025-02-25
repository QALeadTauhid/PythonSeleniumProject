import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Admin.CommonLogin import login_to_application

# Setup WebDriver
driver = webdriver.Chrome()

# Define login details
LOGIN_URL = "https://admin-ptm-panel.pay2me.co/login"
USERNAME = "---------"
PASSWORD = "----------------"

# Call the reusable login function
login_to_application(driver, USERNAME, PASSWORD, LOGIN_URL)

# Now proceed with test actions after login
print("Performing test cases after login...")

# User section
wait = WebDriverWait(driver, 10)

# Wait for the "user" section to be clickable
user_menu = wait.until(EC.presence_of_element_located((By.XPATH, "//legend[normalize-space()='user']")))
driver.execute_script("arguments[0].scrollIntoView();", user_menu)
user_menu.click()

# Wait for the input field to be clickable
input_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.MuiInputBase-input")))
input_field.click()

# Type and select from dropdown
input_field.send_keys("Name")
option_locator = "//li[contains(text(), 'Name')]"
desired_option = wait.until(EC.element_to_be_clickable((By.XPATH, option_locator)))
desired_option.click()

# Ensure input field for 'Name' is visible and interactable
input_name = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Name']")))
input_name.send_keys("Test Tauhid")

# Click the Search button
search_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Search']")))
search_button.click()

# Wait for results dynamically instead of using sleep
wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'No records found') or @class='search-results']")))

# Close the browser
driver.quit()
