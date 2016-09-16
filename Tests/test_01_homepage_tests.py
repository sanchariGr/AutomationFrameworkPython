import unittest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from Tests.lib.homepage import Homepage
from  Tests.lib.basepage import BasePage, LoginUser


class HomepageTests(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get("http://www.amazon.in/")
        self.browser.maximize_window()

    def test_select_category(self):
        login = LoginUser(self.browser)
        category = Homepage(self.browser)
        category.select_category()
        category.select_category_name()







if __name__ == "__main__":
    unittest.main(verbosity=2)