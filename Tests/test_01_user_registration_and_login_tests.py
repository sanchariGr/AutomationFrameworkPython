import unittest
from selenium import webdriver
from lib.basepage import UserDetails


class RegistrationTests(unittest.TestCase):

    def setUp(self):
        # Setup a driver instance
        self.browser = webdriver.Firefox()
        self.browser.get("http://www.amazon.in/")
        self.browser.maximize_window()


    def test_01_register_user(self):
        register = UserDetails(self.browser)
        register.navigate()
        register.sign_in()
        # Creates a new user account
        register.create_account()
        register.fill_user_info()
        register.submit()
        register.verify_user_creation()


    def test_02_login_user(self):
        login = UserDetails(self.browser)
        login.navigate()
        # Signs-in with the newly created user account details
        login.sign_in()
        login.login_details()
        login.confirm()
        login.verify_login()

    def test_03_incorrect_login(self):
        incorrect_login = UserDetails(self.browser)
        incorrect_login.navigate()
        # Signs-in with the newly created user email but with an incorrect password
        incorrect_login.sign_in()
        incorrect_login.wrong_login_details()
        incorrect_login.confirm()
        incorrect_login.verify_error()


    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)