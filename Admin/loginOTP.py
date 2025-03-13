import time
import imaplib
import email
from email.header import decode_header
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from CommonLogin import login_to_application  # Import reusable login function

# -------------------------------------------
# Define website login credentials (Used for website login)
# -------------------------------------------
WEBSITE_URL = "https://admin-ptm-panel.paytome.co/login"
WEBSITE_USERNAME = ""  # Website login email
WEBSITE_PASSWORD = ""          # Website login password

# -------------------------------------------
# Define Gmail credentials (Used for fetching OTP)
# -------------------------------------------
GMAIL_USERNAME = "itteam.9@aieus.com"  # Your Gmail email
GMAIL_PASSWORD = "BD.STBQA0708@"  # Your Gmail password (or App Password)

# -------------------------------------------
# Function to fetch OTP from Gmail
# -------------------------------------------
def fetch_otp_from_gmail(email_user, email_pass):
    try:
        # Connect to Gmail's IMAP server
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(email_user, email_pass)
        mail.select("inbox")  # Open the inbox

        # Search for unread OTP emails
        status, messages = mail.search(None, 'UNSEEN')
        if status != "OK" or not messages[0]:
            print("No new OTP emails found.")
            return None

        # Get the latest unread email
        latest_email_id = messages[0].split()[-1]

        # Fetch the email content
        status, msg_data = mail.fetch(latest_email_id, "(RFC822)")
        if status != "OK":
            print("Failed to retrieve email.")
            return None

        # Process the email content
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding if encoding else 'utf-8')

                # Check if the email contains an OTP
                if "OTP" in subject or "Verification Code" in subject:
                    # Extract OTP from email body
                    if msg.is_multipart():
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))

                            if content_type == "text/plain" and "attachment" not in content_disposition:
                                body = part.get_payload(decode=True).decode()
                                otp = ''.join(filter(str.isdigit, body))  # Extract digits only
                                print(f"Fetched OTP: {otp}")
                                return otp
                    else:
                        body = msg.get_payload(decode=True).decode()
                        otp = ''.join(filter(str.isdigit, body))  # Extract digits only
                        print(f"Fetched OTP: {otp}")
                        return otp
        return None
    except Exception as e:
        print(f"Failed to fetch OTP: {e}")
        return None

# -------------------------------------------
# Setup WebDriver & Perform Website Login
# -------------------------------------------
driver = webdriver.Chrome()
driver.maximize_window()  # Maximize browser window

# Log in to the website using the website credentials
login_to_application(driver, WEBSITE_USERNAME, WEBSITE_PASSWORD, WEBSITE_URL)

# -------------------------------------------
# Wait for OTP input field & fetch OTP from Gmail
# -------------------------------------------
wait = WebDriverWait(driver, 30)

try:
    # Wait for OTP input field to appear
    otp_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='------']")))

    # Fetch OTP from Gmail using Gmail credentials
    otp = fetch_otp_from_gmail(GMAIL_USERNAME, GMAIL_PASSWORD)

    if otp:
        # Enter OTP into the input field
        otp_input.send_keys(otp)
        print("OTP entered successfully!")

        # Click the Verify button
        verify_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Verify'])[1]")))
        verify_button.click()
        print("Verify button clicked successfully!")

    else:
        print("Failed to fetch OTP. Please check Gmail credentials or email format.")

except Exception as e:
    print(f"Error during OTP verification: {e}")

# Continue with test steps after OTP verification
print("Proceeding with next steps...")
