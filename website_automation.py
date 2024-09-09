from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Provide the path to your WebDriver (optional if it's already in PATH)
web = webdriver.Chrome()

# Open Amazon sign-in page
web.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
time.sleep(1)

# Locate the email/phone number input field and input a dummy value
login = web.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/form/div/div/div/div[1]/input[1]")
login.send_keys("silentswordfish2004@gmail.com")

# Locate the submit button and click it
submit_button = web.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/form/div/div/div/div[2]/span/span/input")
submit_button.click()

# Wait for the page to load after submitting the email
time.sleep(2)

# Locate the password input field and input a password
pass_key = web.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[2]/div/form/div/div[1]/input")
pass_key.send_keys("pass")

# Locate the submit button for the password and click it
pass_submit = web.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[2]/div/form/div/div[2]/span/span/input")
pass_submit.click()

# Wait for the page to load completely after submitting the password
time.sleep(3)

# Take a screenshot and save it to the current directory with a file name
web.save_screenshot('amazon_login_screenshot.png')

# Alternatively, provide a full path where the screenshot will be saved
# web.save_screenshot('/path/to/your/folder/amazon_login_screenshot.png')

# Close the browser
web.quit()
