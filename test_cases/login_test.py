from test_cases.base_test import BaseTest
from test_data.data_reader import DataReader
from ddt import data, unpack, ddt
from time import sleep
from faker import Faker

@ddt

class LoginTest(BaseTest):

    def testEmptyLogin(self):

        """
        Logging in test with empty username and password field.
        :return:
        """

        # 1. Click on Log In button
        self.home_page.click_log_in()

        # Correct alert assertion "Please enter a username and password."
        self.assertEqual("Please enter a username and password.", self.home_page.get_log_in_empty_error())
        sleep(2)

    def testInvalidLogin(self):

        """
        Logging in test with usage of invalid username and password.
        :return:
        """

        # 1. Enter username
        self.home_page.enter_username(Faker().user_name())

        # 2. Enter password
        self.home_page.enter_password(Faker(length=10).password())

        # 3. Click on Log In button
        self.home_page.click_log_in()
        sleep(2)

        # Correct alert assertion "An internal error has occurred and has been logged."
        self.assertEqual("The username and password could not be verified.",
                         self.home_page.get_log_in_invalid_error())
        sleep(2)

    def testOnlyUsernameLogin(self):

        """
        Logging in test with usage of username only.
        :return:
        """

        # 1. Enter username
        self.home_page.enter_username(Faker().user_name())

        # 2. Click on Log In button
        self.home_page.click_log_in()
        sleep(2)

        # Correct alert assertion "An internal error has occurred and has been logged."
        self.assertEqual("Please enter a username and password.",
                         self.home_page.get_log_in_empty_error())
        sleep(2)

    def testOnlyPasswordLogin(self):

        """
        Logging in test with usage of password only.
        :return:
        """

        # 1. Enter password
        self.home_page.enter_password(Faker(length=10).password())

        # 2. Click on Log In button
        self.home_page.click_log_in()
        sleep(2)

        # Correct alert assertion "An internal error has occurred and has been logged."
        self.assertEqual("Please enter a username and password.",
                         self.home_page.get_log_in_empty_error())
        sleep(2)

    @data(*DataReader.get_csv_data("test_data/valid_data.csv"))
    @unpack
    def testValidLogin(self, username, password, firstname, lastname):
        """
        Logging in test with usage of valid username and password.
        :return:
        """

        # 1. Enter username
        self.home_page.enter_username(username)

        # 2. Enter password
        self.home_page.enter_password(password)

        # 3. Click on Log In button
        self.home_page.click_log_in()

        # 4. Look for "Welcome <firstname> <lastname>" text
        welcome_text_act = self.logged_page.get_welcome_fullname_text()
        self.assertEqual(f"Welcome {firstname} {lastname}", welcome_text_act)

        # 5. Check if LogOut is visible and clickable
        self.logged_page.click_log_out()

        # 6. Look for "Customer Login" text for LogOut confirmation
        self.assertEqual("Customer Login", self.home_page.get_customer_login_text())
        sleep(2)