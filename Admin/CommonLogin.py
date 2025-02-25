from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login_to_application(driver, username, password, login_url):
    """Reusable function to log in to the PTM application"""

    driver.get(login_url)  # Open the login page
    driver.maximize_window()  # Optional: maximize the browser window

    wait = WebDriverWait(driver, 30)  # Waits up to 10 seconds

    # Locate email input field and send the username/email
    email_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@placeholder, 'johndoe')]")))
    email_input.send_keys(username)

    # Locate password input field and send the password
    password_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='auth-login-v2-password']")))
    password_input.send_keys(password)

    # Locate and click the login button
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Login'])[1]")))
    login_button.click()

    time.sleep(10)

    print("Login successful!")
