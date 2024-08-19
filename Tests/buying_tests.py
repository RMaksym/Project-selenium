from Base_Tests.base_test_buying import BaseTestBuying
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.common.exceptions import TimeoutException
from Data.locators import DANE
class BuyingTests(BaseTestBuying):
    def setUp(self):
        super().setUp()

    def test_buying_item_by_name_ID_013(self):
        self.input_item_name("Burberry Hero")
        sleep(1)
        self.click_search()
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='navigationMainWrapper']/div[3]")))
            searching_result = self.driver.find_element(By.XPATH, "//*[@id='navigationMainWrapper']/div[3]")
            if searching_result.is_displayed():
                print("Search successfull")
        except TimeoutException:
            print("Error: Confirmation of receivables required")

        self.burberry_hero_click()
        self.fragnance_buy()
        self.go_to_shopping_basket()
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div/div[1]/div/div[1]/div")))
            addition_of_fragnance = self.driver.find_element(By.XPATH, "//*[@id='app']/div/div[1]/div/div[1]/div")
            if addition_of_fragnance.is_enabled():
                print("Fragnance added to basket")
        except TimeoutException:
            print("Error: Fragnance not added")

    def test_removeing_item_from_basket_ID_014(self):
        self.open_basket()
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div/div[1]/div/div[1]/div")))
            addition_of_fragnance = self.driver.find_element(By.XPATH, "//*[@id='app']/div/div[1]/div/div[1]/div")
            if addition_of_fragnance.is_enabled():
                self.remove_item().click
        except TimeoutException:
            print("Error: Confirmation of receivables required")
        self.driver.implicitly_wait(3)
        current_page = self.driver.current_url
        if self.assertEqual(DANE.HomePageURL, current_page):
            print("Successful removal")

    def remove_item(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app]/div/div[1]/div/div[1]/div/div[2]/div[6]/a")))
        remove_btn = self.driver.find_element(By.XPATH, "//*[@id='app]/div/div[1]/div/div[1]/div/div[2]/div[6]/aa")
        remove_btn.click()
    def open_basket(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='pageHeader']/div[2]/div[4]/a")))
        basket_btn = self.driver.find_element(By.XPATH, "//*[@id='pageHeader']/div[2]/div[4]/a")
        basket_btn.click()
    def go_to_shopping_basket(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app-ebe6cdab-dbe2-4741-8065-3ce5d42f7e54']/div[1]/div/div/div/div/div[2]/div/a/button")))
        go_to_shopping_basket_btn = self.driver.find_element(By.XPATH,"//*[@id='app-ebe6cdab-dbe2-4741-8065-3ce5d42f7e54']/div[1]/div/div/div/div/div[2]/div/a/button")
        go_to_shopping_basket_btn.click()
    def fragnance_buy(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='pd-buy-button']")))
        fragnance_buy_btn = self.driver.find_element(By.XPATH,"//*[@id='pd-buy-button']")
        fragnance_buy_btn.click()
    def burberry_hero_click(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='productListWrapper']/div[2]/div[1]/a/div[2]/img")))
        burberry_hero_bnt = self.driver.find_element(By.XPATH,"//*[@id='productListWrapper']/div[2]/div[1]/a/div[2]/img")
        burberry_hero_bnt.click()

    def input_item_name(self, item_name):
        input_item_name = self.driver.find_element(By.XPATH, "//*[@id='pageHeader']/div[2]/div[3]/div/input")
        input_item_name.send_keys(item_name)

    def click_search(self):
        click_search = self.driver.find_element(By.XPATH, "//*[@id='pageHeader']/div[2]/div[3]/div[1]/a")
        click_search.click()

    def tearDown(self):
        self.driver.quit()
