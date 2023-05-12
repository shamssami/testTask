import requests
import pytest
from selenium import webdriver
from Utilities.read_properities import TestData
from PageObjects.searchpage import LoginPage
import time
from Utilities.customeLogger import LogGen

class Test_Post_API:
    logger = LogGen.loggen()  # Logger
    BASE_URL = "https://reqres.in"

    # Test POST /users endpoint
    def test_add_user(self):
        url = "https://reqres.in/api/users"
        data = {
            "name": "Shams",
            "job": "Engineer"
        }
        print("Tessssssssssssssssttttttttttttttttt")
        response = requests.post(url, data=data)
        print(response.status_code)
        assert response.status_code == 201, "POST /users endpoint success"
        assert response.json()["name"] == data["name"]
        assert response.json()["job"] == data["job"]
        print(response.json())



