import pytest
from selenium import webdriver
from Utilities.read_properities import TestData
from PageObjects.searchpage import LoginPage
import time
from Utilities.customeLogger import LogGen

class Test_001_Login:
    logger = LogGen.loggen()  # Logger



    def test_homePageTitle(self, test_setup):
        self.logger.info("******* Starting Test_002_DDT_Login Test **********")
        self.logger.info("******* Starting Login DDT Test **********")
        # create a new instance of the Firefox driver
        self.driver = test_setup

        self.driver.get(TestData.getApplicationURL())
        act_title=self.driver.title
        # navigate to the Python website

        if act_title == "Google":
            self.logger.info("**** test passed ****")
            self.driver.save_screenshot(".\\Screenshots\\"+"Test1.png")
            self.driver.close()
            assert True
        else:
            self.logger.info("**** test failed ****")

            self.driver.close()
            assert False


    def test_searchinput(self,test_setup):
        self.logger.info("******* Starting Test_003 Test **********")

        self.driver = test_setup

        # create a new instance of the Firefox driver
        self.driver.get(TestData.getApplicationURL())
        # navigate to the Python website
        self.lp = LoginPage(self.driver)
        self.lp.input_search(TestData.getText())
        self.lp.enterSearch()
        time.sleep(5)
        self.driver.save_screenshot(".\\Screenshots\\" + "test_1.png")

        self.logger.info("**** finished ****")

        self.driver.close()



