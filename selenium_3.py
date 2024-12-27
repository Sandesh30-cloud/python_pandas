from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.youtube.com")
    driver.maximize_window()

    search_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "search_query"))
    )
    search_box.send_keys("selenium with python")
    search_box.send_keys(Keys.ENTER)

    time.sleep(5)  

finally:
    time.sleep(30)
    driver.quit()
