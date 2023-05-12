import requests
import pytest
from selenium import webdriver
from Utilities.read_properities import TestData
from PageObjects.searchpage import LoginPage
import time
from Utilities.customeLogger import LogGen

class Test_GetUser_API:
    logger = LogGen.loggen()  # Logger

    # Test case: GET single user with valid user ID
    def test_get_user(self):
        url = "https://reqres.in/api/users/2"
        response = requests.get(url)
        print("test single users ")

        assert response.status_code == 200
        assert response.json()["data"]["id"] == 2, "Returned user ID does not match requested user ID"


# Test case: GET single user with invalid user ID
#In the second test case, we test the endpoint with an invalid user ID
# and expect a response with a status code of 404 and an error message
# indicating that the user was not found.

    def test_get_single_user_invalid_id(self):
        url = "https://reqres.in/api/users/23"
        response = requests.get(url)
        print(response.json())
        assert response.status_code == 404, "GET single user API endpoint failed"
        assert "Not Found" in response.json()["error"], "Unexpected error message returned"

