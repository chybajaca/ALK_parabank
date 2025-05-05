from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class HomePageLocators:
    """
    Home Page locators
    """
    #PARABANK LOGO, TOP OF THE SCREEN
    PARABANK_LOGO = (By.XPATH, '//*[@id="topPanel"]/a[2]/img')

    # CUSTOMER LOGIN, MIDDLE LEFT OF THE SCREEN
    class CustomerLogin:
        LOG_IN_USERNAME_I = (By.XPATH, '//*[@id="loginPanel"]/form/div[1]/input')
        LOG_IN_PASSWORD_I = (By.XPATH, '//*[@id="loginPanel"]/form/div[2]/input')
        LOG_IN_BUTTON = (By.XPATH, '//*[@id="loginPanel"]/form/div[3]/input')
        FORGOT_LOGIN_INFO = (By.XPATH, '//*[@id="loginPanel"]/p[1]/a')
        REGISTER_HYPERLINK = (By.XPATH, '//*[@id="loginPanel"]/p[2]/a')

        CUSTOMER_LOGIN_TEXT = (By.XPATH, '//*[@id="leftPanel"]/h2')
        EMPTY_LOGIN_CREDENTIALS_ERROR = (By.XPATH, '//*[@id="rightPanel"]/p')
        INVALID_LOGIN_CREDENTIALS_ERROR = (By.XPATH, '//*[@id="rightPanel"]/p')

    # TABS, LEFT TOP OF THE SCREEN
    class TopTabs:
        TOP_ABOUT_US = (By.XPATH, '//*[@id="headerPanel"]/ul[1]/li[2]/a')
        TOP_ABOUT_US_ASSERT = (By.XPATH, '//*[@id="rightPanel"]/h1')
        TOP_SERVICES = (By.XPATH, '//*[@id="headerPanel"]/ul[1]/li[3]/a')
        TOP_SERVICES_ASSERT = (By.XPATH, '//*[@id="rightPanel"]/span[1]')
        TOP_PRODUCTS = (By.XPATH, '//*[@id="headerPanel"]/ul[1]/li[4]/a')
        TOP_PRODUCTS_ASSERT = (By.XPATH, '/html/body/div[5]/header/div/div/div/nav[1]/ul/li[7]/a')
        TOP_LOCATIONS = (By.XPATH, '//*[@id="headerPanel"]/ul[1]/li[5]/a')
        TOP_LOCATIONS_ASSERT = (By.XPATH, '/html/body/div[5]/header/div/div/div/nav[1]/ul/li[7]/a')
        TOP_ADMIN_PAGE = (By.XPATH, '//*[@id="headerPanel"]/ul[1]/li[6]/a')
        TOP_ADMIN_PAGE_ASSERT = (By.XPATH, '//*[@id="rightPanel"]/h1')

    # BUTTONS, RIGHT TOP OF THE SCREEN
    class Buttons:
        HOME_BUTTON = (By.XPATH, '//*[@id="headerPanel"]/ul[2]/li[1]/a')
        HOME_ASSERT = (By.XPATH, '//*[@id="rightPanel"]/ul[1]/li[1]')
        ABOUT_US_BUTTON = (By.XPATH, '//*[@id="headerPanel"]/ul[2]/li[2]/a')
        CONTACT_BUTTON = (By.XPATH, '//*[@id="headerPanel"]/ul[2]/li[3]/a')
        CONTACT_ASSERT = (By.XPATH, '//*[@id="rightPanel"]/h1')

    # ATM SERVICES HYPERLINK, MIDDLE OF THE SCREEN
    class ATMServices:
        ATM_WITHDRAW_FUNDS = (By.XPATH,'//*[@id="rightPanel"]/ul[1]/li[2]/a')
        ATM_TRANSFER_FUNDS = (By.XPATH,'//*[@id="rightPanel"]/ul[1]/li[3]/a')
        ATM_CHECK_BALANCES = (By.XPATH,'//*[@id="rightPanel"]/ul[1]/li[4]/a')
        ATM_MAKE_DEPOSITS = (By.XPATH,'//*[@id="rightPanel"]/ul[1]/li[5]/a')
        ATM_SERVICES_ASSERT = (By.ID, 'webkit-xml-viewer-source-xml')

    # ONLINE SERVICES, MIDDLE OF THE SCREEN
    class OnlineServices:
        OS_BILL_PAY = (By.XPATH,'//*[@id="rightPanel"]/ul[2]/li[2]/a')
        OS_ACCOUNT_HISTORY = (By.XPATH,'//*[@id="rightPanel"]/ul[2]/li[3]/a')
        OS_TRANSFER_FUNDS = (By.XPATH,'//*[@id="rightPanel"]/ul[2]/li[4]/a')
        ONLINE_SERVICES_ASSERT = (By.ID, 'webkit-xml-viewer-source-xml')

    # LATEST NEWS, MIDDLE OF THE SCREEN
    class LatestNews:
        LN_FIRST_NEWS = (By.XPATH,'//*[@id="rightPanel"]/ul[3]/li[2]/a')
        LN_SECOND_NEWS = (By.XPATH,'//*[@id="rightPanel"]/ul[3]/li[3]/a')
        LN_THIRD_NEWS = (By.XPATH,'//*[@id="rightPanel"]/ul[3]/li[4]/a')
        LN_ASSERT = (By.XPATH, '//*[@id="rightPanel"]/h1')

    # READ MORE BUTTONS
    class ReadMore:
        READ_MORE_SERVICES = (By.XPATH,'//*[@id="rightPanel"]/p[1]/a')
        READ_MORE_LATEST_NEWS = (By.XPATH,'//*[@id="rightPanel"]/p[2]/a')

    # TABS ON THE BOTTOM OF THE PAGE
    class BottomTabs:
        BOTTOM_HOME = (By.XPATH,'//*[@id="footerPanel"]/ul[1]/li[1]/a')
        BOTTOM_ABOUT_US = (By.XPATH,'//*[@id="footerPanel"]/ul[1]/li[2]/a')
        BOTTOM_SERVICES = (By.XPATH,'//*[@id="footerPanel"]/ul[1]/li[3]/a')
        BOTTOM_PRODUCTS = (By.XPATH,'//*[@id="footerPanel"]/ul[1]/li[4]/a')
        BOTTOM_LOCATIONS = (By.XPATH,'//*[@id="footerPanel"]/ul[1]/li[5]/a')
        BOTTOM_FORUM = (By.XPATH,'//*[@id="footerPanel"]/ul[1]/li[6]/a')
        BOTTOM_FORUM_ASSERT = (By.XPATH,
                               '//*[@id="app"]/div[3]/div[2]/div/div/div/div/div[2]/'
                               'div/section/div[2]/div/div/ul/li[1]/a/div/div[2]/h3')
        BOTTOM_SITE_MAP = (By.XPATH,'//*[@id="footerPanel"]/ul[1]/li[7]/a')
        BOTTOM_SITE_MAP_ASSERT = (By.XPATH, '//*[@id="rightPanel"]/ul[1]/li[1]')
        BOTTOM_CONTACT_US = (By.XPATH,'//*[@id="footerPanel"]/ul[1]/li[8]/a')

class HomePage(BasePage):

    """
    HomePage object
    """

    def enter_username(self, username):
        """
        Enters username
        :param username:
        :return: Entered username
        """

        # While not logged in
        # Find username field and enter username
        self.driver.find_element(*HomePageLocators.CustomerLogin.LOG_IN_USERNAME_I).send_keys(username)
        return self

    def enter_password(self, password):
        """
          Enters password
          :param password:
          :return: Entered username
          """

        # While not logged in
        # Find password field and enter password
        self.driver.find_element(*HomePageLocators.CustomerLogin.LOG_IN_PASSWORD_I).send_keys(password)
        return self

    def click_log_in(self):
        """
        Clicks Log In button
        :return: LoggedInPage instance
        """

        # While not logged in
        # Find and click on Log In button
        self.driver.find_element(*HomePageLocators.CustomerLogin.LOG_IN_BUTTON).click()

    def get_customer_login_text(self):
        """
        Gets Customer Login text above the username field
        :return:
        """

        # While not logged in
        # Look for Customer Login text
        self.wait_5s.until(EC.text_to_be_present_in_element
                           (HomePageLocators.CustomerLogin.CUSTOMER_LOGIN_TEXT, "Customer Login"))
        return self.driver.find_element(*HomePageLocators.CustomerLogin.CUSTOMER_LOGIN_TEXT).text

    def get_log_in_text(self):
        """
        Gets Log In button below the Password field
        :return:
        """

        # While not logged in
        # Look for Log In button
        self.wait_5s.until(EC.text_to_be_present_in_element
                           (HomePageLocators.CustomerLogin.LOG_IN_BUTTON, "Log in"))
        return self.driver.find_element(*HomePageLocators.CustomerLogin.LOG_IN_BUTTON).text

    def get_log_in_empty_error(self):
        """
        Gets Error once user clicks on Log In button with both empty fields
        :return:
        """

        # While not logged in
        # Look for empty login error
        self.wait_5s.until(EC.text_to_be_present_in_element
                           (HomePageLocators.CustomerLogin.EMPTY_LOGIN_CREDENTIALS_ERROR,
                            "Please enter a username and password."))
        return self.driver.find_element(*HomePageLocators.CustomerLogin.EMPTY_LOGIN_CREDENTIALS_ERROR).text

    def get_log_in_invalid_error(self):
        """
        Gets Error once user clicks on Log In button with invalid credentials
        :return:
        """

        # While not logged in
        #Look for invalid login error
        self.wait_5s.until(EC.text_to_be_present_in_element
                           (HomePageLocators.CustomerLogin.INVALID_LOGIN_CREDENTIALS_ERROR,
                            "An internal error has occurred and has been logged."))
        return self.driver.find_element(*HomePageLocators.CustomerLogin.INVALID_LOGIN_CREDENTIALS_ERROR).text

    def get_register_text(self):
        """
        Gets Register hyperlink below the Log In button
        :return:
        """

        # While not logged in
        # Look for Register hyperlink
        self.wait_5s.until(EC.text_to_be_present_in_element
                           (HomePageLocators.CustomerLogin.REGISTER_HYPERLINK, "Register"))
        return self.driver.find_element(*HomePageLocators.CustomerLogin.REGISTER_HYPERLINK).text

    def click_register_hyperlink(self):
        """
        Clicks on Register hyperlink below the Log In button.
        :return:
        """

        # While not logged in
        # Find and click on Register hyperlink
        self.driver.find_element(*HomePageLocators.CustomerLogin.REGISTER_HYPERLINK).click()


    def click_top_about_us(self):
        """
        Clicks About Us tab
        :return: About Us page
        """
        # Find and click on About Us tab
        self.driver.find_element(*HomePageLocators.TopTabs.TOP_ABOUT_US).click()

    def get_about_us_text(self):
        """
        About Us page assertion
        :return:
        """

        # While not logged in
        # Look for About Us page title
        self.wait_5s.until(EC.text_to_be_present_in_element
                           (HomePageLocators.TopTabs.TOP_ABOUT_US_ASSERT, "ParaSoft Demo Website"))
        return self.driver.find_element(*HomePageLocators.TopTabs.TOP_ABOUT_US_ASSERT).text

    def click_top_services(self):
        """
        Clicks Services tab
        :return: Services page
        """
        # Find and click on Services tab
        self.driver.find_element(*HomePageLocators.TopTabs.TOP_SERVICES).click()

    def get_services_text(self):
        """
        Services page assertion
        :return:
        """

        # While not logged in
        # Look for Services page title
        self.wait_5s.until(EC.text_to_be_present_in_element
                           (HomePageLocators.TopTabs.TOP_SERVICES_ASSERT, "Available Bookstore SOAP services:"))
        return self.driver.find_element(*HomePageLocators.TopTabs.TOP_SERVICES_ASSERT).text

    def click_top_products(self):
        """
        Clicks Products tab
        :return: Products page
        """
        # Find and click on Products tab
        self.driver.find_element(*HomePageLocators.TopTabs.TOP_PRODUCTS).click()

    def get_products_text(self):
        """
        Products page assertion
        :return:
        """

        # While not logged in
        # Look for Products page title
        self.wait_5s.until(EC.text_to_be_present_in_element
                           (HomePageLocators.TopTabs.TOP_PRODUCTS_ASSERT, "Try Parasoft"))
        return self.driver.find_element(*HomePageLocators.TopTabs.TOP_PRODUCTS_ASSERT).text

    def click_top_locations(self):
        """
        Clicks Locations tab
        :return: Locations page
        """
        # Find and click on Locations tab
        self.driver.find_element(*HomePageLocators.TopTabs.TOP_LOCATIONS).click()

    def get_locations_text(self):
        """
        Locations page assertion
        :return:
        """

        # While not logged in
        # Look for Locations page title
        self.wait_5s.until(EC.text_to_be_present_in_element
                           (HomePageLocators.TopTabs.TOP_LOCATIONS_ASSERT, "Try Parasoft"))
        return self.driver.find_element(*HomePageLocators.TopTabs.TOP_LOCATIONS_ASSERT).text

    def click_top_admin_page(self):
        """
        Clicks Admin Page tab
        :return: Admin Page page
        """
        # Find and click on Admin Page tab
        self.driver.find_element(*HomePageLocators.TopTabs.TOP_ADMIN_PAGE).click()

    def get_admin_page_text(self):
        """
        Admin Page assertion
        :return:
        """

        # While not logged in
        # Look for Admin page title
        self.wait_5s.until(EC.text_to_be_present_in_element
                           (HomePageLocators.TopTabs.TOP_ADMIN_PAGE_ASSERT, "Administration"))
        return self.driver.find_element(*HomePageLocators.TopTabs.TOP_ADMIN_PAGE_ASSERT).text


    def click_home_button(self):
        """
        Clicks Home button
        :return: Home page
        """
        # Find and click on Home button
        self.driver.find_element(*HomePageLocators.Buttons.HOME_BUTTON).click()

    def get_home_button_text(self):
        """
        Home Page assertion
        :return:
        """

        # While not logged in
        # Look for Latest News text
        self.wait_5s.until(EC.text_to_be_present_in_element
                           (HomePageLocators.Buttons.HOME_ASSERT, "ATM Services"))
        return self.driver.find_element(*HomePageLocators.Buttons.HOME_ASSERT).text

    def click_about_us_button(self):
        """
        Clicks About Us button
        :return: About Us page
        """
        # Find and click on Home button
        self.driver.find_element(*HomePageLocators.Buttons.ABOUT_US_BUTTON).click()

    def click_contact_button(self):
        """
        Clicks Contact button
        :return: Contact page
        """
        # Find and click on Home button
        self.driver.find_element(*HomePageLocators.Buttons.CONTACT_BUTTON).click()

    def get_contact_button_text(self):
        """
        Contact page assertion
        :return:
        """

        # While not logged in
        # Look for Customer Care text
        self.wait_5s.until(EC.text_to_be_present_in_element
                           (HomePageLocators.Buttons.CONTACT_ASSERT, "Customer Care"))
        return self.driver.find_element(*HomePageLocators.Buttons.CONTACT_ASSERT).text


    def click_atm_withdraw_funds(self):
        """
        Clicks Withdraw Funds hyperlink
        :return: Withdraw Funds page
        """
        # Find and click on Withdraw Funds hyperlink
        self.driver.find_element(*HomePageLocators.ATMServices.ATM_WITHDRAW_FUNDS).click()

    def click_atm_transfer_funds(self):
        """
        Clicks Transfer Funds hyperlink
        :return: Transfer Funds page
        """
        # Find and click on Transfer Funds hyperlink
        self.driver.find_element(*HomePageLocators.ATMServices.ATM_TRANSFER_FUNDS).click()

    def click_atm_check_balances(self):
        """
        Clicks Check Balances hyperlink
        :return: Check Balances page
        """
        # Find and click on Check Balances hyperlink
        self.driver.find_element(*HomePageLocators.ATMServices.ATM_CHECK_BALANCES).click()

    def click_atm_make_deposits(self):
        """
        Clicks Make Deposits hyperlink
        :return: Make Deposits page
        """
        # Find and click on Make Deposits hyperlink
        self.driver.find_element(*HomePageLocators.ATMServices.ATM_MAKE_DEPOSITS).click()

    def get_atm_services_id(self):
        """
        ATM Services page assertion
        :return:
        """

        # While not logged in
        # Look for element present by ID

        try:
            self.wait_5s.until(EC.presence_of_element_located((By.ID, "webkit-xml-viewer-source-xml")))
            return True
        except TimeoutException:
            return False


    def click_os_bill_pay(self):
        """
        Clicks Bill Pay hyperlink
        :return: Bill Pay page
        """
        # Find and click on Bill Pay hyperlink
        self.driver.find_element(*HomePageLocators.OnlineServices.OS_BILL_PAY).click()

    def click_os_account_history(self):
        """
        Clicks Account History hyperlink
        :return: Account History page
        """
        # Find and click on Account History hyperlink
        self.driver.find_element(*HomePageLocators.OnlineServices.OS_ACCOUNT_HISTORY).click()

    def click_os_transfer_funds(self):
        """
        Clicks Transfer Funds hyperlink
        :return: Transfer Funds page
        """
        # Find and click on Transfer Funds hyperlink
        self.driver.find_element(*HomePageLocators.OnlineServices.OS_TRANSFER_FUNDS).click()

    def get_online_services_id(self):
        """
        Online Services page assertion
        :return:
        """

        # While not logged in
        # Look for element present by ID

        try:
            self.wait_5s.until(EC.presence_of_element_located((By.ID, "webkit-xml-viewer-source-xml")))
            return True
        except TimeoutException:
            return False


    def click_ln_first_news(self):
        """
        Clicks First News hyperlink
        :return: First News page
        """
        # Find and click on First News hyperlink
        self.driver.find_element(*HomePageLocators.LatestNews.LN_FIRST_NEWS).click()

    def click_ln_second_news(self):
        """
        Clicks Second News hyperlink
        :return: Second News page
        """
        # Find and click on Second News hyperlink
        self.driver.find_element(*HomePageLocators.LatestNews.LN_SECOND_NEWS).click()

    def click_ln_third_news(self):
        """
        Clicks Third News hyperlink
        :return: Third News page
        """
        # Find and click on Third News hyperlink
        self.driver.find_element(*HomePageLocators.LatestNews.LN_THIRD_NEWS).click()

    def get_parabank_news_text(self):
        """
        ParaBank News page assertion
        :return:
        """

        # While not logged in
        # Look for ParaBank News title
        self.wait_5s.until(EC.text_to_be_present_in_element
                           (HomePageLocators.LatestNews.LN_ASSERT, "ParaBank News"))
        return self.driver.find_element(*HomePageLocators.LatestNews.LN_ASSERT).text


    def click_read_more_services(self):
        """
        Clicks Read More hyperlink for services
        :return: Services page
        """
        # Find and click on Read More hyperlink for Services
        self.driver.find_element(*HomePageLocators.ReadMore.READ_MORE_SERVICES).click()

    def click_read_more_latest_news(self):
        """
        Clicks Read More hyperlink for latest news
        :return: Latest News page
        """
        # Find and click on Read More hyperlink for Latest News
        self.driver.find_element(*HomePageLocators.ReadMore.READ_MORE_LATEST_NEWS).click()


    def click_bottom_home(self):
        """
        Clicks Home hyperlink
        :return: Home page
        """
        # Find and click on Home hyperlink on the bottom of the screen
        self.driver.find_element(*HomePageLocators.BottomTabs.BOTTOM_HOME).click()

    def click_bottom_about_us(self):
        """
        Clicks About Us hyperlink
        :return: About Us page
        """
        # Find and click on About Us hyperlink on the bottom of the screen
        self.driver.find_element(*HomePageLocators.BottomTabs.BOTTOM_ABOUT_US).click()

    def click_bottom_services(self):
        """
        Clicks Services hyperlink
        :return: Services page
        """
        # Find and click on Services hyperlink on the bottom of the screen
        self.driver.find_element(*HomePageLocators.BottomTabs.BOTTOM_SERVICES).click()

    def click_bottom_products(self):
        """
        Clicks Products hyperlink
        :return: Products page
        """
        # Find and click on Products hyperlink on the bottom of the screen
        self.driver.find_element(*HomePageLocators.BottomTabs.BOTTOM_PRODUCTS).click()

    def click_bottom_locations(self):
        """
        Clicks Locations hyperlink
        :return: Locations page
        """
        # Find and click on Locations hyperlink on the bottom of the screen
        self.driver.find_element(*HomePageLocators.BottomTabs.BOTTOM_LOCATIONS).click()

    def click_bottom_forum(self):
        """
        Clicks Forum hyperlink
        :return: Forum page
        """
        # Find and click on Forum hyperlink on the bottom of the screen
        self.driver.find_element(*HomePageLocators.BottomTabs.BOTTOM_FORUM).click()

    def get_forum_text(self):
        """
        Forum page assertion
        :return:
        """

        # While not logged in
        # Look for Forum page title
        self.wait_5s.until(EC.text_to_be_present_in_element
                           (HomePageLocators.BottomTabs.BOTTOM_FORUM_ASSERT, "Product Ideas"))
        return self.driver.find_element(*HomePageLocators.BottomTabs.BOTTOM_FORUM_ASSERT).text

    def click_bottom_site_map(self):
        """
        Clicks Site Map hyperlink
        :return: Site Map page
        """
        # Find and click on Site Map hyperlink on the bottom of the screen
        self.driver.find_element(*HomePageLocators.BottomTabs.BOTTOM_SITE_MAP).click()

    def get_site_map_text(self):
        """
        Site Map page assertion
        :return:
        """

        # While not logged in
        # Look for Forum page title
        self.wait_5s.until(EC.text_to_be_present_in_element
                           (HomePageLocators.BottomTabs.BOTTOM_SITE_MAP_ASSERT, "Solutions"))
        return self.driver.find_element(*HomePageLocators.BottomTabs.BOTTOM_SITE_MAP_ASSERT).text

    def click_bottom_contact_us(self):
        """
        Clicks Contact Us hyperlink
        :return: Contact Us page
        """
        # Find and click on Contact Us hyperlink on the bottom of the screen
        self.driver.find_element(*HomePageLocators.BottomTabs.BOTTOM_CONTACT_US).click()