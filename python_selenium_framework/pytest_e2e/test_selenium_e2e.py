import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.checkout import Checkout
from pageObjects.confirmPage import ConfirmPage
from pageObjects.homePage import HomePage
from utilities.baseclass import BaseClass


class TestSel(BaseClass):
    def test_selenium(self):
        homePage = HomePage(self.driver)
        homePage.homepageitems().click()
        checkout = Checkout(self.driver)
        items = checkout.getitems()
        for item in items:
            if item.find_element_by_xpath("div/h4").text == "Nokia Edge":
                item.find_element_by_css_selector(".btn.btn-info").click()
                break
        checkout.cartCheck().click()
        checkout.finalCheck().click()
        confirm_page = ConfirmPage(self.driver)
        confirm_page.get_country().send_keys("ind")
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        countries = confirm_page.send_country()
        for country in countries:
            if country.text == 'India':
                country.click()
                break
        confirm_page.check_terms().click()
        confirm_page.click_purchase().click()
        result = confirm_page.confirm_message().text
        assert 'Succ' in result
        self.driver.get_screenshot_as_file("result.png")
