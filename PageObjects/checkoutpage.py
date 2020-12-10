from selenium.webdriver.common.by import By
from PageObjects.confirmationpage import Confirmation


class Checkoutpage:

    def __init__(self,driver):
        self.driver = driver
    cardTitle = (By.CSS_SELECTOR,".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")

    def getCardtitle(self):
        return self.driver.find_elements(*Checkoutpage.cardTitle)

    def getCardfooter(self):
        return self.driver.find_elements(*Checkoutpage.cardFooter)
