# 🎭 SoftTechverse Education Portal — BDD Test Automation Framework

![Project Banner](assets/banner.jpg)

[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/selenium-4.21.0-green.svg)](https://www.selenium.dev/)
[![BDD](https://img.shields.io/badge/behave-1.2.6-orange.svg)](https://behave.readthedocs.io/)

A professional, enterprise-grade test automation suite built for the **SoftTechverse Education Portal** (`https://education.softtechverse.com`). This project implements the **Page Object Model (POM)** design pattern combined with **Behavior-Driven Development (BDD)** using Python's **Behave** framework and **Selenium WebDriver**.

---

## 🌟 Framework Key Features

- **Behavior-Driven Development (BDD)**: Written in Gherkin syntax, enabling collaboration between QA, developers, and non-technical stakeholders.
- **Page Object Model (POM)**: Enhances code maintainability and reusability by separating page interactions from step definitions.
- **Driver Auto-Resolution**: Integrates `webdriver-manager` with custom 64-bit architecture resolution to prevent binary mismatch crashes.
- **Fail-Safe Screenshots**: Automatic screenshot capture on scenario failures, stored in `reports/screenshots/`.
- **Robust Synchronization**: Handled dynamic page loading with Selenium's explicit waits, bypassing redirect loops caused by expired portal subscriptions.

---

## 📂 Project Structure

```text
SoftTechverse/
│
├── features/                           # Gherkin Scenario Files (.feature)
│   ├── authentication/
│   │   └── login.feature               # Login validation (smoke and negative scenarios)
│   ├── dashboard/
│   │   └── dashboard.feature           # Verifies dashboard rendering and main layouts
│   ├── students/
│   │   └── student_management.feature  # Sidebar expansion and Student List visibility
│   └── navigation/
│       └── navigation.feature          # Direct access redirects for unauthenticated users
│
├── steps/                              # Python Step Definitions
│   ├── auth_steps.py                   # Authentication step implementations
│   ├── dashboard_steps.py              # Dashboard assertions and setups
│   ├── student_steps.py                # Student module interaction steps
│   └── navigation_steps.py             # Route security checks
│
├── pages/                              # Page Object Model Class Files
│   ├── base_page.py                    # Wrapper for selenium actions (clicks, types, waits)
│   ├── login_page.py                   # Locators & actions for the Authentication page
│   ├── dashboard_page.py               # Locators & actions for the Dashboard panel
│   ├── student_page.py                 # Locators & actions for the Student Details section
│   └── navigation_page.py              # Navigation links handlers
│
├── utils/                              # Framework Configuration & Utilities
│   ├── config.py                       # Global variables, base URL, timeouts, and credentials
│   └── driver_factory.py               # Multi-browser setup factory (Chrome, Firefox, Edge)
│
├── environment.py                      # Behave hooks for setup, teardown & error screenshots
├── behave.ini                          # Behave global runner configuration
├── requirements.txt                    # Project python dependencies
└── .gitignore                          # Exclusions for python caches, virtual envs, and report outputs
```

---

## 📋 Scenarios Covered

| Feature | Scenario | Tags | Objective |
|---|---|---|---|
| **User Authentication** | Successful login with valid credentials | `@smoke`, `@login` | Checks that valid credentials redirect successfully to the dashboard. |
| **User Authentication** | Login fails with invalid credentials | `@login`, `@negative` | Confirms validation errors and ensures user remains on login page. |
| **Dashboard Verification**| Dashboard loads after login | `@smoke`, `@dashboard`| Verifies page layout elements and sidebar rendering. |
| **Navigation Security** | Unauthenticated user is redirected | `@smoke`, `@navigation`| Ensures direct URL access without session redirects back to login page. |
| **Student Management** | Expand Student Details menu | `@smoke`, `@student` | Confirms sidebar submenu navigation works correctly. |

---

## 🚀 Setup & Execution Guide

Follow these steps to set up the environment and run the test suite locally.

### 1. Clone the repository
```bash
git clone <your-repository-url>
cd SoftTechverse
```

### 2. Configure Virtual Environment
Create and activate a Python virtual environment to manage dependencies:
```bash
# Create environment
python -m venv myenv

# Activate on Windows (PowerShell)
myenv\Scripts\activate

# Activate on macOS/Linux
source myenv/bin/activate
```

### 3. Install Requirements
Install all dependencies listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Execute Automated Suite
Run the test command in your terminal:
```bash
# Run all scenarios
behave

# Run only smoke scenarios
behave --tags=@smoke

# Run with stdout output enabled
behave --no-capture --no-capture-stderr
```

---

## ⚙️ Configuration File (`utils/config.py`)

You can easily toggle parameters like target browser and timeouts in `utils/config.py`:
```python
BASE_URL = "https://education.softtechverse.com"
TIMEOUT = 15          # Explicit wait time limits (seconds)
BROWSER = "chrome"    # Multi-browser selection: 'chrome' | 'firefox' | 'edge'
```
