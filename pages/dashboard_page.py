# Author: Ali Hashmi
# File: dashboard_page.py
# Description: POM for verifying that the Dashboard page is displayed.

from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.dashboard_heading = (By.XPATH, "//h6[text()='Dashboard']")

    def is_dashboard_displayed(self):
        try:
            return self.driver.find_element(*self.dashboard_heading).is_displayed()
        except:
            return False
