from pages.base_page import BasePage
# from pages.home_page import HomePageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LoggedInPageLocators:
    """
    Logged In Page locators
    """

    # ACCOUNT SERVICES, MIDDLE LEFT OF THE SCREEN
    WELCOME_FULL_NAME = (By.XPATH, '//*[@id="leftPanel"]/p')
    AS_OPEN_NEW_ACCOUNT = (By.XPATH, '//*[@id="leftPanel"]/ul/li[1]/a')
    AS_ACCOUNTS_OVERVIEW = (By.XPATH, '//*[@id="leftPanel"]/ul/li[2]/a')
    AS_TRANSFER_FUNDS = (By.XPATH, '//*[@id="leftPanel"]/ul/li[3]/a')
    AS_BILL_PAY = (By.XPATH, '//*[@id="leftPanel"]/ul/li[4]/a')
    AS_FIND_TRANSACTIONS = (By.XPATH, '//*[@id="leftPanel"]/ul/li[5]/a')
    AS_UPDATE_CONTACT_INFO = (By.XPATH, '//*[@id="leftPanel"]/ul/li[6]/a')
    AS_REQUEST_LOAN = (By.XPATH, '//*[@id="leftPanel"]/ul/li[7]/a')
    AS_LOG_OUT = (By.XPATH, '//*[@id="leftPanel"]/ul/li[8]/a')

class LoggedInPage(BasePage):
    """
    Login Page object
    """

    def get_welcome_fullname_text(self):
        """
        Gets "Welcome <firstname> <lastname>" message in the middle left of the screen
        :return: Welcome <firstname> <lastname> text
        """

        # After logging in
        # Waiting for Welcome <firstname> <lastname>
        self.wait_5s.until(EC.text_to_be_present_in_element(LoggedInPageLocators.WELCOME_FULL_NAME, "Welcome"))
        return self.driver.find_element(*LoggedInPageLocators.WELCOME_FULL_NAME).text

    def click_log_out(self):

        """
        Clicks log out link
        :return: LoginPage instance
        """

        # While logged in
        # Find log out button and click on it
        self.driver.find_element(*LoggedInPageLocators.AS_LOG_OUT).click()




    # TODO: Click on each account service

    # def _verify_page(self):
    #     self.wait_5s.until(EC.visibility_of_element_located(HomePageLocators.LOG_IN_USERNAME_I))
    #     self.wait_5s.until(EC.visibility_of_element_located(HomePageLocators.LOG_IN_PASSWORD_I))
    #     log_in_button = self.driver.find_element(*HomePageLocators.LOG_IN_BUTTON)
    #     self.wait_5s.until(EC.element_to_be_clickable(log_in_button))