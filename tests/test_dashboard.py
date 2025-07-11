# Author: Ali Hashmi
# File: test_dashboard.py
# Description: Full POM-based automation test that verifies the dashboard is visible after login.

import time
from selenium import webdriver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

print("🚀 Starting test_dashboard.py")

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(2)

# Login
login = LoginPage(driver)
login.login("Admin", "admin123")
time.sleep(2)

# Validate dashboard
dashboard = DashboardPage(driver)
if dashboard.is_dashboard_displayed():
    print("✅ Dashboard is visible — Test Passed")
else:
    print("❌ Dashboard not found — Test Failed")
    driver.save_screenshot("Screenshots/dashboard_not_found.png")

driver.quit()

