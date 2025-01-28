import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageobject.CheckoutPage import CheckOutPage
from pageobject.HomePage import HomePage
from utilities.BaseClass import BaseClass



class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        homePage.shopItems().click()
        checkOutPage = CheckOutPage(self.driver)
        log.info("getting all the card titles")
        cards = checkOutPage.getCardTitle()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkOutPage.getcardFooter()[i].click()

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        log.info("entering country name as ind")
        self.driver.find_element(By.ID, "country").send_keys("ind")
        #time.sleep(5)
        self.verifyLinkPresence("Indonesia")

        self.driver.find_element(By.LINK_TEXT, "Indonesia").click()
        self.driver.find_element(By. XPATH,("//div[@class='checkbox checkbox-primary']")).click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        textMatch = self.driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text
        log.info("text received from application is"+textMatch)
        assert ("Success! Thank you!" in textMatch)