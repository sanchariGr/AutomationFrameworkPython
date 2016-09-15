import unittest
from selenium import webdriver
from Tests.lib.homepage import Homepage


class HomepageTests(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()

    def test_select_category(self):
        category = Homepage(self.browser)
        category.select_category()
        category.select_category_name()







if __name__ == "__main__":
    unittest.main(verbosity=2)