# Mobile Test Automation Framework

A cross-platform test automation framework for Android and iOS applications using Python, Appium, and Pytest with advanced reporting capabilities.

## Features

- 🚀 Cross-platform support (Android & iOS)
- 📱 Appium-powered mobile automation
- 📊 Dual reporting system (Allure & pytest-html)
- 🏗️ Page Object Model with Selenium Page Factory
- 🎯 Selective test execution
- ⏱️ Automatic report opening post-execution
- 🔧 Configurable through INI files
- 🏷️ Tag-based test categorization

## Prerequisites

- Python 3.8+
- Appium Server 2.0+
- Node.js (for Appium installation)
- Android SDK/Xcode (depending on platform)
- [iOS] WebDriverAgent setup
- Java Development Kit (JDK 8+)

## Installation

1. **Clone Repository**
   ```bash
   git clone https://github.com/masudr4n4/ios-test-automation-appium.git
   cd ios-test-automation-appium
   
Folder structure
```
.
├── app
│   ├── android
│   │   └── General-Store.apk
│   └── ios
│       └── temp.txt
├── config
│   ├── logging.conf
│   └── properties.ini
├── pages
│   ├── android_pages
│   │   ├── __pycache__
│   │   └── home_page.py
│   └── ios_pages
│       ├── __pycache__
│       └── reminder_page.py
├── reports
│   ├── allure_report
│   ├── htmlreport
│   │   └── assets
│   ├── logs
│   ├── screenshots
│   │   ├── failed
│   │   └── passed
│   └── xml_report
│       └── regression_2025-04-28_09-51-48-PM_report.xml
├── tests
│   ├── __pycache__
│   │   └── conftest.cpython-311-pytest-8.3.5.pyc
│   ├── test_android
│   │   ├── __pycache__
│   │   └── test_sample.py
│   ├── test_ios
│   │   ├── __pycache__
│   │   └── test_reminders.py
│   ├── conftest.py
│   └── final.py
├── utils
│   ├── __pycache__
│   │   ├── common.cpython-311.pyc
│   │   ├── config.cpython-311.pyc
│   │   └── data.cpython-311.pyc
│   ├── locators
│   │   ├── __pycache__
│   │   ├── android_locators.py
│   │   └── ios_locators.py
│   ├── common.py
│   ├── config.py
│   ├── data.py
│   ├── mailutils.py
│   └── testdata.xlsx
├── CHANGELOG.md
├── README.md
├── README_FOR_INSTALLATION.md
├── device_capabilities.json
├── installation_script.py
├── ios_device_capabilities.json
├── packages.json
├── pytest.ini
└── requirements.txt

```

### Report Types

* 📈 Interactive Allure Dashboard
* 📄 Static HTML Report
* 📂 XML Results for CI integration