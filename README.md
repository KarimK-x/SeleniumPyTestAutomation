# SeleniumPyTestAutomation

## Overview
This project demonstrates comprehensive software testing practices using Python, Selenium WebDriver, and Pytest. It is designed to showcase my understanding of automated UI testing, test case design, and best practices in real-world Agile QA workflow. The project is structured for clarity, maintainability, and scalability, making it suitable for real-world software testing scenarios.

## Features
- **Automated UI Testing**: Uses Selenium WebDriver to automate browser interactions for login and password change functionalities.
- **Pytest Framework**: Leverages Pytest for test organization, fixtures, and reporting.
- **Test Case Design**: Includes well-documented test cases covering positive and negative scenarios.
- **Modular Structure**: Separates test logic, configuration, and test data for maintainability.
- **Best Practices**: Follows industry standards for test automation, including the use of fixtures, assertions, and clear test naming.

## Project Structure
```
SeleniumPythonLoginAutomation/
├── backlog.md                # Project backlog and feature ideas
├── sprint-plan.md            # Sprint planning documentation
├── test-case.md              # Test case documentation
├── selenium-ui-tests/
│   ├── conftest.py           # Pytest fixtures and setup
│   ├── requirements.txt      # Python dependencies
│   └── tests/
│       ├── test_change_password.py  # Change password tests
│       └── test_login.py           # Login tests
```

## How to Run
1. **Install Dependencies**
   ```bash
   pip install -r selenium-ui-tests/requirements.txt
   ```
2. **No Need to Download ChromeDriver**
   - The test fixture is set up with ChromeDriverManager, which automatically downloads and manages the correct version of ChromeDriver. No manual setup is required.
3. **Run Tests**
   ```bash
   pytest selenium-ui-tests/tests/
   ```

## Key Files
- `selenium-ui-tests/tests/test_login.py`: Contains automated tests for login functionality.
- `selenium-ui-tests/tests/test_change_password.py`: Contains automated tests for password change scenarios.
- `selenium-ui-tests/conftest.py`: Defines fixtures for browser setup and teardown.
- `selenium-ui-tests/requirements.txt`: Lists all required Python packages.
- `test-case.md`: Documents the test cases and scenarios covered.
- `sprint-plan.md` & `backlog.md`: Show project planning and agile practices.

## Software Testing Concepts Demonstrated
- Test automation using Selenium and Pytest
- Test case documentation and traceability
- Use of fixtures for setup/teardown
- Assertion strategies for validation
- Modular and maintainable test code
- Agile testing practices (backlog, sprint planning)

## Why This Project?
This repository highlights my ability to design, implement, and document automated software tests in a professional manner. It demonstrates not only technical proficiency with Selenium and Pytest, but also a strong understanding of software testing methodologies and best practices.

---

**Author:** Karim Khaled
