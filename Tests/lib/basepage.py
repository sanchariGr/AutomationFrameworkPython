import json
import os
import pdb


class BasePage(object):
    url = "http://www.amazon.in/"

    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        self.driver.get(self.url)


class UserDetails(BasePage):
    def sign_in(self):
        signin = self.driver.find_element_by_css_selector("#nav-link-yourAccount")
        signin.click()

    def create_account(self):
        create_account = self.driver.find_element_by_css_selector("#createAccountSubmit")
        create_account.click()

    def fill_user_info(self):
        self.driver.implicitly_wait(10)
        use_email = self.driver.find_element_by_css_selector("#ap_use_email")
        use_email.click()

        with open(os.path.dirname(__file__) + '/config.json', 'r+') as configure:
            data = json.load(configure)
            your_name = data["user_registration"]["name"]
            email = data["user_registration"]["email"]
            password = data["user_registration"]["password"]

            self.driver.find_element_by_id("ap_customer_name").send_keys(your_name)
            self.driver.find_element_by_id("ap_email").send_keys(email)
            self.driver.find_element_by_id("ap_password").send_keys(password)

    def submit(self):

        submit_button = self.driver.find_element_by_css_selector("#auth-create-account-button #continue")
        submit_button.click()
        # pdb.set_trace()

    def verify_user_creation(self):
        self.driver.implicitly_wait(10)
        verify_username = self.driver.find_element_by_css_selector("#nav-link-yourAccount .nav-line-1").text

        try:
            assert "Hello, Sanchari" in verify_username
            print "User Account Created Successfully..."
        except Exception as e:
            print e


    def login_details(self):
        with open(os.path.dirname(__file__) + '/config.json', 'r+') as configure:
            data = json.load(configure)
            email = data["user_login"]["email"]
            password = data["user_login"]["password"]

            self.driver.find_element_by_id("ap_email").send_keys(email)
            self.driver.find_element_by_id("ap_password").send_keys(password)


    def confirm(self):
        confirm_login = self.driver.find_element_by_css_selector("#signInSubmit")
        confirm_login.click()
        # pdb.set_trace()

    def verify_login(self):
        verify_username = self.driver.find_element_by_css_selector("#nav-link-yourAccount .nav-line-1").text

        try:
            assert "Hello, Sanchari" in verify_username
            print "User Account Created Successfully..."
        except Exception as e:
            print e

    def wrong_login_details(self):
        with open(os.path.dirname(__file__) + '/config.json', 'r+') as configure:
            data = json.load(configure)
            email = data["user_incorrect_login"]["email"]
            password = data["user_incorrect_login"]["password"]

            self.driver.find_element_by_id("ap_email").send_keys(email)
            self.driver.find_element_by_id("ap_password").send_keys(password)

    def verify_error(self):
        error_message = self.driver.find_element_by_css_selector("#auth-error-message-box").text

        try:
            assert "There was a problem Your password is incorrect" in error_message
            print "Incorrect User Details..."
        except Exception as e:
            print e




