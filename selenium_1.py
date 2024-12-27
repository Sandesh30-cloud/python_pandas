# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# print("Test case started")

# # Initialize the WebDriver
# driver = webdriver.Chrome()

# # Maximize the browser window
# driver.maximize_window()

# # Clear all cookies
# driver.delete_all_cookies()

# # Open Gmail
# driver.get("https://www.gmail.com")

# # Wait for the email input field to load and send the email address
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "identifierId"))).send_keys("yesanesandesh.in@gmail.com")

# # Click the "Next" button after entering the email
# driver.find_element(By.XPATH, "//span[@class='RveJvd snByac']").click()  # Using simpler XPath
# time.sleep(5)

# # Wait for the password field to load and send the password
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("#")

# # Click the "Next" button after entering the password
# driver.find_element(By.XPATH, "//span[contains(text(),'Next')]").click()  # Improved XPath
# time.sleep(5)

# # Close the browser
# driver.close()

# print("Gmail login has been successfully completed")


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Navigate to Gmail login page
driver.get("https://www.gmail.com")

# Wait for the email input field to load and send the email address
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "identifierId"))).send_keys("yesanesandesh.in@gmail.com")

# Click the "Next" button after entering the email
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='VfPpkd-RLmnJb']"))).click()

# Wait for password input field to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("#@spy123")

# Wait for and click the "Next" button after entering the password
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Next')]"))).click()

# Optionally wait a few seconds before closing the browser (if necessary for observation)
time.sleep(5)

# Close the browser
driver.quit()

print("Test case completed")
