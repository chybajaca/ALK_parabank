from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class RegisterPageLocators:

    REGISTER_FIRST_NAME_I = (By.XPATH, '//*[@id="customer.firstName"]')
    REGISTER_LAST_NAME_I = (By.XPATH, '//*[@id="customer.lastName"]')
    REGISTER_ADDRESS_I = (By.XPATH, '//*[@id="customer.address.street"]')
    REGISTER_CITY_I = (By.XPATH, '//*[@id="customer.address.city"]')
    REGISTER_STATE_I = (By.XPATH, '//*[@id="customer.address.state"]')
    REGISTER_ZIPCODE_I = (By.XPATH, '//*[@id="customer.address.zipCode"]')
    REGISTER_PHONE_I = (By.XPATH, '//*[@id="customer.phoneNumber"]')
    REGISTER_SSN_I = (By.XPATH, '//*[@id="customer.ssn"]')

    REGISTER_USERNAME_I = (By.XPATH, '//*[@id="customer.username"]')
    REGISTER_PASSWORD_I = (By.XPATH, '//*[@id="customer.password"]')
    REGISTER_PASSWORD_CONFIRM_I = (By.XPATH, '//*[@id="repeatedPassword"]')

    REGISTER_EMPTY_FIRST_NAME_I = (By.XPATH, '//*[@id="customer.firstName.errors"]')
    REGISTER_EMPTY_LAST_NAME_I = (By.XPATH, '//*[@id="customer.lastName.errors"]')
    REGISTER_EMPTY_ADDRESS_I = (By.XPATH, '//*[@id="customer.address.street.errors"]')
    REGISTER_EMPTY_CITY_I = (By.XPATH, '//*[@id="customer.address.city.errors"]')
    REGISTER_EMPTY_STATE_I = (By.XPATH, '//*[@id="customer.address.state.errors"]')
    REGISTER_EMPTY_ZIPCODE_I = (By.XPATH, '//*[@id="customer.address.zipCode.errors"]')
    REGISTER_EMPTY_SSN_I = (By.XPATH, '//*[@id="customer.ssn.errors"]')

    REGISTER_EMPTY_USERNAME_I = (By.XPATH, '//*[@id="customer.username.errors"]')
    REGISTER_EMPTY_PASSWORD_I = (By.XPATH, '//*[@id="customer.password.errors"]')
    REGISTER_EMPTY_CONFIRM_I = (By.XPATH, '//*[@id="repeatedPassword.errors"]')

    REGISTER_BUTTON_I = (By.XPATH, '//*[@id="customerForm"]/table/tbody/tr[13]/td[2]/input')

class RegisterPage(BasePage):

    """
    HomePage object
    """

    def enter_firstname(self, firstname):
        """
        Enters First Name
        :param firstname:
        :return: Entered first name
        """

        # While not logged in
        # Find "First Name" field and enter first name
        self.driver.find_element(*RegisterPageLocators.REGISTER_FIRST_NAME_I).send_keys(firstname)
        return self

    def enter_lastname(self, lastname):
        """
        Enters Last Name
        :param lastname:
        :return: Entered last name
        """

        # While not logged in
        # Find "Last Name" field and enter last name
        self.driver.find_element(*RegisterPageLocators.REGISTER_LAST_NAME_I).send_keys(lastname)
        return self

    def enter_address(self, address):
        """
        Enters address
        :param address:
        :return: Entered address
        """

        # While not logged in
        # Find Address field and enter street name and number
        self.driver.find_element(*RegisterPageLocators.REGISTER_ADDRESS_I).send_keys(address)
        return self

    def enter_city(self, city):
        """
        Enters city
        :param city:
        :return: Entered city
        """

        # While not logged in
        # Find City field and enter city name
        self.driver.find_element(*RegisterPageLocators.REGISTER_CITY_I).send_keys(city)
        return self

    def enter_state(self, state):
        """
        Enters state
        :param state:
        :return: Entered state
        """

        # While not logged in
        # Find State field and enter state name
        self.driver.find_element(*RegisterPageLocators.REGISTER_STATE_I).send_keys(state)
        return self

    def enter_zipcode(self, zipcode):
        """
        Enters ZIP Code
        :param zipcode:
        :return: Entered ZIP Code
        """

        # While not logged in
        # Find "Zip Code" field and enter zipcode name
        self.driver.find_element(*RegisterPageLocators.REGISTER_ZIPCODE_I).send_keys(zipcode)
        return self

    def enter_phonenumber(self, phonenumber):
        """
        Enters Phone Number
        :param phonenumber:
        :return: Entered Phone Number
        """

        # While not logged in
        # Find "Phone Number" field and enter phone number
        self.driver.find_element(*RegisterPageLocators.REGISTER_PHONE_I).send_keys(phonenumber)
        return self

    def enter_ssn(self, ssn):
        """
        Enters SSN
        :param ssn:
        :return: Entered SSN
        """

        # While not logged in
        # Find SSN field and enter SSN
        self.driver.find_element(*RegisterPageLocators.REGISTER_SSN_I).send_keys(ssn)
        return self

    def enter_username(self, username):
        """
        Enters username
        :param username:
        :return: Entered username
        """

        # While not logged in
        # Find Username field and enter username
        self.driver.find_element(*RegisterPageLocators.REGISTER_USERNAME_I).send_keys(username)
        return self

    def enter_password(self, password):
        """
        Enters password
        :param password:
        :return: Entered password
        """

        # While not logged in
        # Find Password field and enter password
        self.driver.find_element(*RegisterPageLocators.REGISTER_PASSWORD_I).send_keys(password)
        return self

    def enter_confirm(self, password):
        """
        Enters Password once again
        :param confirm:
        :return: Entered password once again
        """

        # While not logged in
        # Find Confirm field and enter the same password as in the Password field
        self.driver.find_element(*RegisterPageLocators.REGISTER_PASSWORD_CONFIRM_I).send_keys(password)
        return self

    def click_register(self):
        """
        Clicks Register button
        :return: Logged in page
        """
        # Press Register button on the registration form page
        self.driver.find_element(*RegisterPageLocators.REGISTER_BUTTON_I).click()

    def get_empty_firstname_text(self):
        """
        Gets alert for empty First Name field
        :return:
        """

        # While not logged in
        # Look for empty First Name field alert
        self.wait_5s.until(EC.text_to_be_present_in_element
                           (RegisterPageLocators.REGISTER_EMPTY_FIRST_NAME_I, "First name is required."))
        return self.driver.find_element(*RegisterPageLocators.REGISTER_EMPTY_FIRST_NAME_I).text

    def get_empty_lastname_text(self):
        """
        Gets alert for empty Last Name field
        :return:
        """

        # While not logged in
        # Look for empty Last Name field alert
        self.wait_5s.until(EC.text_to_be_present_in_element
                           (RegisterPageLocators.REGISTER_EMPTY_LAST_NAME_I, "Last name is required."))
        return self.driver.find_element(*RegisterPageLocators.REGISTER_EMPTY_LAST_NAME_I).text

    def get_empty_address_text(self):
        """
        Gets alert for empty Address field
        :return:
        """

        # While not logged in
        # Look for empty Address field alert
        self.wait_5s.until(EC.text_to_be_present_in_element
                           (RegisterPageLocators.REGISTER_EMPTY_ADDRESS_I, "Address is required."))
        return self.driver.find_element(*RegisterPageLocators.REGISTER_EMPTY_ADDRESS_I).text

    def get_empty_city_text(self):
        """
        Gets alert for empty City field
        :return:
        """

        # While not logged in
        # Look for empty City field alert
        self.wait_5s.until(EC.text_to_be_present_in_element
                           (RegisterPageLocators.REGISTER_EMPTY_CITY_I, "City is required."))
        return self.driver.find_element(*RegisterPageLocators.REGISTER_EMPTY_CITY_I).text

    def get_empty_state_text(self):
        """
        Gets alert for empty State field
        :return:
        """

        # While not logged in
        # Look for empty State field alert
        self.wait_5s.until(EC.text_to_be_present_in_element
                           (RegisterPageLocators.REGISTER_EMPTY_STATE_I, "State is required."))
        return self.driver.find_element(*RegisterPageLocators.REGISTER_EMPTY_STATE_I).text

    def get_empty_zipcode_text(self):
        """
        Gets alert for empty Zip Code field
        :return:
        """

        # While not logged in
        # Look for empty Zip Code field alert
        self.wait_5s.until(EC.text_to_be_present_in_element
                           (RegisterPageLocators.REGISTER_EMPTY_ZIPCODE_I, "Zip Code is required."))
        return self.driver.find_element(*RegisterPageLocators.REGISTER_EMPTY_ZIPCODE_I).text

    def get_empty_ssn_text(self):
        """
        Gets alert for empty SSN field
        :return:
        """

        # While not logged in
        # Look for empty SSN field alert
        self.wait_5s.until(EC.text_to_be_present_in_element
                           (RegisterPageLocators.REGISTER_EMPTY_SSN_I, "Social Security Number is required."))
        return self.driver.find_element(*RegisterPageLocators.REGISTER_EMPTY_SSN_I).text

    def get_empty_username_text(self):
        """
        Gets alert for empty Username field
        :return:
        """

        # While not logged in
        # Look for empty Username field alert
        self.wait_5s.until(EC.text_to_be_present_in_element
                           (RegisterPageLocators.REGISTER_EMPTY_USERNAME_I, "Username is required."))
        return self.driver.find_element(*RegisterPageLocators.REGISTER_EMPTY_USERNAME_I).text

    def get_empty_password_text(self):
        """
        Gets alert for empty Password field
        :return:
        """

        # While not logged in
        # Look for empty Password field alert
        self.wait_5s.until(EC.text_to_be_present_in_element
                           (RegisterPageLocators.REGISTER_EMPTY_PASSWORD_I, "Password is required."))
        return self.driver.find_element(*RegisterPageLocators.REGISTER_EMPTY_PASSWORD_I).text

    def get_empty_confirm_text(self):
        """
        Gets alert for empty Password Confirmation field
        :return:
        """

        # While not logged in
        # Look for empty Confirm field alert
        self.wait_5s.until(EC.text_to_be_present_in_element
                           (RegisterPageLocators.REGISTER_EMPTY_CONFIRM_I, "Password confirmation is required."))
        return self.driver.find_element(*RegisterPageLocators.REGISTER_EMPTY_CONFIRM_I).text