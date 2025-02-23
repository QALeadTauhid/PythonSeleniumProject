from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome WebDriver
driver = webdriver.Chrome()

# Open PTM
driver.get("https://admin-ptm-panel.pay2me.co/login")

driver.maximize_window()



wait = WebDriverWait(driver, 10)  # Waits up to 10 seconds
email_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@placeholder, 'johndoe')]")))
email_input.send_keys("itteam.9@aieus.com")

#Login in to the admin
# driver.find_element(By.XPATH, "//input[@placeholder='johndoe']").send_keys("itteam.9@aieus.com")
driver.find_element(By.XPATH, "//input[@id='auth-login-v2-password']").send_keys("sVs$j3z201IV")
driver.find_element(By.XPATH, "(//button[normalize-space()='Login'])[1]").click()



# Print Page Title
expected_title = "PayToMe Admin"  # Replace with your actual expected title
actual_title = driver.title  # Fetch the current page title

if actual_title == expected_title:
    print("Title matches! ✅:", actual_title)
else:
    print(f"Title mismatch! ❌ Expected: '{expected_title}', but got: '{actual_title}'")