import os
import requests
from selenium import webdriver

from Tests.lib.basepage import BasePage


class Homepage(BasePage):

    def select_category(self):
        self.driver.find_element_by_css_selector("#nav-link-shopall").click()
        category = self.driver.find_element_by_css_selector('.nav_a[href="/Laptops/b/ref=sd_allcat_computers_laptop?ie=UTF8&node=1375424031"]')
        category.click()




