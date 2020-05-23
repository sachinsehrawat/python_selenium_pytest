import time

import pytest

from TestData.HomePage_test_data import HomePageTestData
from pageObjects.homePage import HomePage
from utilities.baseclass import BaseClass


class TestHomePage(BaseClass):

    def test_form_submission(self, get_data):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        homepage.get_passowrd().send_keys(get_data['password'])
        log.info("Password entered ")
        homepage.get_name().send_keys(get_data['name'])
        homepage.get_checkbox().click()
        homepage.get_email().send_keys(get_data['email'])
        log.info("Email entered")
        homepage.get_button().click()
        log.info("Final button clicked")
        message = homepage.get_success().text
        assert "Succ" in message
        self.driver.refresh()

    #@pytest.fixture(params[{"name": "Sachin", "password": "Sachin", "email": "email@email.com"},
                            #{"name": "Sachin1", "password": "Sachin1", "email": "emai1@email.com"}])

    @pytest.fixture(params= HomePageTestData.test_data)
    def get_data(self, request):
        return request.param
