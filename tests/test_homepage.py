import pytest
import os
import PageObjects
from PageObjects.homepage import HomePage
from TestData.test_HomePageData import HomePageData
from utilities.BaseClass import BaseClass

class Test_HomePageVerify(BaseClass):

    def test_Formsubmission(self, getData):  # Trying to enter data from fixture tuples
        logger = self.test_loggerf()
        # self.driver.find_element_by_xpath("//input[@name='name']").send_keys("Ankur Puri")
        # self.driver.find_element_by_xpath("//input[@name='email']").send_keys("ankurk.puri@gmail.com")
        # self.driver.find_element_by_xpath("//input[@type='password']").send_keys("ankurpwd")
        # self.driver.find_element_by_xpath("// select[ @ id = 'exampleFormControlSelect1']/option[1]").click() #Choose Male
        # self.driver.find_element_by_xpath("//input[@value='option2']").click()
        # self.driver.find_element_by_xpath("// input[ @ name = 'bday']").send_keys("08/02/1981")
        # self.driver.find_element_by_xpath("//input[@value='Submit']").click()
        homepageform = HomePage(self.driver)

        homepageform.fillName().send_keys(getData["Name"])
        homepageform.fillEmail().send_keys("ankurk.puri@gmail.com")
        homepageform.fillPassword().send_keys(getData["Password"])
        homepageform.fillGender().click()
        homepageform.fillBday().send_keys(getData["Bday"])
        homepageform.fillEmploymentStatus().click()
        homepageform.submitForm().click()
        logger.info("Form submitted by user")
        successmsg = homepageform.successMsg()
        logger.info("The message on the screen is" + successmsg.text)
        assert "Success" in successmsg.text
        self.driver.refresh()  # Refresh the page for clearing fields for next run

    # @pytest.fixture(params=[("Ankur","Puri","09/10/1982"),("Ayansh","Puri","26/06/2013")]) #To run test with multiple datasets

    #os.chdir("..")  #This is only needed for local pycharm run, as on azure repo agents, the file is found without
    # moving to parent folder
    print(os.getcwd())
    datafile = os.getcwd() + "/TestData/testData.xlsx"

    homepagedata = HomePageData(datafile)
    @pytest.fixture(params=homepagedata.read_Datafromexcel())
    def getData(self, request):
        return request.param
