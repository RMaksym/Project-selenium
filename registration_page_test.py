import unittest
from locators import DANE
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_test import BaseTest
class StartRegistrationPageTes(BaseTest):
    def setUp(self):
        super().setUp()
    def test_RegistrationPageTest_ID_002(self):

        logo_rejestracja = self.driver.find_element(By.XPATH, '//*[@id="register"]/h1')
        if logo_rejestracja.is_displayed():
            print("PASS: strona rejestracyjna zaladowana pomyslnie")
        else:
            print("FAILED: brak widocznego logo rejestracji")
    def tearDown(self):
        self.driver.quit()

