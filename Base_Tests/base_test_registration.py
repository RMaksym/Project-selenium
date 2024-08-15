import unittest
from selenium import webdriver
from Data.locators import DANE
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker
class BaseTestRegistration(unittest.TestCase):
    """
    Base class for future registration tests
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(DANE.RegistrationPageURL)
        self.driver.implicitly_wait(3)
        self.wait = WebDriverWait(self.driver, 5)
        self.fake = Faker("pl_PL")

    def tearDown(self):
        self.driver.quit()