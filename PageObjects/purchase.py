from selenium.webdriver.common.by import By

class Purchase:

    def __init__(self,driver):
        self.driver = driver

    #self.driver.find_element_by_id("country").send_keys("india")
    countryName = (By.ID, "country")
    selectCountryfromlist = (By.XPATH, "//div[@class='suggestions']/ul/li")
    successButton = (By.CLASS_NAME, "btn-success")

    def findCountry(self):
        self.driver.switch_to.window(self.driver.current_window_handle)
        return self.driver.find_element(*Purchase.countryName)

    def selectCountry(self):
        return self.driver.find_element(*Purchase.selectCountryfromlist)

    def clickPurchase(self):
        return self.driver.find_element(*Purchase.successButton)
