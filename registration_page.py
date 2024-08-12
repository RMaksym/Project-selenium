import unittest
from data import DANE
from selenium import webdriver
from selenium.webdriver.common.by import By
class StartRegistrationPage (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_RegistrationPage(self):
        self.driver.get(DANE.RegistrationPageURL)

        logo_rejestracja = self.driver.find_element(By.XPATH, '//*[@id="register"]/h1')
        if logo_rejestracja.is_displayed():
            print("PASS: strona rejestracyjna zaladowana pomyslnie")
        else:
            print("FAILED: brak widocznego logo rejestracji")
    def tearDown(self):
        self.driver.quit()

