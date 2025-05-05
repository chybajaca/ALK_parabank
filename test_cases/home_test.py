from test_cases.base_test import BaseTest
from time import sleep

# TODO: wrzucic tutaj testy klikania różnych zakładek na home page

class HomeTopTest(BaseTest):

    def testAboutUsTab(self):

        """
        Checking in the About Us tab
        :return:
        """

        # 1. Click on About Us hyperlink
        self.home_page.click_top_about_us()
        sleep(2)

        # Correct text assertion "ParaSoft Demo Website"
        self.assertEqual("ParaSoft Demo Website", self.home_page.get_about_us_text())

    def testServicesTab(self):

        """
        Checking in the Services tab
        :return:
        """

        # 1. Click on Services hyperlink
        self.home_page.click_top_services()
        sleep(2)

        # Correct text assertion "Available Bookstore SOAP services:"
        self.assertEqual("Available Bookstore SOAP services:", self.home_page.get_services_text())

    def testProductsTab(self):

        """
        Checking in the Products tab
        :return:
        """

        # 1. Click on Products hyperlink
        self.home_page.click_top_products()
        sleep(2)

        # Correct text assertion "Try Parasoft"
        self.assertEqual("Try Parasoft", self.home_page.get_products_text())

    def testLocationsTab(self):

        """
        Checking in the Locations tab
        :return:
        """

        # 1. Click on Locations hyperlink
        self.home_page.click_top_locations()
        sleep(2)

        # Correct text assertion "Try Parasoft"
        self.assertEqual("Try Parasoft", self.home_page.get_locations_text())

    def testAdminPageTab(self):

        """
        Checking in the Admin Page tab
        :return:
        """

        # 1. Click on Admin Page hyperlink
        self.home_page.click_top_admin_page()
        sleep(2)

        # Correct text assertion "Administration"
        self.assertEqual("Administration", self.home_page.get_admin_page_text())

class HomeButtonsTest(BaseTest):

    def testHomeButton(self):

        """
        Checking in the Home button for not logged-in user
        :return:
        """

        # 1. Click on About Us hyperlink
        self.home_page.click_top_about_us()
        sleep(2)

        # 2. Click on Home button
        self.home_page.click_home_button()
        sleep(2)

        # Correct text assertion "ATM Services"
        self.assertEqual("ATM Services", self.home_page.get_home_button_text())

    def testAboutUsButton(self):

        """
        Checking in the About Us button
        :return:
        """

        # 1. Click on About Us button
        self.home_page.click_about_us_button()
        sleep(2)

        # Correct text assertion "ParaSoft Demo Website"
        self.assertEqual("ParaSoft Demo Website", self.home_page.get_about_us_text())

    def testContactButton(self):

        """
        Checking in the Contact button
        :return:
        """

        # 1. Click on Contact button
        self.home_page.click_contact_button()
        sleep(2)

        # Correct text assertion "Customer Care"
        self.assertEqual("Customer Care", self.home_page.get_contact_button_text())

class HomeATMServicesTest(BaseTest):

    def testATMWithdrawFunds(self):

        """
        Checking in the Withdraw Funds hyperlink
        :return:
        """

        # 1. Click on Withdraw Funds hyperlink
        self.home_page.click_atm_withdraw_funds()
        sleep(2)

        # Correct id assertion "ATM Services"
        self.assertTrue(self.home_page.get_atm_services_id())

    def testATMTransferFunds(self):

        """
        Checking in the Transfer Funds hyperlink
        :return:
        """

        # 1. Click on Withdraw Funds hyperlink
        self.home_page.click_atm_transfer_funds()
        sleep(2)

        # Correct id assertion "ATM Services"
        self.assertTrue(self.home_page.get_atm_services_id())

    def testATMCheckBalances(self):

        """
        Checking in the Check Balances hyperlink
        :return:
        """

        # 1. Click on Check Balances hyperlink
        self.home_page.click_atm_check_balances()
        sleep(2)

        # Correct id assertion "ATM Services"
        self.assertTrue(self.home_page.get_atm_services_id())

    def testATMMakeDeposits(self):

        """
        Checking in the Make Deposits hyperlink
        :return:
        """

        # 1. Click on Make Deposits hyperlink
        self.home_page.click_atm_make_deposits()
        sleep(2)

        # Correct id assertion "ATM Services"
        self.assertTrue(self.home_page.get_atm_services_id())