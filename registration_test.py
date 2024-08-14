from base_test import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import uuid
from locators import DANE
from time import sleep

class RegistrationTests(BaseTest):
    def setUp(self):
        super().setUp()

    def test_Registration_correct_email_ID_003(self):

        self.input_email(self.fake.email())
        self.input_password(self.fake.password(10))
        self.sign_up()

        register_correct = self.driver.find_element(By.XPATH, "//*[@id='col-content']/span")
        self.wait.until(EC.visibility_of(register_correct))
        if register_correct.is_displayed():
                print("Account has been created")


    def test_Registration_non_email_ID_004(self):
        self.input_email("")
        self.input_password(self.fake.password())
        self.sign_up()

        none_email_mess = self.driver.find_element(By.XPATH, "//*[@id='register-form']/fieldset/p[2]")
        self.wait.until(EC.visibility_of(none_email_mess))
        if none_email_mess.is_displayed():
                print("Account has NOT been created: Email is required")

        else:
            print("Account has NOT been created")

    def test_Registration_invalid_email_ID_005(self):
        self.input_email("tester@123@gmail.com")
        self.input_password(self.fake.password())
        self.sign_up()

        invalid_email_mess = self.driver.find_element(By.XPATH, "//*[@id='register-form']/fieldset/p[1]/span")
        self.wait.until(EC.visibility_of(invalid_email_mess))
        if invalid_email_mess.is_displayed():
                print("Account has been created")

        else:
                print("Account has NOT been created")



    def input_email(self, email):
        email_window = self.driver.find_element(By.XPATH, "//*[@id='Email']")
        self.wait.until(EC.visibility_of(email_window))
        email_window.send_keys(email)

    def input_password (self, password):
        password_windoow = self.driver.find_element(By.XPATH, "//*[@id='Password']")
        password_windoow.send_keys(password)

    def sign_up (self):
        sign_up_btn= self.driver.find_element(By.XPATH, "//*[@id='btnRegister']")
        sign_up_btn.click()
