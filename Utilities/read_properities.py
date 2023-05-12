from operator import itemgetter
class TestData:
    baseURL = "https://www.aircanada.com/ca/en/aco/home.html"
    text = "Selenium Test"
    source = "Amman"
    destination = "Dubai"
    startDate = "13/05/2023"
    endDate = "1/06/2023"

    @staticmethod
    def getApplicationURL():
        return TestData.baseURL

    @staticmethod
    def getSource():
        return TestData.source

    @staticmethod
    def getDestination():
        return TestData.destination

    @staticmethod
    def getStartDate():
        return TestData.startDate

    @staticmethod
    def getEndDate():
        return TestData.endDate

class API_links:
    get_users_api = "https://reqres.in/api/users/"


    @staticmethod
    def getAllUsersAPI():
        return API_links.get_users_api

