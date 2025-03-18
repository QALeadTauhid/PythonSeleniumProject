import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from CommonLogin import login_to_application  # Import reusable login function

# Setup WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Define login details
LOGIN_URL = "https://admin-ptm-panel.pay2me.co/login"
USERNAME = "----------"
PASSWORD = "------------"

# Call the reusable login function
login_to_application(driver, USERNAME, PASSWORD, LOGIN_URL)

# Wait setup
wait = WebDriverWait(driver, 20)

# Profile types and corresponding XPaths
profiles = [
    ("Personal", "//a[@href='/users/type/personal']//button[@type='button']/span[1]", "//a[@href='/users/type/personal']//button[@type='button']/span[2]"),
    ("B. Lite", "//a[@href='/users/type/lite']//button[@type='button']/span[1]", "//a[@href='/users/type/lite']//button[@type='button']/span[2]"),
    ("B. Basic", "//a[@href='/users/type/basic']//button[@type='button']/span[1]", "//a[@href='/users/type/basic']//button[@type='button']/span[2]"),
    ("B. Pro", "//a[@href='/users/type/pro']//button[@type='button']/span[1]", "//a[@href='/users/type/pro']//button[@type='button']/span[2]")
]

# Function to get the total number for each profile
def get_profile_count(profile_name, profile_xpath, number_xpath):
    try:
        # Click on the profile tab
        profile_tab = wait.until(EC.element_to_be_clickable((By.XPATH, profile_xpath)))
        profile_tab.click()

        # Allow time for data to refresh
        time.sleep(3)

        # Fetch the total number
        total_number = wait.until(EC.presence_of_element_located((By.XPATH, number_xpath)))

        return total_number.text.strip()
    except Exception as e:
        print(f"Error fetching data for {profile_name}: {e}")
        return "0"

# Collect data
data = [(name, get_profile_count(name, click_xpath, number_xpath)) for name, click_xpath, number_xpath in profiles]

# Display data in terminal
print("\nProfile Type         | Total Number")
print("---------------------|-------------")
for profile, count in data:
    print(f"{profile:<20} | {count}")

# Save to CSV
csv_file = "profile_counts.csv"
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Profile Type", "Total Number"])
    writer.writerows(data)

print(f"\nData saved to {csv_file}")

# Clean up
driver.quit()
