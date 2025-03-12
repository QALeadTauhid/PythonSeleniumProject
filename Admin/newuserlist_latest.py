import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from CommonLogin import login_to_application  # Import reusable login function

# Setup WebDriver
driver = webdriver.Chrome()
driver.maximize_window()  # Ensure all elements are visible

# Define login details
LOGIN_URL = "https://admin-ptm-panel.paytome.co/login"
USERNAME = "--------------"
PASSWORD = "----------"

# Call the reusable login function
login_to_application(driver, USERNAME, PASSWORD, LOGIN_URL)

# Now proceed with your test actions after login
print("Performing test cases after login...")

# Wait setup
wait = WebDriverWait(driver, 20)  # Increased timeout to handle slow loading

# Click on "New User" section
try:
    new_user_list = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='New User']")))
    new_user_list.click()
    print("Navigated to New User List.")
except Exception as e:
    print(f"Failed to click on 'New User' list: {e}")
    driver.quit()
    exit()

# Ensure the table is fully loaded
try:
    wait.until(EC.presence_of_element_located((By.XPATH, "//tbody/tr")))
    time.sleep(3)  # Extra buffer time for full table load
    print("Table loaded successfully.")
except Exception as e:
    print(f"Table not found or not loaded: {e}")
    driver.quit()
    exit()


def fetch_table_data():
    """Extracts data from the first page of the table, ensuring all rows are captured."""

    # Ensure all rows are visible
    driver.execute_script("window.scrollBy(0, 500)")  # Scroll to load all rows
    time.sleep(2)  # Wait for UI updates

    # Fetch all visible rows
    rows = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr")))
    data = []

    print(f"Found {len(rows)} rows in the table.")  # Debugging

    for index, row in enumerate(rows):
        try:
            print(f"\nProcessing row {index + 1}...")  # Debugging

            # Extract all required elements from the row
            customer_name = row.find_element(By.XPATH, "./td[1]/p[1]").text.strip() if row.find_elements(By.XPATH, "./td[1]/p[1]") else "N/A"
            account_id = row.find_element(By.XPATH, "./td[1]/p[2]").text.strip() if row.find_elements(By.XPATH, "./td[1]/p[2]") else "N/A"
            country = row.find_element(By.XPATH, "./td[3]/p[1]").text.strip() if row.find_elements(By.XPATH, "./td[3]/p[1]") else "N/A"
            ip_address = row.find_element(By.XPATH, "./td[3]/button").text.strip() if row.find_elements(By.XPATH, "./td[3]/button") else "N/A"
            date_acc = row.find_element(By.XPATH, "./td[2]/p[1]").text.strip() if row.find_elements(By.XPATH, "./td[2]/p[1]") else "N/A"
            merchant_account = row.find_element(By.XPATH, "./td[7]/p[1]").text.strip() if row.find_elements(By.XPATH, "./td[7]/p[1]") else "N/A"
            company_account = row.find_element(By.XPATH, "./td[8]/p[1]").text.strip() if row.find_elements(By.XPATH, "./td[8]/p[1]") else "N/A"
            profile_update = row.find_element(By.XPATH, "./td[9]/p[1]").text.strip() if row.find_elements(By.XPATH, "./td[9]/p[1]") else "N/A"
            status = row.find_element(By.XPATH, "./td[10]/div[1]/div[1]/p[1]").text.strip() if row.find_elements(By.XPATH, "./td[10]/div[1]/div[1]/p[1]") else "N/A"
            account_type = row.find_element(By.XPATH, "./td[11]/a[1]/button[1]/p[1]").text.strip() if row.find_elements(By.XPATH, "./td[11]/a[1]/button[1]/p[1]") else "N/A"

            # Debugging Output
            print(f"Customer: {customer_name}, Account ID: {account_id}, Country: {country}, IP: {ip_address}, "
                  f"Date: {date_acc}, Merchant Account: {merchant_account}, Company Account: {company_account}, "
                  f"Profile Update: {profile_update}, Status: {status}, Account Type: {account_type}")

            # Store extracted data
            data.append((customer_name, account_id, country, ip_address, date_acc, merchant_account, company_account, profile_update, status, account_type))

        except Exception as e:
            print(f"Skipping row {index + 1} due to error: {e}")

    return data


# Fetch data from the first page
first_page_data = fetch_table_data()

# Print structured output
print("\nExtracted Data:")
print(f"{'Customer Name':<30} {'Account ID':<20} {'Country':<25} {'IP Address':<20} {'Date':<20} "
      f"{'Merchant Account':<10} {'Company Account':<10} {'Profile Update':<20} {'Status':<20} {'Account Type':<20}")
print("=" * 80)

for customer_name, account_id, country, ip_address, date_acc, merchant_account, company_account, profile_update, status, account_type in first_page_data:
    print(f"{customer_name:<30} {account_id:<20} {country:<25} {ip_address:<20} {date_acc:<20} "
          f"{merchant_account:<20} {company_account:<20} {profile_update:<20} {status:<10} {account_type:<10}")

# Save data to CSV
csv_filename = 'first_page_data.csv'
with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Customer Name', 'Account ID', 'Country', 'IP Address', 'Date', 'Merchant Account', 'Company Account', 'Profile Update', 'Status', 'Account Type'])  # Corrected missing comma
    writer.writerows(first_page_data)  # Write rows

print(f"Data saved to '{csv_filename}'.")

# Close browser
driver.quit()


# import csv
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from CommonLogin import login_to_application  # Import reusable login function
#
# # Setup WebDriver
# driver = webdriver.Chrome()
# driver.maximize_window()  # Ensure all elements are visible
#
# # Define login details
# LOGIN_URL = "https://admin-ptm-panel.pay2me.co/login"
# USERNAME = ".............
# PASSWORD = "............"
#
# # Call the reusable login function
# login_to_application(driver, USERNAME, PASSWORD, LOGIN_URL)
#
# # Now proceed with your test actions after login
# print("Performing test cases after login...")
#
# # Wait setup
# wait = WebDriverWait(driver, 20)  # Increased timeout to handle slow loading
#
# # Click on "New User" section
# try:
#     new_user_list = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='New User']")))
#     new_user_list.click()
#     print("Navigated to New User List.")
# except Exception as e:
#     print(f"Failed to click on 'New User' list: {e}")
#     driver.quit()
#     exit()
#
# # Ensure the table is fully loaded
# try:
#     wait.until(EC.presence_of_element_located((By.XPATH, "//tbody/tr")))
#     time.sleep(3)  # Extra buffer time for full table load
#     print("Table loaded successfully.")
# except Exception as e:
#     print(f"Table not found or not loaded: {e}")
#     driver.quit()
#     exit()
#
#
# def truncate_text(text, max_length=20):
#     """Truncate long text to prevent display issues."""
#     return text[:max_length] + "..." if len(text) > max_length else text
#
#
# def fetch_table_data():
#     """Extracts data from the first page of the table, ensuring all rows are captured."""
#
#     driver.execute_script("window.scrollBy(0, 500)")  # Scroll to load all rows
#     time.sleep(2)  # Wait for UI updates
#
#     rows = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr")))
#     data = []
#
#     print(f"Found {len(rows)} rows in the table.")  # Debugging
#
#     for index, row in enumerate(rows):
#         try:
#             print(f"\nProcessing row {index + 1}...")  # Debugging
#
#             # Extract all required elements from the row
#             customer_name = row.find_element(By.XPATH, "./td[1]/p[1]").text.strip() if row.find_elements(By.XPATH,
#                                                                                                          "./td[1]/p[1]") else "N/A"
#             account_id = row.find_element(By.XPATH, "./td[1]/p[2]").text.strip() if row.find_elements(By.XPATH,
#                                                                                                       "./td[1]/p[2]") else "N/A"
#             country = row.find_element(By.XPATH, "./td[3]/p[1]").text.strip() if row.find_elements(By.XPATH,
#                                                                                                    "./td[3]/p[1]") else "N/A"
#             ip_address = row.find_element(By.XPATH, "./td[3]/button").text.strip() if row.find_elements(By.XPATH,
#                                                                                                         "./td[3]/button") else "N/A"
#             date_acc = row.find_element(By.XPATH, "./td[2]/p[1]").text.strip() if row.find_elements(By.XPATH,
#                                                                                                     "./td[2]/p[1]") else "N/A"
#             merchant_account = row.find_element(By.XPATH, "./td[7]/p[1]").text.strip() if row.find_elements(By.XPATH,
#                                                                                                             "./td[7]/p[1]") else "N/A"
#             company_account = row.find_element(By.XPATH, "./td[8]/p[1]").text.strip() if row.find_elements(By.XPATH,
#                                                                                                            "./td[8]/p[1]") else "N/A"
#             profile_update = row.find_element(By.XPATH, "./td[9]/p[1]").text.strip() if row.find_elements(By.XPATH,
#                                                                                                           "./td[9]/p[1]") else "N/A"
#             status = row.find_element(By.XPATH, "./td[10]/div[1]/div[1]/p[1]").text.strip() if row.find_elements(
#                 By.XPATH, "./td[10]/div[1]/div[1]/p[1]") else "N/A"
#             account_type = row.find_element(By.XPATH, "./td[11]/a[1]/button[1]/p[1]").text.strip() if row.find_elements(
#                 By.XPATH, "./td[11]/a[1]/button[1]/p[1]") else "N/A"
#
#             # Truncate long data for better display
#             customer_name = truncate_text(customer_name)
#             account_id = truncate_text(account_id)
#             country = truncate_text(country)
#             ip_address = truncate_text(ip_address)
#             date_acc = truncate_text(date_acc)
#             merchant_account = truncate_text(merchant_account)
#             company_account = truncate_text(company_account)
#             profile_update = truncate_text(profile_update)
#             status = truncate_text(status)
#             account_type = truncate_text(account_type)
#
#             # Debugging Output
#             print(f"Customer: {customer_name}, Account ID: {account_id}, Country: {country}, IP: {ip_address}, "
#                   f"Date: {date_acc}, Merchant Account: {merchant_account}, Company Account: {company_account}, "
#                   f"Profile Update: {profile_update}, Status: {status}, Account Type: {account_type}")
#
#             # Store extracted data
#             data.append((customer_name, account_id, country, ip_address, date_acc, merchant_account, company_account,
#                          profile_update, status, account_type))
#
#         except Exception as e:
#             print(f"Skipping row {index + 1} due to error: {e}")
#
#     return data
#
#
# # Fetch data from the first page
# first_page_data = fetch_table_data()
#
# # Print structured output
# print("\nExtracted Data:")
# headers = ["Customer Name", "Account ID", "Country", "IP Address", "Date", "Merchant Account", "Company Account",
#            "Profile Update", "Status", "Account Type"]
# print(f"{' | '.join(h[:15] for h in headers)}")
# print("=" * 120)
#
# for row in first_page_data:
#     print(f"{' | '.join(value.ljust(15) for value in row)}")
#
# # Save data to CSV
# csv_filename = 'first_page_data.csv'
# with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(headers)  # Write header
#     writer.writerows(first_page_data)  # Write rows
#
# print(f"Data saved to '{csv_filename}'.")
#
# # Close browser
# driver.quit()
