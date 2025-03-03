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

# Call the reusable login function
login_to_application(driver, USERNAME, PASSWORD, LOGIN_URL)

print("Performing test cases after login...")

# Wait for the "user" section to be clickable
user_menu = wait.until(EC.presence_of_element_located((By.XPATH, "//legend[normalize-space()='user']")))
user_menu.click()

input_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.MuiInputBase-input")))
input_field.click()

input_field.send_keys("Name")
option_locator = "//li[contains(text(), 'Name')]"
desired_option = wait.until(EC.element_to_be_clickable((By.XPATH, option_locator)))
desired_option.click()

input_name = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Name']")))
input_name.send_keys("Test Tauhid")



# Close the browser
driver.quit()