ParaBank Project - Selenium Automation with Python 3.12

Project Overview

    This project automates functional testing of the ParaBank web application using Selenium WebDriver and Python 3.12.
    The automation framework is organized following best practices such as the Page Object Model (POM)
    and modular test design, enabling maintainable, scalable, and reusable test scripts.


Project Structure

parabank_project/
│
├── pages/                  # Page Object Model classes
│   ├── base_page.py        # Base page with common methods
│   ├── home_page.py        # Home page interactions
│   ├── logged_page.py      # Logged-in user page interactions
│   └── register_page.py    # Registration page interactions
│
├── test_cases/             # Test scripts
│   ├── base_test.py        # Base test setup and teardown
│   ├── home_test.py        # Tests related to home page
│   ├── login_test.py       # Login functionality tests
│   └── register_test.py    # Registration functionality tests
│
├── test_data/              # Test data and data reader utility
│   ├── data_reader.py      # Utility to read test data (e.g., CSV)
│   └── valid_data.csv      # Sample valid test data
│
├── test_reports/           # Folder for test reports and logs
│
└── test_running.py         # Main script to run tests based on user preferences


Technologies & Dependencies

    Python 3.12
    Selenium WebDriver
    ChromeDriver
    Additional Python packages
    unittest testing framework

Key Features

    Page Object Model (POM): Encapsulates page elements and actions in dedicated classes for better maintainability.
    Modular Test Cases: Organized by functionality (home, login, registration).
    Data-Driven Testing: Test data is externalized in CSV files and read dynamically.
    Configurable Test Runner: test_running.py allows running specific tests or suites based on user input.
    Test Reports: Test results and logs are saved in the test_reports folder for analysis.


Prerequisites

    Python 3.12 installed on your machine
    Selenium installed (pip install selenium)
    Browser ChromeDriver installed and added to your system PATH
    Internet connection to access the ParaBank website


Setup Instructions

    1. Clone the repository

    git clone https://github.com/chybajaca/ALK_parabank
    cd parabank_project

    2. Install dependencies

    Run requirements.txt:
    pip install -r requirements.txt


    3. Ensure WebDriver is set up
    Download the ChromeDriver and place it in your system PATH or specify its
    location in your scripts.


How to Run Tests

    To run all tests or specific test modules, use the test_running.py script.
    This script provides options to select which tests to execute based on your preference.

    Follow the on-screen prompts to select tests or test suites.