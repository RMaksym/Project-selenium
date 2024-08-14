import unittest
from selenium import webdriver
from locators import DANE
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker
class BaseTest(unittest.TestCase):
    """
    Base class for future tests
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(DANE.RegistrationPageURL)
        self.driver.implicitly_wait(3)
        self.wait = WebDriverWait(self.driver, 20)
        self.fake = Faker("pl_PL")

    def tearDown(self):
        self.driver.quit()