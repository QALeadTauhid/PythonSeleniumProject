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
USERNAME = "--------"
PASSWORD = "--------"

# Call the reusable login function
login_to_application(driver, USERNAME, PASSWORD, LOGIN_URL)

# Now proceed with your test actions after login
print("Performing test cases after login...")

# Wait setup
wait = WebDriverWait(driver, 10)
all_customers = []

# Open Invoice Section
invoiceList = wait.until(EC.presence_of_element_located((By.XPATH, "(//legend[normalize-space()='invoice'])[1]")))
invoiceList.click()

# Click "Cancel" Menu Option
menu = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Cancel Invoice']")))
menu.click()

# **Wait for Table to Fully Load Before First Fetch**
time.sleep(5)  # Ensures first page loads properly (adjust timing as needed)


# Function to fetch customers from the current page
def fetch_customers_from_cancel_list():
    return wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr")))


# Loop through pages and fetch customers
while True:
    # **Ensure table rows are loaded before extracting**
    rows = fetch_customers_from_cancel_list()

    if not rows:  # If no rows found, break the loop
        print("No customer data found on this page.")
        break

    # Iterate through all rows and fetch customer names
    for index, row in enumerate(rows, start=1):
        try:
            customer_name_xpath = f"./td[1]/p[1]"  # **Relative XPath (faster & reliable)**
            customer_name = row.find_element(By.XPATH, customer_name_xpath).text
            all_customers.append(customer_name)
            print(f"Customer {index}: {customer_name}")
        except Exception as e:
            print(f"Error fetching customer name for row {index}: {e}")

    # **Check for "Next" button availability**
    try:
        next_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Go to next page']//*[name()='svg']")))
        next_button.click()  # Click "Next" to move to the next page
        time.sleep(5)  # Wait for the next page to load properly
    except Exception:
        print("No more pages to load.")
        break  # Exit the loop if the "Next" button is not found or disabled

# # Print total number of customers fetched
print(f"Total Invoice found: {len(all_customers)}")

# **Count customer name occurrences (i.e., invoices)**
customer_counts = Counter(all_customers)

# # **Print Results**
# print("\nCompany Name and Invoice Count:")
# for customer, count in customer_counts.items():
#     print(f"Company Name: {customer}, Invoice Count: {count}")

# **Print Results with Numbering**
print("\nCompany Name and Invoice Count:")
for idx, (customer, count) in enumerate(customer_counts.items(), start=1):
    print(f"{idx}. Company Name: {customer}, Invoice Count: {count}")






# Close the browser after tests
driver.quit()
