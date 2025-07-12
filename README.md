#  OrangeHRM Dashboard Automation Project (POM-Based)

This is a Selenium-based automation testing suite that uses the **Page Object Model (POM)** design pattern.  
It includes:

-  **Valid login test** — Verifies successful login and dashboard visibility  
-  **Invalid login test** — Ensures proper failure message for wrong credentials

 Target Website: [OrangeHRM Demo Site](https://opensource-demo.orangehrmlive.com)

---

##  Project Author

**Ali Hashmi**  
Business student delving into devops by replacing 4 years of university knowledge with self learning

---

##  Project Folder Structure

OrangeHRM_Dashboard_Automation_By_Ali_Hashmi/
│
├── pages/ # Page Object Model (POM) files
│ ├── login_page.py # LoginPage class with actions
│ └── dashboard_page.py # DashboardPage class with dashboard check
│
├── tests/ # Test scripts
│ ├── init.py
│ ├── test_dashboard.py #  Valid login + dashboard visible test
│ └── test_invalid_login.py #  Invalid login + screenshot capture
│
├── Screenshots/ # Contains screenshot of invalid login result
│ └── invalid_login.png # (Auto-saved after running invalid login test)
│
└── README.md # You are here 

---

##  Technologies Used

| Tool | Purpose |
|------|---------|
| `Python 3.x` | Programming Language |
| `Selenium WebDriver` | Web browser automation |
| `ChromeDriver` | Interface for Selenium to run Chrome |
| `POM Design Pattern` | Reusable, clean test structure |
| `Git & GitHub` | Version control & portfolio hosting |
| `Notepad + PowerShell` | IDE and terminal (for beginners) |

---

## Tests Implemented

| Test Name | Description |
|-----------|-------------|
| `test_dashboard.py` | Logs in with valid credentials and checks if dashboard appears |
| `test_invalid_login.py` | Attempts login with wrong credentials and saves screenshot of failure |

---

##  Screenshot Example

>  Screenshot auto-saves to `Screenshots/invalid_login.png` when the test fails.
> Useful for reporting and debugging!

---

##  How to Run the Tests

### 1. Clone or Download the Repo

```bash
git clone https://github.com/aliihashmiii/OrangeHRM_Dashboard_Automation_By_Ali_Hashmi.git
cd OrangeHRM_Dashboard_Automation_By_Ali_Hashmi

2. Install Dependencies
pip install selenium

3. Run the Tests
python -m tests.test_dashboard
python -m tests.test_invalid_login
