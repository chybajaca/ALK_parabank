from test_cases.base_test import BaseTest
from time import sleep


class HomeTopTabsTest(BaseTest):

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

class HomeOnlineServicesTest(BaseTest):

    def testOSBillPay(self):

        """
        Checking in the Bill Pay hyperlink
        :return:
        """

        # 1. Click on Bill Pay hyperlink
        self.home_page.click_os_bill_pay()
        sleep(2)

        # Correct id assertion "ATM Services"
        self.assertTrue(self.home_page.get_online_services_id())

    def testOSAccountHistory(self):

        """
        Checking in the Account History hyperlink
        :return:
        """

        # 1. Click on Account History hyperlink
        self.home_page.click_os_account_history()
        sleep(2)

        # Correct id assertion "ATM Services"
        self.assertTrue(self.home_page.get_online_services_id())

    def testOSTransferFunds(self):

        """
        Checking in the Transfer Funds hyperlink
        :return:
        """

        # 1. Click on Transfer Funds hyperlink
        self.home_page.click_os_transfer_funds()
        sleep(2)

        # Correct id assertion "ATM Services"
        self.assertTrue(self.home_page.get_online_services_id())

class HomeLatestNewsTest(BaseTest):

    def testLNFirstNews(self):

        """
        Checking in the first news from the top of the ParaBank News
        :return:
        """

        # 1. Click on first news hyperlink
        self.home_page.click_ln_first_news()
        sleep(2)

        # Correct text assertion "ParaBank News"
        self.assertEqual("ParaBank News", self.home_page.get_parabank_news_text())

    def testLNSecondNews(self):

        """
        Checking in the second news from the top of the ParaBank News
        :return:
        """

        # 1. Click on second news hyperlink
        self.home_page.click_ln_second_news()
        sleep(2)

        # Correct text assertion "ParaBank News"
        self.assertEqual("ParaBank News", self.home_page.get_parabank_news_text())

    def testLNThirdNews(self):

        """
        Checking in the third news from the top of the ParaBank News
        :return:
        """

        # 1. Click on third news hyperlink
        self.home_page.click_ln_third_news()
        sleep(2)

        # Correct text assertion "ParaBank News"
        self.assertEqual("ParaBank News", self.home_page.get_parabank_news_text())

class HomeReadMoreTest(BaseTest):

    def testReadMoreServices(self):

        """
        Checking in the Read More button below the Services table
        :return:
        """

        # 1. Click on Read More button below the Services table
        self.home_page.click_read_more_services()
        sleep(2)

        # Correct text assertion "Available Bookstore SOAP services:"
        self.assertEqual("Available Bookstore SOAP services:", self.home_page.get_services_text())

    def testReadMoreLatestNews(self):

        """
        Checking in the Read More button below the Latest News table
        :return:
        """

        # 1. Click on Read More button below the Latest News table
        self.home_page.click_read_more_latest_news()
        sleep(2)

        # Correct text assertion "ParaBank News"
        self.assertEqual("ParaBank News", self.home_page.get_parabank_news_text())

class HomeBottomTabsTest(BaseTest):

    def testHomeTab(self):

        """
        Checking in the Home hyperlink on the bottom of the page
        :return:
        """

        # 1. Click on Home hyperlink
        self.home_page.click_bottom_home()
        sleep(2)

        # Correct text assertion "ATM Services"
        self.assertEqual("ATM Services", self.home_page.get_home_button_text())

    def testAboutUsTab(self):

        """
        Checking in the About Us hyperlink on the bottom of the page
        :return:
        """

        # 1. Click on About Us hyperlink
        self.home_page.click_bottom_about_us()
        sleep(2)

        # Correct text assertion "ParaSoft Demo Website"
        self.assertEqual("ParaSoft Demo Website", self.home_page.get_about_us_text())

    def testServicesTab(self):

        """
        Checking in the Services hyperlink on the bottom of the page
        :return:
        """

        # 1. Click on Services hyperlink
        self.home_page.click_bottom_services()
        sleep(2)

        # Correct text assertion "Available Bookstore SOAP services:"
        self.assertEqual("Available Bookstore SOAP services:", self.home_page.get_services_text())

    def testProductsTab(self):

        """
        Checking in the Products hyperlink on the bottom of the page
        :return:
        """

        # 1. Click on Products hyperlink
        self.home_page.click_bottom_products()
        sleep(2)

        # Correct text assertion "Try Parasoft"
        self.assertEqual("Try Parasoft", self.home_page.get_products_text())

    def testLocationsTab(self):

        """
        Checking in the Locations hyperlink on the bottom of the page
        :return:
        """

        # 1. Click on Locations hyperlink
        self.home_page.click_bottom_locations()
        sleep(2)

        # Correct text assertion "Try Parasoft"
        self.assertEqual("Try Parasoft", self.home_page.get_locations_text())

    def testSiteMapTab(self):

        """
        Checking in the Site Map hyperlink on the bottom of the page
        :return:
        """

        # 1. Click on Site Map hyperlink
        self.home_page.click_bottom_site_map()
        sleep(2)

        # Correct text assertion "Try Parasoft"
        self.assertEqual("Solutions", self.home_page.get_site_map_text())

    def testContactUsTab(self):

        """
        Checking in the Contact Us hyperlink on the bottom of the page
        :return:
        """

        # 1. Click on Contact Us hyperlink
        self.home_page.click_bottom_contact_us()
        sleep(2)

        # Correct text assertion "Customer Care"
        self.assertEqual("Customer Care", self.home_page.get_contact_button_text())