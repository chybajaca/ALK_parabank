from test_cases.base_test import BaseTest
from time import sleep

class HomeTest(BaseTest):

    # TODO: wrzucic tutaj testy klikania różnych zakładek na home page

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