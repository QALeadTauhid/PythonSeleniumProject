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
email_input.send_keys("---------")

#Login in to the admin
# driver.find_element(By.XPATH, "//input[@placeholder='johndoe']").send_keys("itteam.9@aieus.com")
driver.find_element(By.XPATH, "//input[@id='auth-login-v2-password']").send_keys("--------")
driver.find_element(By.XPATH, "(//button[normalize-space()='Login'])[1]").click()


#Invoice counting check
wait1 = WebDriverWait(driver, 10)  # Waits up to 10 seconds
invoiceList = wait1.until(EC.presence_of_element_located((By.XPATH, "(//legend[normalize-space()='invoice'])[1]")))
invoiceList.click()

#New
wait4 = WebDriverWait(driver, 10)
menu = wait4.until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='MuiBox-root css-hkavrg'][normalize-space()='New'])[2]")))
menu.click()

# Wait for the result (e.g., "New 379") to be visible
result_text = wait4.until(EC.visibility_of_element_located((By.XPATH, "(//span[normalize-space()='379'])[1]")))


# Extract the visible text 379
result_text_content = result_text.text
print(f"Full Text: {result_text_content}")


#New mission for find out all the customers

#Wait for the customer names to be visible in the list
#Wait for the table to load
wait5 = WebDriverWait(driver, 1000)
rows = wait5.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr")
           ))

# Loop through each row and fetch the customer's details
print(f"Total customers found: {len(rows)}")

for index, row in enumerate(rows, start=1):
       # Fetch customer name from the first column (td[1])
        customer_name = row.find_element(By.XPATH, "./td[1]").text  # Relative XPath to fetch name from current row
        print(f"Customer {index}: {customer_name}")

