import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class SearchFlight:
    def __init__(self, driver):
        self.driver = driver
        self.from_field = driver.find_element(By.XPATH, '//*[@id="bkmgFlights_origin_trip_1"]')
        self.to_field = driver.find_element(By.XPATH, '//*[@id="bkmgFlights_destination_trip_1"]')
        self.departure_field = driver.find_element(By.XPATH,'//*[@id="bkmgFlights_travelDates_1-formfield-1"]')
        self.return_field = driver.find_element(By.XPATH,'//*[@id="bkmgFlights_travelDates_1-formfield-2"]')
        self.passenger_list = driver.find_element(By.XPATH,'//*[@id="bkmgFlights_selectTravelersMainContainer"]/div')
        self.search_button = driver.find_element(By.XPATH,'//*[@id="bkmgFlights_findButton"]/abc-ripple/div')


    def input_source(self, source):
        self.from_field.clear()
        self.from_field.send_keys(source)
        self.departure_field.send_keys(Keys.ENTER)


    def input_destination(self, destination):
        self.to_field.clear()
        self.to_field.send_keys(destination)
        self.departure_field.send_keys(Keys.ENTER)


    def select_start_date(self,startDate):
        self.departure_field.clear()
        self.departure_field.send_keys(startDate)
        self.departure_field.send_keys(Keys.ENTER)

    def select_end_date(self,endDate):
        self.return_field.clear()
        self.return_field.send_keys(endDate)
        self.return_field.send_keys(Keys.ENTER)

    def click_search(self):
        self.search_button.click()

    def check_loading_icon(self):

        # wait for loading image to be displayed
        try:
            WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="pageContent"]/div[1]/ac-page-loader/div/div/img'))
            )

        except:
            # if loading image is not displayed, fail the test
            assert False, "Loading image is not displayed"



    def check_error_msg(self):
        self.to_field.clear()
        time.sleep(5)
        # Wait for the error message to appear
        error_message = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="bkmgFlights_destination_trip_1ErrorText"]/div'))
        )

        # Assert that the error message is displayed with the correct text
        assert error_message.text == 'Please select a valid destination for this trip.'