from selenium.webdriver.common.by import By

from pageobject.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By. CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")


    def getCardTitle(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getcardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def getcheckOutItems(self):
        self.driver.find_element(*CheckOutPage.checkOut).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage