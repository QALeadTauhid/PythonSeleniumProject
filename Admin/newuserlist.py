from collections import Counter

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from CommonLogin import login_to_application  # Import the reusable login function
import time

# Setup WebDriver
driver = webdriver.Chrome()

# Define login details
LOGIN_URL = "https://admin-ptm-panel.pay2me.co/login"
USERNAME = "----"
PASSWORD = "-----"

# Call the reusable login function
login_to_application(driver, USERNAME, PASSWORD, LOGIN_URL)

# Now proceed with your test actions after login
print("Performing test cases after login...")

# Wait setup
wait = WebDriverWait(driver, 10)
all_customers = []

#user list
newUserList = wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='New User']")))
newUserList.click()


