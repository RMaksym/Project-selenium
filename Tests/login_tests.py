from Base_Tests.base_test_login import BaseTestLogin
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class LoginTests(BaseTestLogin):
    def setUp(self):
        super().setUp()

    def test_Login_Page_ID_009(self):
        logo_login = self.driver.find_element(By.CLASS_NAME, ("header"))
        if logo_login.is_displayed():
            print("PASS: Registration Page loaded successfully")
        else:
            print("FAILED: No visible registration logo")

    def test_SignIn_correct_login_and_pass_ID_010(self):
        self.input_email_log("tester0597@onet.pl")
        self.input_password_log("Tester0597")
        self.sign_in()

        self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='myNotinoApp']/div[3]/div/div[1]/div[2]/div[6]/a")))
        log_out_btn = self.driver.find_element(By.XPATH, "//*[@id='myNotinoApp']/div[3]/div/div[1]/div[2]/div[6]/a")
        if log_out_btn.is_enabled():
            print("Signed in successfully")


    def test_SignIn_invalid_login_ID_011(self):
        self.input_email_log(self.fake.email())
        self.input_password_log("Tester0597")
        self.sign_in()

        self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='login-form']/fieldset/p[5]/span")))
        login_filed = self.driver.find_element(By.XPATH, "//*[@id='login-form']/fieldset/p[5]/span")
        if login_filed.is_enabled():
            print("The e-mail or password you entered is incorrect.")

    def test_SignIn_invalid_password_ID_012(self):
        self.input_email_log("tester0597@onet.pl")
        self.input_password_log(self.fake.password(12))
        self.sign_in()

        self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='login-form']/fieldset/p[5]/span")))
        password_filed = self.driver.find_element(By.XPATH, "//*[@id='login-form']/fieldset/p[5]/span")
        if password_filed.is_enabled():
            print("The e-mail or password you entered is incorrect.")

    def input_email_log(self, email):
         email_window_log = self.driver.find_element(By.XPATH, "//*[@id='Email']")
         self.wait.until(EC.visibility_of(email_window_log))
         email_window_log.send_keys(email)
    def input_password_log(self, password_log):
        password_window_log = self.driver.find_element(By.XPATH, "//*[@id='Password']")
        password_window_log.send_keys(password_log)
    def sign_in(self):
         sign_in_btn = self.driver.find_element(By.XPATH, "//*[@id='login-form']/fieldset/p[7]/button")
         sign_in_btn.click()
    def tearDown(self):
        self.driver.quit()



