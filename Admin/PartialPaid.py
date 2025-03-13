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
LOGIN_URL = "https://admin-ptm-panel.pay2me.co/login"
USERNAME = "-----------"
PASSWORD = "++++sVs$j+++3z201IV----"

# Call the reusable login function
login_to_application(driver, USERNAME, PASSWORD, LOGIN_URL)

# Now proceed with your test actions after login
print("Performing test cases after login...")

# Wait setup
wait = WebDriverWait(driver, 20)  # Increased timeout to handle slow loading


#Invoice counting check
wait1 = WebDriverWait(driver, 10)  # Waits up to 10 seconds
invoiceList = wait1.until(EC.presence_of_element_located((By.XPATH, "(//legend[normalize-space()='invoice'])[1]")))

invoiceList.click()

#New
wait4 = WebDriverWait(driver, 10)
menu = wait4.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Partial Paid']")))

menu.click()


def fetch_table_data():
    wait = WebDriverWait(driver, 15)

    # Ensure the table is fully loaded
    wait.until(EC.presence_of_element_located((By.XPATH, "//table")))

    # Wait until at least one row is loaded
    wait.until(EC.presence_of_element_located((By.XPATH, "//tbody/tr")))

    # Scroll multiple times to ensure all rows are loaded
    for _ in range(5):
        driver.execute_script("window.scrollBy(0,500)")
        time.sleep(2)  # Allow UI to update

    rows = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr")))

    print(f"Found {len(rows)} rows in the table.")

    data = []
    for index, row in enumerate(rows):
        try:
            wait.until(EC.visibility_of(row))  # Ensure row is visible

            customer_name = row.find_element(By.XPATH, ".//td[1]/p[1]").text.strip() if row.find_elements(By.XPATH, ".//td[1]/p[1]") else "N/A"
            account_id = row.find_element(By.XPATH, ".//td[1]/p[2]").text.strip() if row.find_elements(By.XPATH, ".//td[1]/p[2]") else "N/A"
            total_invoice = row.find_element(By.XPATH, ".//td[2]/p[1]").text.strip() if row.find_elements(By.XPATH, ".//td[2]/p[1]") else "N/A"
            order_date = row.find_element(By.XPATH, ".//td[4]/p[1]").text.strip() if row.find_elements(By.XPATH, ".//td[4]/p[1]") else "N/A"
            order_time = row.find_element(By.XPATH, ".//td[4]/p[2]").text.strip() if row.find_elements(By.XPATH, ".//td[4]/p[2]") else "N/A"
            paid_date = row.find_element(By.XPATH, ".//td[5]/p[1]/span[1]").text.strip() if row.find_elements(By.XPATH, ".//td[5]/p[1]/span[1]") else "N/A"
            paid_time = row.find_element(By.XPATH, ".//td[5]/p[1]/span[2]").text.strip() if row.find_elements(By.XPATH, ".//td[5]/p[1]/span[2]") else "N/A"
            invoice_amount = row.find_element(By.XPATH, ".//td[6]/p[1]/span[1]").text.strip() if row.find_elements(By.XPATH, ".//td[6]/p[1]/span[1]") else "N/A"
            partial_amount = row.find_element(By.CLASS_NAME,"text-red-strong").text.strip() if row.find_elements(By.CLASS_NAME, "text-red-strong") else "N/A"
            paid_amount = row.find_element(By.CLASS_NAME,"text-green-tealish").text.strip() if row.find_elements(By.CLASS_NAME, "text-green-tealish") else "N/A"

            status = row.find_element(By.XPATH, ".//td[8]/div[1]/div[1]/a[1]/button[1]").text.strip() if row.find_elements(By.XPATH, ".//td[8]/div[1]/div[1]/a[1]/button[1]") else "N/A"
            try:
                payment_link = row.find_element(By.XPATH, ".//td[8]/div[2]/a[1]").get_attribute("href")
            except:
                payment_link = "N/A"

            print(f"Row {index + 1}: {customer_name}, {account_id}, {total_invoice}, {order_date}, {order_time}, {paid_date}, {paid_time}, {invoice_amount},{partial_amount},{paid_amount},{status},{payment_link}")
            data.append((customer_name, account_id, total_invoice, order_date, order_time, paid_date, paid_time, invoice_amount, partial_amount, paid_amount, status, payment_link))

        except Exception as e:
            print(f"Skipping row {index + 1} due to error: {e}")

    return data


def navigate_to_next_page():
    try:
        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Go to next page']//*[name()='svg']")))
        next_button.click()
        print("✅ Clicked on next page button.")
        time.sleep(2)  # Wait for the next page to load
        return True
    except Exception as e:
        print(f"⚠️ Pagination error skip ended")
        return False


# Fetch data from the first page and navigate through all pages
page_number = 1
all_data = []

while True:
    print(f"\n📄 Fetching data from page {page_number}...")
    page_data = fetch_table_data()
    all_data.extend(page_data)

    # Try to navigate to the next page, if possible
    if not navigate_to_next_page():
        break  # Stop if there's no next page button or error occurs

    page_number += 1  # Increment page number


# Print structured output
print("\nExtracted Data:")
print(f"{'No.':<5} {'Customer Name':<40} {'Account ID':<20} {'Total Invoice':<25} {'Order Date':<20} {'Order Time':<20} "
      f"{'Paid Date':<20} {'Paid Time':<20} {'Invoice Amount':<20} {'Partial Amount':<20} {'Paid Amount':<20} {'Status':<40} {'Payment Link':<20}")
print("=" * 120)

for idx, (customer_name, account_id, total_invoice, order_date, order_time, paid_date, paid_time, invoice_amount, partial_amount, paid_amount, status, payment_link) in enumerate(all_data, 1):
    print(f"{idx:<5} {customer_name:<40} {account_id:<20} {total_invoice:<25} {order_date:<20} {order_time:<20} "
          f"{paid_date:<20} {paid_time:<20} {invoice_amount:<20} {partial_amount:<20} {paid_amount:<20} {status:<40} {payment_link:<20}")

# Save data to CSV
csv_filename = 'Partial_paid_all_pages_data.csv'
with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Customer Name', 'Account ID', 'Total Invoice', 'Order Date', 'Order Time', 'Paid Date', 'Paid time', 'Invoice Amount', 'Partial Amount', 'Paid Amount', 'Status', 'Payment Link'])
    writer.writerows(all_data)

print(f"Data saved to '{csv_filename}'.")

# Close browser
driver.quit()
