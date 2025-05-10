import unittest
import HtmlTestRunner

# from test_cases.home_test import HomeTopTabsTest
# from test_cases.home_test import HomeButtonsTest
# from test_cases.home_test import HomeATMServicesTest
# from test_cases.home_test import HomeOnlineServicesTest
# from test_cases.home_test import HomeLatestNewsTest
# from test_cases.home_test import HomeReadMoreTest
# from test_cases.home_test import HomeBottomTabsTest
# from test_cases.login_test import LoginTest
from test_cases.register_test import RegisterTest


# Loading the tests
# top_tabs_tests = unittest.TestLoader().loadTestsFromTestCase(HomeTopTabsTest)
# button_tests = unittest.TestLoader().loadTestsFromTestCase(HomeButtonsTest)
# atm_services_tests = unittest.TestLoader().loadTestsFromTestCase(HomeATMServicesTest)
# online_services_tests = unittest.TestLoader().loadTestsFromTestCase(HomeOnlineServicesTest)
# latest_news_tests = unittest.TestLoader().loadTestsFromTestCase(HomeLatestNewsTest)
# read_more_tests = unittest.TestLoader().loadTestsFromTestCase(HomeReadMoreTest)
# bottom_tabs_tests = unittest.TestLoader().loadTestsFromTestCase(HomeBottomTabsTest)
# login_tests = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
register_tests = unittest.TestLoader().loadTestsFromTestCase(RegisterTest)

# List of tests to run (modify as needed)
tests_for_run = [

    register_tests,
    # login_tests,
    # top_tabs_tests,
    # button_tests,
    # atm_services_tests,
    # online_services_tests,
    # latest_news_tests,
    # read_more_tests,
    # bottom_tabs_tests,

]

# Creating the Test Suite
test_suite = unittest.TestSuite(tests_for_run)

# Running the tests with HTML report generation
runner = HtmlTestRunner.HTMLTestRunner(
    output='test_reports',                # destination path
    report_name="TestReport",   # Just use a static name (timestamp will be added automatically)
    combine_reports=True,           # summary into one file
    verbosity=2                      # report level of details
)

runner.run(test_suite)