from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



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



#Invoice counting check
wait1 = WebDriverWait(driver, 10)  # Waits up to 10 seconds
invoiceList = wait1.until(EC.presence_of_element_located((By.XPATH, "(//legend[normalize-space()='invoice'])[1]")))
invoiceList.click()

#New
wait4 = WebDriverWait(driver, 10)
menu = wait4.until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='MuiBox-root css-hkavrg'][normalize-space()='New'])[2]")))
menu.click()

# # Wait setup
# wait = WebDriverWait(driver, 10)
# all_customers = []
#
# # Function to fetch customers from the current page
# def fetch_customers_from_page():
#     rows = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr[td[1]]")))
#     return rows
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
#         time.sleep(2)  # Wait for the next page to load
#     except Exception:
#         print("No more pages to load.")
#         break  # Exit the loop if the "Next" button is not found or disabled
#
# # Print the total number of customers found
# print(f"Total customers found: {len(all_customers)}")

# Wait setup
wait = WebDriverWait(driver, 10)
all_customers = []


# Function to fetch customers from the current page
def fetch_customers_from_page():
    """Fetches customer rows from the current page."""
    return wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr[td[1]]")))


while True:
    rows = fetch_customers_from_page()  # Fetch all rows on the page

    for index, row in enumerate(rows, start=1):
        try:
            # Use relative XPath inside the row
            customer_name = row.find_element(By.XPATH, "./td[1]").text  # No need for <p>
            all_customers.append(customer_name)
            print(f"Customer {index}: {customer_name}")
        except Exception as e:
            print(f"Error fetching customer name for row {index}: {e}")

    # Attempt to click "Next" button
    try:
        next_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Go to next page']//*[name()='svg']")))
        next_button.click()

        # Wait for new rows to load
        wait.until(EC.staleness_of(rows[0]))  # Ensures old rows disappear
        time.sleep(2)  # Small delay
    except Exception:
        print("No more pages to load.")
        break  # Exit loop if "Next" button is not found

# Print total customers
print(f"Total customers found: {len(all_customers)}")
