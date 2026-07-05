# SoftTechverse Education Portal BDD Test Automation Framework

This repository contains a professional BDD (Behavior-Driven Development) test automation framework for the SoftTechverse Education Portal using Python, Selenium WebDriver, and Behave.

---

## 🛠️ Tech Stack & Tools
- **Language**: Python 3.12+
- **BDD Framework**: Behave (Gherkin style syntax)
- **Browser Automation**: Selenium WebDriver 4
- **Design Pattern**: Page Object Model (POM)
- **Reporting**: Allure Reports / Custom HTML reports
- **Driver Management**: WebDriver Manager (Auto-resolves browser driver binaries)

---

## 📂 Project Structure

```text
SoftTechverse/
│
├── features/                           # Gherkin Scenario Files
│   ├── authentication/
│   │   └── login.feature               # Login valid/invalid checks
│   ├── dashboard/
│   │   └── dashboard.feature           # Stats & Sidebar widgets
│   ├── students/
│   │   └── student_management.feature  # Student list details menu checks
│   └── navigation/
│       └── navigation.feature          # Unauthenticated redirect checks
│
├── steps/                              # Python Step Definitions
│   ├── auth_steps.py
│   ├── dashboard_steps.py
│   ├── student_steps.py
│   └── navigation_steps.py
│
├── pages/                              # Page Object Model (POM) Layers
│   ├── base_page.py                    # Common element helpers & explicit waits
│   ├── login_page.py
│   ├── dashboard_page.py
│   ├── student_page.py
│   └── navigation_page.py
│
├── utils/                              # Configurations & Framework Drivers
│   ├── config.py                       # Global constants, credentials, timeouts
│   └── driver_factory.py               # Multibrowser driver initialization
│
├── environment.py                      # Behave hooks (setup & teardown browser instances)
├── behave.ini                          # Behave framework configurations
├── requirements.txt                    # Project dependency list
└── .gitignore                          # Unwanted files exclusions
```

---

## 🚀 Setup & Execution

### 1. Prerequisites
Ensure you have Python 3.12+ installed.

### 2. Install Dependencies
Initialize your virtual environment and install the required modules:
```bash
python -m venv myenv
myenv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run Automated Tests
Execute the test cases:
```bash
behave
```

---

## 💻 Git Branching Strategy
We follow a professional QA feature branching strategy:
- `main`: Production-ready automation scripts.
- `feature/<feature-name>`: Development/testing branch for new test coverage.
