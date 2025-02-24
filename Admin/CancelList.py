from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from CommonLogin import login_to_application  # Import the reusable login function

# Setup WebDriver
driver = webdriver.Chrome()

# Define login details
LOGIN_URL = "https://admin-ptm-panel.pay2me.co/login"
USERNAME = "itteam.9@aieus.com"
PASSWORD = "sVs$j3z201IV"

# Call the reusable login function
login_to_application(driver, USERNAME, PASSWORD, LOGIN_URL)

# Now proceed with your test actions after login
print("Performing test cases after login...")

# Example: Perform additional actions after login
# driver.find_element(By.XPATH, "//span[normalize-space()='Cancel Invoice']").click()
#Cancel Invoice
wait4 = WebDriverWait(driver, 10)
menu = wait4.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Cancel Invoice']")))
menu.click()

# Close the browser after tests
driver.quit()
