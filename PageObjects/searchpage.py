from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class LoginPage:
    # Login Page




    def __init__(self, driver):
        self.driver = driver
        self.search_box = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')



    def input_search(self, text):
        self.search_box.clear()
        self.search_box.send_keys(text)

    def enterSearch(self):
        self.search_box.send_keys(Keys.ENTER)
