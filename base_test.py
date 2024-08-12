import unittest
from selenium import webdriver
from data import DANE
from registration_page import RegistrationPage

class BaseTest(unittest.TestCase):

    """
    base class for each test
    """

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(DANE.RegistrationPageURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.registration_page = RegistrationPage(self.driver)

    def tearDown(self):
        self.driver.quit()