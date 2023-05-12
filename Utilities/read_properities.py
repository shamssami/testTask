from operator import itemgetter


class TestData:
    baseURL = "https:\\Google.com"
    text = "ya Allah Help me"
    @staticmethod
    def getApplicationURL():
        return TestData.baseURL


    @staticmethod
    def getText():
        return TestData.text
