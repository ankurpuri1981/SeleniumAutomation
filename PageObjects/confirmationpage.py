from selenium.webdriver.common.by import By

from PageObjects.purchase import Purchase


class Confirmation:

    def __init__(self,driver):
        self.driver = driver

    checkOutconfirm = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    cartProd = (By.XPATH, "//h4[@class='media-heading']")
    successButton = (By.CLASS_NAME, "btn-success")

    def confirmCheckout(self):
        return self.driver.find_element(*Confirmation.checkOutconfirm)

    def confirmProduct(self):
        return self.driver.find_element(*Confirmation.cartProd)

    def buttonSuccess(self):
        self.driver.find_element(*Confirmation.successButton).click()
        purchase = Purchase(self.driver)
        return purchase