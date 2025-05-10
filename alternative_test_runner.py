import unittest
import HtmlTestRunner
import os


# Path to reports folder
reports_dir = 'test_reports'
os.makedirs(reports_dir, exist_ok=True)

# Creating a loader and automatically searching for tests in the test_cases folder
loader = unittest.TestLoader()
tests = loader.discover(start_dir='test_cases', pattern='register_test.py')

# Running tests with HTML report generation
runner = HtmlTestRunner.HTMLTestRunner(
    output=reports_dir,
    report_name=f"TestReport",
    combine_reports=True,
    verbosity=3
)

runner.run(tests)
