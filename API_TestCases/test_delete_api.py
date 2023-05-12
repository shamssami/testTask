import requests
import pytest
from selenium import webdriver
from Utilities.read_properities import TestData
from PageObjects.searchpage import LoginPage
import time
from Utilities.customeLogger import LogGen

class Test_Post_API:
    logger = LogGen.loggen()  # Logger

    # Test case: DELETE user with valid ID
    def test_delete_user_valid_id(self):
        url = "https://reqres.in/api/users/2"
        response = requests.delete(url)
        assert response.status_code == 204, "DELETE API endpoint failed to delete user"

    # Test case: DELETE user with valid ID and verify success message is displayed
    def test_delete_user_valid_id_and_verify_message(self):
        url = "https://reqres.in/api/users/2"
        response = requests.delete(url)
        assert response.status_code == 204, "DELETE API endpoint failed to delete user"

        # Verify success message is displayed
        message = "User deleted successfully"
        response_content = response.content

        assert message.encode('utf-8') in response_content, " not found in response content"

    # Test case: DELETE user with missing ID
    def test_delete_user_missing_id(self):
        url = "https://reqres.in/api/users/"
        response = requests.delete(url)
        assert response.status_code == 404, "DELETE API endpoint failed to return expected status code"
        assert "Not Found" in response.json()["error"], "Unexpected error message returned"