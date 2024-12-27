from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

print("Here the sample test case will be started")

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.google.com/")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("javatpoint")
time.sleep(3)

search_box.send_keys(Keys.ENTER)
time.sleep(3)

driver.close()

print("Sample test case successfully completed")
