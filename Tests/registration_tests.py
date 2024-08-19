from Base_Tests.base_test_registration import BaseTestRegistration
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class RegistrationTests(BaseTestRegistration):
    def setUp(self):
        super().setUp()

    def test_RegistrationPageTest_ID_002(self):

        logo_rejestracja = self.driver.find_element(By.XPATH, '//*[@id="register"]/h1')
        if logo_rejestracja.is_displayed():
            print("PASS: Registration Page loaded successfully")
        else:
            print("FAILED: No visible registration logo")


    def test_Registration_correct_email_and_password_ID_003(self):
        self.input_email(self.fake.email())
        self.input_password(self.fake.password(12))
        self.sign_up()

        register_correct = self.driver.find_element(By.XPATH, "//*[@id='col-content']/span")
        self.wait.until(EC.visibility_of(register_correct))
        if register_correct.is_displayed():
                print("Account has been created")


    def test_Registration_non_email_ID_004(self):
        self.input_email("")
        self.input_password(self.fake.password(12))
        self.sign_up()

        self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='register-form']/fieldset/p[1]/span")))
        non_email_mess = self.driver.find_element(By.XPATH, "//*[@id='register-form']/fieldset/p[1]/span")
        if non_email_mess.is_enabled():
                print("Account has NOT been created: Email is required")



    def test_Registration_invalid_email_ID_005(self):
        self.input_email("tester0597@onet")
        self.input_password("Tester0597")
        self.sign_up()

        self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='register-form']/fieldset/p[1]/span")))
        invalid_email_mess = self.driver.find_element(By.XPATH, "//*[@id='register-form']/fieldset/p[1]/span")
        if invalid_email_mess.is_enabled():
                print("The Email field does not contain a valid email address.")



    def test_Registration_non_password_ID_006(self):
        self.input_email(self.fake.email())
        self.input_password("")

        pass_doesnt_meet_requirements = self.driver.find_element(By.XPATH, "//*[@id='passwordMeter']/div[3]")
        if pass_doesnt_meet_requirements.is_displayed():
            print("Password doesnt meet requirements")
        else:
            self.sign_up()

    def test_Registration_too_short_password_ID_007(self):
        self.input_email(self.fake.email())
        self.input_password(self.fake.password(5))

        pass_doesnt_meet_requirements = self.driver.find_element(By.XPATH, "//*[@id='passwordMeter']/div[3]")
        if pass_doesnt_meet_requirements.is_displayed():
            print("Password doesnt meet requirements")
        else:
            self.sign_up()

    def test_Registration_without_numbers_password_ID_008(self):
        self.input_email(self.fake.email())
        self.input_password(self.fake.password(digits=False))

        pass_doesnt_meet_requirements = self.driver.find_element(By.XPATH, "//*[@id='passwordMeter']/div[3]")
        if pass_doesnt_meet_requirements.is_displayed():
            print("Password doesnt meet requirements")
        else:
            self.sign_up()

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

    def tearDown(self):
        self.driver.quit()
