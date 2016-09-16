import json
import os


class BasePage(object):
    url = "http://www.amazon.in/"

    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        self.driver.get(self.url)


class LoginUser(BasePage):
    def Login(self):
        signin = self.driver.find_element_by_css_selector("#nav-link-yourAccount")
        signin.click()
        with open(os.path.dirname(__file__) + '/config.json', 'r') as configure:
            data = json.load(configure)
            username = data["user_login"]["username"]
            password = data["user_login"]["password"]
            self.driver.find_element_by_id("ap_email").sendkeys(username)
            self.driver.find_element_by_id("ap_password").sendkeys(password)

