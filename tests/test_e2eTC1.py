import pytest
from PageObjects.checkoutpage import Checkoutpage
from PageObjects.confirmationpage import Confirmation
from PageObjects.homepage import HomePage
from PageObjects.purchase import Purchase
from tests.conftest import setup
from utilities.BaseClass import BaseClass
from selenium.webdriver.support import wait

class TestE2E(BaseClass):
    def test_e2e(self):

        homePage = HomePage(self.driver)
        checkoutpage = homePage.shopItems() #create object for checkout from previous page only
        products = checkoutpage.getCardtitle()
        n=0
        for product in products:
            if 'Blackberry' in product.text:
                checkoutpage.getCardfooter()[n].click()
                prodName = product.text
                print(prodName)
            n = n + 1
        # Checkout
        confirmation = Confirmation(self.driver)
        confirmation.confirmCheckout().click()
        # check if same product has been added in the cart
        cartprod = confirmation.confirmProduct()
        assert prodName == cartprod.text
        purchase = confirmation.buttonSuccess()
        purchase.findCountry().send_keys("India")
        purchase.selectCountry().click() # Select India
        purchase.clickPurchase().click()
        successmsg = self.driver.find_element_by_class_name("alert-success").text
        print(successmsg)
        assert "Success! Thank you!" in successmsg
        #self.driver.get_screenshot_as_file("success.png")








