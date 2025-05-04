import unittest
from selenium import webdriver
from pages.home_page import HomePage
from pages.logged_page import LoggedInPage
from pages.register_page import RegisterPage

class BaseTest(unittest.TestCase):
    """
    Base class for each test
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://parabank.parasoft.com/parabank/index.htm")
        self.home_page = HomePage(self.driver)
        self.logged_page = LoggedInPage(self.driver)
        self.register_page = RegisterPage(self.driver)

    def TearDown(self):
        self.driver.quit()