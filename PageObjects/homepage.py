from selenium.webdriver.common.by import By

from PageObjects.checkoutpage import Checkoutpage
from utilities.BaseClass import BaseClass


class HomePage:

    # Create a constructor for the driver, to be called from test case script
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.XPATH, "//input[@name='name']")
    email = (By.XPATH, "//input[@name='email']")
    password = (By.XPATH, "//input[@type='password']")
    gender = (By.XPATH, "//select[ @ id = 'exampleFormControlSelect1']/option[1]")
    employstatus = (By.XPATH, "//input[@value='option2']")
    bday = (By.XPATH, "// input[ @ name = 'bday']")
    successmsg = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    submitButton = (By.XPATH, "//input[@value='Submit']")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click() # De serialize the touple with *
        return Checkoutpage(self.driver)

    def fillName(self):
        return self.driver.find_element(*HomePage.name)

    def fillEmail(self):
        return self.driver.find_element(*HomePage.email)
    def fillPassword(self):
        return self.driver.find_element(*HomePage.password)

    def fillGender(self):
        return self.driver.find_element(*HomePage.gender)

    def fillEmploymentStatus(self):
        return self.driver.find_element(*HomePage.employstatus)

    def fillBday(self):
        return  self.driver.find_element(*HomePage.bday)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submitButton)

    def successMsg(self):
        return self.driver.find_element(*HomePage.successmsg) #Dont keep same name for variable or function

