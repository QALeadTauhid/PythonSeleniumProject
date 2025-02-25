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
PASSWORD = "-------"

# Call the reusable login function
login_to_application(driver, USERNAME, PASSWORD, LOGIN_URL)

# Now proceed with your test actions after login
print("Performing test cases after login...")

# Wait setup
wait = WebDriverWait(driver, 10)

#user list
newUserList = wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='New User']")))
newUserList.click()

#Approach
# # Function to fetch table data
# def fetch_table_data():
#     time.sleep(2)  # Allow time for the page to fully load
#
#     rows = driver.find_elements(By.XPATH, "//tbody/tr")  # Get all rows
#     data = []
#
#     for row in rows:
#         try:
#             # Extract Customer Name and Account ID from Column 1
#             customer_name = row.find_element(By.XPATH, "./td[1]/p[1]").text
#             account_id = row.find_element(By.XPATH, "./td[1]/p[2]").text
#
#             # Extract Country and IP Address from Column 3
#             country = row.find_element(By.XPATH, "./td[3]/p[1]").text
#             ip_address = row.find_element(By.XPATH, "./td[3]/button").text  # Button contains IP text
#
#             # Store extracted data
#             data.append((customer_name, account_id, country, ip_address))
#
#         except Exception as e:
#             print(f"Skipping row due to error: {e}")
#
#     return data
#
# # Store all pages' data
# all_data = []
#
# while True:
#     time.sleep(3)  # Wait before fetching data to ensure full page load
#     all_data.extend(fetch_table_data())  # Fetch data from current page
#
#     try:
#         # Locate "Next Page" button
#         next_button = WebDriverWait(driver, 5).until(
#             EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Go to next page']//*[name()='svg']"))
#         )
#         time.sleep(2)  # Wait before clicking to ensure smooth transition
#         next_button.click()
#         WebDriverWait(driver, 3).until(EC.staleness_of(next_button))  # Wait for page reload
#     except Exception as e:
#         print("No more pages or error encountered:", e)
#         break  # Exit loop if no more pages
#
# # Print collected data with titles
# print(f"{'Customer Name':<20} {'Account ID':<15} {'Country':<20} {'IP Address':<20}")
# print("=" * 80)  # Separator line
#
# for customer_name, account_id, country, ip_address in all_data:
#     print(f"{customer_name:<20} {account_id:<15} {country:<20} {ip_address:<20}")
#
# # Close browser
# driver.quit()

#Approach 2
# def fetch_table_data():
#     time.sleep(2)  # Ensure page loads fully
#     rows = driver.find_elements(By.XPATH, "//tbody/tr")  # Get all rows
#     data = []
#
#     print(f"Found {len(rows)} rows in the table")  # Debugging
#
#     for index, row in enumerate(rows):
#         try:
#             print(f"\nProcessing row {index + 1}...")  # Debugging
#
#             # Column 1: Customer Name & Account ID
#             customer_name_elements = row.find_elements(By.XPATH, "./td[1]/p[1]")
#             account_id_elements = row.find_elements(By.XPATH, "./td[1]/p[2]")
#
#             customer_name = customer_name_elements[0].text if customer_name_elements else "N/A"
#             account_id = account_id_elements[0].text if account_id_elements else "N/A"
#
#             # Column 3: Country & IP Address
#             country_elements = row.find_elements(By.XPATH, "./td[3]/p[1]")
#             ip_elements = row.find_elements(By.XPATH, "./td[3]/button")
#
#             country = country_elements[0].text if country_elements else "N/A"
#             ip_address = ip_elements[0].text if ip_elements else "N/A"
#
#             # Debugging Output
#             print(f"Customer: {customer_name}, Account ID: {account_id}, Country: {country}, IP: {ip_address}")
#
#             # Store extracted data
#             data.append((customer_name, account_id, country, ip_address))
#
#         except Exception as e:
#             print(f"Skipping row {index + 1} due to error: {e}")
#
#     return data
#
#
# # Run extraction and print data
# all_data = fetch_table_data()
#
# # Print structured output
# print("\nExtracted Data:")
# print(f"{'Customer Name':<20} {'Account ID':<15} {'Country':<20} {'IP Address':<20}")
# print("=" * 80)
#
# for customer_name, account_id, country, ip_address in all_data:
#     print(f"{customer_name:<20} {account_id:<15} {country:<20} {ip_address:<20}")
#
# # Close browser
# driver.quit()

#Approach 3
# def fetch_table_data():
#     """Extracts table data from the current page."""
#     time.sleep(2)  # Ensure page loads fully
#     rows = driver.find_elements(By.XPATH, "//tbody/tr")  # Get all rows
#     data = []
#
#     print(f"Found {len(rows)} rows in the table")  # Debugging
#
#     for index, row in enumerate(rows):
#         try:
#             print(f"\nProcessing row {index + 1}...")  # Debugging
#
#             # Column 1: Customer Name & Account ID
#             customer_name_elements = row.find_elements(By.XPATH, "./td[1]/p[1]")
#             account_id_elements = row.find_elements(By.XPATH, "./td[1]/p[2]")
#
#             customer_name = customer_name_elements[0].text if customer_name_elements else "N/A"
#             account_id = account_id_elements[0].text if account_id_elements else "N/A"
#
#             # Column 3: Country & IP Address
#             country_elements = row.find_elements(By.XPATH, "./td[3]/p[1]")
#             ip_elements = row.find_elements(By.XPATH, "./td[3]/button")
#
#             country = country_elements[0].text if country_elements else "N/A"
#             ip_address = ip_elements[0].text if ip_elements else "N/A"
#
#             # Debugging Output
#             print(f"Customer: {customer_name}, Account ID: {account_id}, Country: {country}, IP: {ip_address}")
#
#             # Store extracted data
#             data.append((customer_name, account_id, country, ip_address))
#
#         except Exception as e:
#             print(f"Skipping row {index + 1} due to error: {e}")
#
#     return data
#
#
# # Store all pages' data
# all_data = []
#
# while True:
#     time.sleep(3)  # Wait before fetching data to ensure full page load
#     all_data.extend(fetch_table_data())  # Fetch data from current page
#
#     try:
#         # Locate "Next Page" button
#         next_button = WebDriverWait(driver, 5).until(
#             EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Go to next page']//*[name()='svg']"))
#         )
#         time.sleep(2)  # Wait before clicking to ensure smooth transition
#         next_button.click()
#         WebDriverWait(driver, 3).until(EC.staleness_of(next_button))  # Wait for page reload
#     except Exception as e:
#         print("No more pages or error encountered:", e)
#         break  # Exit loop if no more pages
#
# # Print structured output
# print("\nExtracted Data:")
# print(f"{'Customer Name':<20} {'Account ID':<15} {'Country':<20} {'IP Address':<20}")
# print("=" * 80)
#
# for customer_name, account_id, country, ip_address in all_data:
#     print(f"{customer_name:<20} {account_id:<15} {country:<20} {ip_address:<20}")
#
# # Close browser
# driver.quit()

#Approach 4
from selenium.webdriver.common.action_chains import ActionChains
def fetch_table_data():
    time.sleep(2)  # Ensure page loads fully
    rows = driver.find_elements(By.XPATH, "//tbody/tr")  # Get all rows
    data = []

    print(f"Found {len(rows)} rows in the table")  # Debugging

    for index, row in enumerate(rows):
        try:
            print(f"\nProcessing row {index + 1}...")  # Debugging

            # Column 1: Customer Name & Account ID
            customer_name_elements = row.find_elements(By.XPATH, "./td[1]/p[1]")
            account_id_elements = row.find_elements(By.XPATH, "./td[1]/p[2]")

            customer_name = customer_name_elements[0].text if customer_name_elements else "N/A"
            account_id = account_id_elements[0].text if account_id_elements else "N/A"

            # Column 3: Country & IP Address
            country_elements = row.find_elements(By.XPATH, "./td[3]/p[1]")
            ip_elements = row.find_elements(By.XPATH, "./td[3]/button")

            country = country_elements[0].text if country_elements else "N/A"
            ip_address = ip_elements[0].text if ip_elements else "N/A"

            # Debugging Output
            print(f"Customer: {customer_name}, Account ID: {account_id}, Country: {country}, IP: {ip_address}")

            # Store extracted data
            data.append((customer_name, account_id, country, ip_address))

        except Exception as e:
            print(f"Skipping row {index + 1} due to error: {e}")

    return data


# Store all pages' data
all_data = []

while True:
    time.sleep(3)  # Wait before fetching data to ensure full page load
    all_data.extend(fetch_table_data())  # Fetch data from current page

    try:
        # Locate "Next Page" button
        next_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Go to next page']//*[name()='svg']"))
        )

        # Scroll the button into view
        ActionChains(driver).move_to_element(next_button).perform()

        time.sleep(2)  # Wait before clicking to ensure smooth transition
        next_button.click()

        # Wait for the page to reload (staleness of the previous "Next Page" button)
        WebDriverWait(driver, 3).until(EC.staleness_of(next_button))


    except Exception:
        print("No more pages to load. Go forward")
        break  # Exit the loop if the "Next" button is not found or disabled


# Print structured output
print("\nExtracted Data:")
print(f"{'Customer Name':<20} {'Account ID':<15} {'Country':<20} {'IP Address':<20}")
print("=" * 80)

for customer_name, account_id, country, ip_address in all_data:
    print(f"{customer_name:<20} {account_id:<15} {country:<20} {ip_address:<20}")

import csv

# Save the collected data to a CSV file
with open('collected_data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Write the header row (column titles)
    writer.writerow(['Customer Name', 'Account ID', 'Country', 'IP Address'])

    # Write the data rows
    for customer_name, account_id, country, ip_address in all_data:
        writer.writerow([customer_name, account_id, country, ip_address])

print("Data saved to 'collected_data.csv'.")

# Close browser
driver.quit()

#
# # Specify the directory and file name
# file_path = 'C:/Users/YourUsername/Documents/collected_data.csv'  # Modify this path as needed
#
# with open(file_path, mode='w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Customer Name', 'Account ID', 'Country', 'IP Address'])
#     for customer_name, account_id, country, ip_address in all_data:
#         writer.writerow([customer_name, account_id, country, ip_address])
#
# print(f"Data saved to {file_path}.")
