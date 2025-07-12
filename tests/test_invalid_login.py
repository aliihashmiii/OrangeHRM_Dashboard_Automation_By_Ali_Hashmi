# test_invalid_login.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Setup Chrome
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  # Keeps browser open
service = Service()  # Uses default ChromeDriver from PATH

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")

# Wait for login page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))

# Step 1: Enter invalid credentials
driver.find_element(By.NAME, "username").send_keys("wrong_user")
driver.find_element(By.NAME, "password").send_keys("wrong_pass")

# Step 2: Click login
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Step 3: Wait for error to appear
time.sleep(2)

# Step 4: Save screenshot
if not os.path.exists("Screenshots"):
    os.mkdir("Screenshots")

driver.save_screenshot("../Screenshots/invalid_login.png")
print("✅ Test complete. Screenshot saved at Screenshots/invalid_login.png")

