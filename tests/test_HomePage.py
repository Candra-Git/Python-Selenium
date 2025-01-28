import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib3 import request

from TestData.HomePageData import HomePageData
from pageobject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("first name is "+getData["fullname"])
        homepage.getName().send_keys(getData["fullname"]) #bisa pake [0]
        homepage.getEmail().send_keys(getData["email"])
        homepage.getCheck().click()
        self.selectOptionByText(homepage.getGender(), getData["gender"])
        homepage.getSubmit().click()
        alertText = homepage.getSuccessMessage().text
        assert ("Success" in alertText)



    @pytest.fixture(params = HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param
