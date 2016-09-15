import unittest
from selenium import webdriver


class HomepageTests(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()






if __name__ == "__main__":
    unittest.main(verbosity=2)