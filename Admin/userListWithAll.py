import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from CommonLogin import login_to_application

# Setup WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Define login details
LOGIN_URL = "https://admin-ptm-panel.pay2me.co/login"
USERNAME = "--------"
PASSWORD = "-----------"

# Call the reusable login function
login_to_application(driver, USERNAME, PASSWORD, LOGIN_URL)

# Wait setup
wait = WebDriverWait(driver, 20)

# Account types with navigation XPaths
account_types = [
    ("Personal", "//a[@href='/users/type/personal']//button[@type='button']"),
    ("B. Lite", "//a[@href='/users/type/lite']//button[@type='button']"),
    ("B. Basic", "//a[@href='/users/type/basic']//button[@type='button']"),
    ("B. Pro", "//a[@href='/users/type/pro']//button[@type='button']")
]

# Pagination next button XPath
pagination_next_xpath = "//button[@aria-label='Go to next page']"

# Table data XPaths
xpaths = {
    "Customer Name": "./td[1]/p[1]",
    "Payment ID": "./td[1]/p[2]",
    "Register Date": "./td[2]/p[1]",
    "Register Time": "./td[2]/p[2]",
    "Country": "./td[3]/p[1]",
    "IP Address": "./td[3]/button",
    "Invoice Sent": "./td[4]/p[1]/a[1]/span[1]",
    "Invoice Received": "./td[4]/p[1]/a[2]/span[1]",
    "Check Sent": "./td[5]/a[1]/span[1]",
    "KYC": "./td[6]/div[1]/p[1]/a[1]/span[1]/span[1]",
    "KYB": "./td[6]/div[1]/p[1]/a[2]/span[1]/span[1]",
    "Bank": "./td[6]/div[1]/p[1]/a[3]/span[1]/span[1]",
    "CC": "./td[6]/div[1]/p[1]/a[4]/span[1]/span[1]",
    "Merchant Account": "./td[7]/p[1]",
    "Company Account": "./td[8]/p[1]",
    "Profile Update": "./td[9]/p[1]",
    "Status": "./td[10]/div[1]/div[1]/p[1]",
    "Type": "./td[11]/a[1]/button[1]"
}

# Function to extract text from an element
def get_element_text(row, xpath):
    try:
        element = row.find_element(By.XPATH, xpath)
        return element.text.strip()
    except:
        return "N/A"

# Function to extract data from the table for a given account type
def extract_table_data(account_name, account_xpath):
    # Click on the account type tab
    wait.until(EC.element_to_be_clickable((By.XPATH, account_xpath))).click()
    time.sleep(3)  # Allow time for the page to load

    data = []

    page = 1
    while True:
        print(f"Extracting {account_name} - Page {page}")

        # Wait for table rows to be present
        rows = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr")))

        for row in rows:
            row_data = {"Account Type": account_name}
            for key, value_xpath in xpaths.items():
                row_data[key] = get_element_text(row, value_xpath)
            data.append(row_data)
            print(row_data)  # Print the data to the terminal

        # Check for pagination and move to the next page if available
        try:
            next_button = wait.until(EC.element_to_be_clickable((By.XPATH, pagination_next_xpath)))
            next_button.click()
            page += 1
            time.sleep(3)  # Wait for the next page to load
        except:
            print(f"No more pages for {account_name}.")
            break

    return data

# Collect all data
all_data = []
for name, xpath in account_types:
    all_data.extend(extract_table_data(name, xpath))

# Save data to CSV
csv_file = "account_data.csv"
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["Account Type"] + list(xpaths.keys()))
    writer.writeheader()
    writer.writerows(all_data)

print(f"Data saved to {csv_file}")

# Clean up
driver.quit()
