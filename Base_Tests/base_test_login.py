import unittest
from selenium import webdriver
from Data.locators import DANE
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker
class BaseTestLogin(unittest.TestCase):
    """
    Base class for future login tests
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(DANE.LoginPageURL)
        self.wait = WebDriverWait(self.driver, 20)
        self.fake = Faker("pl_PL")

    def tearDown(self):
        self.driver.quit()