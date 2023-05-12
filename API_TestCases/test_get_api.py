import requests
import pytest
from selenium import webdriver
from Utilities.read_properities import TestData
from PageObjects.searchpage import LoginPage
import time
from Utilities.customeLogger import LogGen

class Test_002_API:
    logger = LogGen.loggen()  # Logger
    BASE_URL = "https://reqres.in"

    def test_get_resource(self):
        response = requests.get(self.BASE_URL+ "/api/users?page=2")
        print(response.content)
        assert response.status_code == 200

# Test get all users API
    def test_get_users(self):
        url = "https://reqres.in/api/users?page=2"
        response = requests.get(url)
        print("test all users ")
        print("Total number of returned users is: ",len(response.json()))
        assert response.status_code == 200, "GET /users endpoint failed"
        assert len(response.json()) > 0, "No users returned by GET /users endpoint"
