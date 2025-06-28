import unittest
import HtmlTestRunner
import os


# Path to reports folder
reports_dir = 'test_reports'
os.makedirs(reports_dir, exist_ok=True)

# Creating a loader and automatically searching for tests in the test_cases folder
loader = unittest.TestLoader()
register_tests = loader.discover(start_dir='test_cases', pattern='register_test.py')
login_tests = loader.discover(start_dir='test_cases', pattern='login_test.py')
homepage_tests = loader.discover(start_dir='test_cases', pattern='home_test.py')

# Combine tests to run

tests = unittest.TestSuite()
for test_suite in [
    # login_tests,
    homepage_tests,
    # register_tests
                   ]:
    for test in test_suite:
        tests.addTests(test)

# Running tests with HTML report generation
runner = HtmlTestRunner.HTMLTestRunner(
    output=reports_dir,
    report_name=f"TestReport",
    combine_reports=True,
    verbosity=3
)

runner.run(tests)
