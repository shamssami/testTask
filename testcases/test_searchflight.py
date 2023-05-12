import pytest
from selenium import webdriver
from Utilities.read_properities import TestData
from PageObjects.SearchFlight import SearchFlight
import time
from Utilities.customeLogger import LogGen

class Test_001_Search:
    logger = LogGen.loggen()  # Logger

    def test_homePageTitle(self, test_setup):
        self.logger.info("******* Starting Test_11_Title Test **********")
        # create a new instance of the Firefox driver
        self.driver = test_setup
        # Set the implicit wait time to 10 seconds

        self.driver.get(TestData.getApplicationURL())
        self.driver.implicitly_wait(10)

        actual_title=self.driver.title
        # navigate to the Python website

        if actual_title == "Air Canada":
            self.logger.info("**** test passed ****")
            self.driver.save_screenshot(".\\Screenshots\\"+"Test1.png")
            self.driver.close()
            assert True
        else:
            self.logger.info("**** test failed ****")
            self.driver.close()
            assert False


    def test_searchflight(self,test_setup):
        self.logger.info("******* Starting Test_12_Search_Flight Test **********")

        self.driver = test_setup

        # create a new instance of the Firefox driver
        self.driver.get(TestData.getApplicationURL())
        # navigate to the Python website
        self.sf = SearchFlight(self.driver)
        self.sf.input_source(TestData.getSource())
        self.sf.input_destination(TestData.getDestination())
        self.sf.select_start_date(TestData.getStartDate())
        self.sf.select_end_date(TestData.getEndDate())
        self.sf.click_search()
        self.sf.check_loading_icon()
        self.driver.save_screenshot(".\\Screenshots\\" + "test_1.png")
        self.logger.info("**** finished ****")

        self.driver.close()



    def test_searchflight_invalid(self,test_setup):
        self.logger.info("******* Starting Test_13_Search_Flight Test Without Filling Required Field **********")

        self.driver = test_setup

        # create a new instance of the Firefox driver
        self.driver.get(TestData.getApplicationURL())
        # navigate to the Python website
        self.sf = SearchFlight(self.driver)
        self.sf.input_source(TestData.getSource())
        self.sf.select_start_date(TestData.getStartDate())
        self.sf.select_end_date(TestData.getEndDate())

        self.sf.check_error_msg()
        self.driver.save_screenshot(".\\Screenshots\\" + "test3_search_flight.png")
        self.logger.info("**** finished ****")

        self.driver.close()




