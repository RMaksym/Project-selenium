import unittest
from selenium import webdriver
from data import DANE
from base_page import BasePage



class RegistrationPage(BasePage):

    def RegistrationPage(self):
        self.driver.get(DANE.RegistrationPageURL)

