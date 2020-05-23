import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects import checkout
from pageObjects.checkout import Checkout
from pageObjects import confirmPage
from pageObjects.confirmPage import ConfirmPage
from pageObjects.homePage import HomePage
from utilities.baseclass import BaseClass


class TestSel(BaseClass):
    def test_selenium(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkout = homePage.homepageitems()
        items = checkout.getitems()
        for item in items:
            if item.find_element_by_xpath("div/h4").text == "Nokia Edge":
                item.find_element_by_css_selector(".btn.btn-info").click()
                break
        log.info("Item Selected")
        checkout.cartCheck().click()
        confirm_page = checkout.finalCheck()
        confirm_page.get_country().send_keys("ind")
        self.wait_utility("India")
        countries = confirm_page.send_country()
        for country in countries:
            if country.text == 'India':
                country.click()
                break
        log.info(" Country entered")
        confirm_page.check_terms().click()
        confirm_page.click_purchase().click()
        result = confirm_page.confirm_message().text
        log.info(result)
        assert 'SuccT' in result
        self.driver.get_screenshot_as_file("result.png")
