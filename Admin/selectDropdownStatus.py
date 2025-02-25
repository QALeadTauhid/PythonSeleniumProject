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
PASSWORD = "++++sVs$j3z201IV++++"

# Call the reusable login function
login_to_application(driver, USERNAME, PASSWORD, LOGIN_URL)

# Now proceed with your test actions after login
print("Performing test cases after login...")

time.sleep(2)
#User section:
# Wait for the "user" section to be clickable
wait = WebDriverWait(driver, 10)
user_menu = wait.until(EC.presence_of_element_located((By.XPATH, "//legend[normalize-space()='user']")))
user_menu.click()

# Wait for the input field to be clickable, ensuring the dropdown is ready to be interacted with
input_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.MuiInputBase-input")))

# Click the input field to activate the dropdown
input_field.click()

# Type some text to filter the results
input_field.send_keys("Name")

# Wait for the dropdown options to appear
option_locator = "//li[contains(text(), 'Name')]"
desired_option = wait.until(EC.element_to_be_clickable((By.XPATH, option_locator)))

# Click the desired option
desired_option.click()

# Alternatively, use keyboard to select the first suggestion
input_field.send_keys(Keys.ARROW_DOWN)
input_field.send_keys(Keys.ENTER)

# Ensure the input field for 'Name' is ready for typing
input_name = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Name']")))
input_name.send_keys("Test Tauhid")

# Wait for the Search button to be clickable and then click it
value_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Search']")))
value_input.click()

# Wait for the necessary actions to complete (or page load to finish)
time.sleep(20)

# Close the browser
driver.quit()