from Base_Tests.base_test_buying import BaseTestBuying
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.common.exceptions import TimeoutException

class BuyingTests(BaseTestBuying):
    def setUp(self):
        super().setUp()

    def test_searching_item_ID_013(self):
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



    def input_item_name(self, item_name):
        input_item_name = self.driver.find_element(By.XPATH, "//*[@id='pageHeader']/div[2]/div[3]/div/input")
        input_item_name.send_keys(item_name)

    def click_search(self):
        click_search = self.driver.find_element(By.XPATH, "//*[@id='pageHeader']/div[2]/div[3]/div[1]/a")
        click_search.click()