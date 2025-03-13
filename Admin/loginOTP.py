import time
import imaplib
import email
from email.header import decode_header
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from CommonLogin import login_to_application  # Import reusable login function

# Function to fetch OTP from Gmail
def fetch_otp_from_gmail(username, password):
    try:
        # Connect to Gmail's IMAP server
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(username, password)
        mail.select("inbox")  # Open the inbox

        # Search for emails that are UNSEEN (new emails)
        status, messages = mail.search(None, 'UNSEEN')
        if status != "OK":
            print("No new messages.")
            return None

        # Get the latest email
        messages = messages[0].split()
        latest_email_id = messages[-1]

        # Fetch the email
        status, msg_data = mail.fetch(latest_email_id, "(RFC822)")
        if status != "OK":
            print("Failed to retrieve email.")
            return None

        # Parse the email
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding if encoding else 'utf-8')

                # Check if the email contains the OTP (example for subject)
                if "OTP" in subject or "Verification Code" in subject:
                    # Get the OTP from the email body
                    if msg.is_multipart():
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))

                            # Get the email content
                            if content_type == "text/plain" and "attachment" not in content_disposition:
                                body = part.get_payload(decode=True).decode()
                                # Extract OTP from the email body (assuming OTP is a 6-digit number)
                                otp = ''.join(filter(str.isdigit, body))  # This will extract only the digits
                                print(f"OTP: {otp}")
                                return otp
                    else:
                        body = msg.get_payload(decode=True).decode()
                        otp = ''.join(filter(str.isdigit, body))  # This will extract only the digits
                        print(f"OTP: {otp}")
                        return otp
        return None
    except Exception as e:
        print(f"Failed to fetch OTP: {e}")
        return None

# Setup WebDriver
driver = webdriver.Chrome()
driver.maximize_window()  # Ensure all elements are visible

# Define login details
LOGIN_URL = "https://admin-ptm-panel.paytome.co/login"
USERNAME = "------"  # Gmail username (email)
PASSWORD = "--------------"  # Gmail password or app-specific password

# Call the reusable login function
login_to_application(driver, USERNAME, PASSWORD, LOGIN_URL)

# Wait for OTP prompt in the application
wait = WebDriverWait(driver, 30)
otp_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='otp-input']")))

# Fetch OTP from Gmail
otp = fetch_otp_from_gmail(USERNAME, PASSWORD)
if otp:
    # Enter the OTP in the input field
    otp_input.send_keys(otp)
    print("OTP entered successfully!")
else:
    print("Failed to fetch OTP.")

# Continue with the rest of the test steps after OTP entry
print("Proceeding with test steps...")
