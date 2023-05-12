from selenium import webdriver
import pytest


@pytest.fixture()
def test_setup():
    driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    driver.implicitly_wait(5)
    driver.maximize_window()
    return driver


########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'UI Automation'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Shams'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

