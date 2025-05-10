from test_cases.base_test import BaseTest
from time import sleep
from faker import Faker
import csv

fake = Faker()

firstname = fake.first_name()
lastname = fake.last_name()
address = fake.address()
city = fake.city()
state = fake.state()
zipcode = fake.zipcode()
phone = fake.phone_number()
ssn = fake.ssn()

username = fake.user_name()
password = fake.password(length=8)

class RegisterTest(BaseTest):

    def testEmptyRegister(self):

        """
        Attempt to register an account with empty fields.
        :return:
        """

        # 1. Enter registration page
        self.home_page.click_register_hyperlink()
        sleep(2)

        # 2. Click on Register button
        self.register_page.click_register()
        sleep(2)

        # 3. Look for "First name is required" text for empty First Name field alert
        self.assertEqual("First name is required.", self.register_page.get_empty_firstname_text())

        # 4. Look for "Last name is required" text for empty Last Name field alert
        self.assertEqual("Last name is required.", self.register_page.get_empty_lastname_text())

        # 5. Look for "Address is required" text for empty Address field alert
        self.assertEqual("Address is required.", self.register_page.get_empty_address_text())

        # 6. Look for "City is required" text for empty City field alert
        self.assertEqual("City is required.", self.register_page.get_empty_city_text())

        # 7. Look for "State is required" text for empty State field alert
        self.assertEqual("State is required.", self.register_page.get_empty_state_text())

        # 8. Look for "Zip code is required" text for empty Zip Code field alert
        self.assertEqual("Zip Code is required.", self.register_page.get_empty_zipcode_text())

        # 9. Look for "Social Security Number is required" text for empty SSN field alert
        self.assertEqual("Social Security Number is required.", self.register_page.get_empty_ssn_text())

        # 10. Look for "Username is required" text for empty Username field alert
        self.assertEqual("Username is required.", self.register_page.get_empty_username_text())

        # 11. Look for "Password is required" text for empty Password field alert
        self.assertEqual("Password is required.", self.register_page.get_empty_password_text())

        # 12. Look for "Password confirmation is required." text for empty Confirm field alert
        self.assertEqual("Password confirmation is required.", self.register_page.get_empty_confirm_text())

    def testPartialRegister(self):

        """
        Attempt to register an account with few fields fulfilled.
        :return:
        """

        # 1. Enter registration page
        self.home_page.click_register_hyperlink()
        sleep(2)

        # 2. Enter First Name
        self.register_page.enter_firstname(firstname)

        # 3. Enter City
        self.register_page.enter_city(city)

        # 4. Enter Phone number
        self.register_page.enter_phonenumber(phone)

        # 5. Enter SSN
        self.register_page.enter_ssn(ssn)

        # 6. Enter Username
        self.register_page.enter_username(username)

        # 7. Enter Password
        self.register_page.enter_password(password)

        # 8. Click on Register button
        self.register_page.click_register()
        sleep(2)

        # 9. Look for "Last name is required" text for empty Last Name field alert
        self.assertEqual("Last name is required.", self.register_page.get_empty_lastname_text())

        # 10. Look for "Address is required" text for empty Address field alert
        self.assertEqual("Address is required.", self.register_page.get_empty_address_text())

        # 11. Look for "State is required" text for empty State field alert
        self.assertEqual("State is required.", self.register_page.get_empty_state_text())

        # 12. Look for "Zip code is required" text for empty Zip Code field alert
        self.assertEqual("Zip Code is required.", self.register_page.get_empty_zipcode_text())

        # 13. Look for "Password confirmation is required." text for empty Confirm field alert
        self.assertEqual("Password confirmation is required.", self.register_page.get_empty_confirm_text())

    def testMissingConfirmRegister(self):

        """
        Registering the new account with all fields fulfilled except password confirmation field.
        :return:
        """

        # 1. Enter registration page
        self.home_page.click_register_hyperlink()
        sleep(2)

        # 2. Enter First Name
        self.register_page.enter_firstname(firstname)

        # 3. Enter Last Name
        self.register_page.enter_lastname(lastname)

        # 4. Enter Address
        self.register_page.enter_address(address)

        # 5. Enter City
        self.register_page.enter_city(city)

        # 6. Enter State
        self.register_page.enter_state(state)

        # 7. Enter Zip Code
        self.register_page.enter_zipcode(zipcode)

        # 8. Enter Phone number
        self.register_page.enter_phonenumber(phone)

        # 9. Enter SSN
        self.register_page.enter_ssn(ssn)

        # 10. Enter Username
        self.register_page.enter_username(username)

        # 11. Enter Password
        self.register_page.enter_password(password)

        sleep(2)

        # 12. Click on Register button
        self.register_page.click_register()
        sleep(2)

        # 13. Look for "Password confirmation is required." text for empty Confirm field alert
        self.assertEqual("Password confirmation is required.", self.register_page.get_empty_confirm_text())

    def testValidRegister(self):

        """
        Registering the new account with all fields fulfilled.
        :return:
        """
        fakefirstname = fake.first_name()
        fakelastname = fake.last_name()
        fakepassword = fake.password(length=8)

        # 1. Enter registration page
        self.home_page.click_register_hyperlink()
        sleep(2)

        # 2. Enter First Name
        self.register_page.enter_firstname(fakefirstname)

        # 3. Enter Last Name
        self.register_page.enter_lastname(fakelastname)

        # 4. Enter Address
        self.register_page.enter_address(fake.address())

        # 5. Enter City
        self.register_page.enter_city(fake.city())

        # 6. Enter State
        self.register_page.enter_state(fake.state())

        # 7. Enter Zip Code
        self.register_page.enter_zipcode(fake.zipcode())

        # 8. Enter Phone number
        self.register_page.enter_phonenumber(fake.phone_number())

        # 9. Enter SSN
        self.register_page.enter_ssn(fake.ssn())

        # 10. Enter Username
        self.register_page.enter_username(fake.user_name())

        # 11. Enter Password
        self.register_page.enter_password(fakepassword)

        # 12. Enter the same password once again
        self.register_page.enter_confirm(fakepassword)

        sleep(2)

        # Saving required data to file
        with open("C:/Users/jacek/OneDrive/Desktop/Projekt/parabank_project/test_data/valid_data.csv",
                  mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([username, password, firstname, lastname])

        # 13. Click on Register button
        self.register_page.click_register()
        sleep(2)

        # 14. Look for "Welcome <firstname> <lastname>" text
        welcome_text_act = self.logged_page.get_welcome_fullname_text()
        self.assertEqual(f"Welcome {fakefirstname} {fakelastname}", welcome_text_act)

        # 15. Check if LogOut is visible and clickable
        self.logged_page.click_log_out()
        sleep(2)

        # 16. Look for "Customer Login" text for LogOut confirmation
        self.assertEqual("Customer Login", self.home_page.get_customer_login_text())
        sleep(2)
