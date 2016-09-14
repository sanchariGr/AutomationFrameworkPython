import json
import os

class BasePage(object):


    url = "http://www.amazon.in/"

    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        self.driver.get(self.url)
