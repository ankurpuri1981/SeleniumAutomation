import pytest
from PageObjects.checkoutpage import Checkoutpage
from PageObjects.confirmationpage import Confirmation
from PageObjects.homepage import HomePage
from PageObjects.purchase import Purchase
from tests.conftest import setup
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
from selenium.webdriver.support import wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        # try:
        #     element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(confirmation.confirmCheckout))
        confirmation.confirmCheckout().click()
        # except:
        #     print('the checkout button is not found')
        #     # check if same product has been added in the cart
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








