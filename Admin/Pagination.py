from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from collections import Counter


# Set up Chrome WebDriver
driver = webdriver.Chrome()

# Open PTM
driver.get("https://admin-ptm-panel.paytome.co/login")

driver.maximize_window()



wait = WebDriverWait(driver, 20)  # Waits up to 10 seconds
email_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@placeholder, 'johndoe')]")))
email_input.send_keys("itteam.9@aieus.com")

#Login in to the admin
# driver.find_element(By.XPATH, "//input[@placeholder='johndoe']").send_keys("itteam.9@aieus.com")
driver.find_element(By.XPATH, "//input[@id='auth-login-v2-password']").send_keys("sVs$j3z201IV")
driver.find_element(By.XPATH, "(//button[normalize-space()='Login'])[1]").click()



# #Invoice counting check
# wait1 = WebDriverWait(driver, 20)  # Waits up to 10 seconds
# invoiceList = wait1.until(EC.presence_of_element_located((By.XPATH, "(//legend[normalize-space()='invoice'])[1]")))
# invoiceList.click()
#
# #New
# wait4 = WebDriverWait(driver, 20)
# menu = wait4.until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='MuiBox-root css-hkavrg'][normalize-space()='New'])[2]")))
# menu.click()
#
# # Wait setup
# wait12 = WebDriverWait(driver, 200)
# all_customers = []
#
# # Function to fetch customers from the current page
# def fetch_customers_from_page():
#     rows1 = wait12.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr[td[1]]")))
#     return rows1
#
# # Loop through pages and fetch customers
# while True:
#     # Fetch customers from the current page
#     rows = fetch_customers_from_page()
#
#     # Iterate through all rows and fetch customer names
#     for index, row in enumerate(rows, start=1):
#         try:
#             customer_name_xpath = f"//tbody/tr[{index}]/td[1]/p[1]"
#             customer_name = row.find_element(By.XPATH, customer_name_xpath).text
#             all_customers.append(customer_name)
#             print(f"Customer {index}: {customer_name}")
#         except Exception as e:
#             print(f"Error fetching customer name for row {index}: {e}")
#
#     # Check if the "Next" button is present and enabled
#     try:
#         next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Go to next page']//*[name()='svg']")))
#         next_button.click()  # Click "Next" to move to the next page
#         time.sleep(10)  # Wait for the next page to load
#     except Exception:
#         print("No more pages to load.")
#         break  # Exit the loop if the "Next" button is not found or disabled
#
# # Print the total number of customers found
# print(f"Total customers found: {len(all_customers)}")

# # Wait setup
# wait = WebDriverWait(driver, 100)
# all_customers = []
#
#
# # Function to fetch customers from the current page
# def fetch_customers_from_page():
#     """Fetches customer rows from the current page."""
#     return wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr[td[1]]")))
#
#
# while True:
#     rows = fetch_customers_from_page()  # Fetch all rows on the page
#
#     for index, row in enumerate(rows, start=1):
#         try:
#             # Use relative XPath inside the row
#             customer_name = row.find_element(By.XPATH, "./td[1]").text  # No need for <p>
#             all_customers.append(customer_name)
#             print(f"Customer {index}: {customer_name}")
#         except Exception as e:
#             print(f"Error fetching customer name for row {index}: {e}")
#
#     # Attempt to click "Next" button
#     try:
#         next_button = wait.until(
#             EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Go to next page']//*[name()='svg']")))
#         next_button.click()
#
#         # Wait for new rows to load
#         wait.until(EC.staleness_of(rows[0]))  # Ensures old rows disappear
#         time.sleep(2)  # Small delay
#     except Exception:
#         print("No more pages to load.")
#         break  # Exit loop if "Next" button is not found
#
# # Print total customers
# print(f"Total customers found: {len(all_customers)}")


# Wait setup
wait = WebDriverWait(driver, 20)
all_customers = []

# Open Invoice Section
invoiceList = wait.until(EC.presence_of_element_located((By.XPATH, "(//legend[normalize-space()='invoice'])[1]")))
invoiceList.click()

# Click "New" Menu Option
menu = wait.until(
    EC.element_to_be_clickable((By.XPATH, "(//span[@class='MuiBox-root css-hkavrg'][normalize-space()='New'])[2]")))
menu.click()

# **Wait for Table to Fully Load Before First Fetch**
time.sleep(5)  # Ensures first page loads properly (adjust timing as needed)


# Function to fetch customers from the current page
def fetch_customers_from_page():
    return wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr")))


# Loop through pages and fetch customers
while True:
    # **Ensure table rows are loaded before extracting**
    rows = fetch_customers_from_page()

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
