from selenium.webdriver.common.by import By

from pageObjects.confirmPage import ConfirmPage


class Checkout:
    selectItem = (By.CSS_SELECTOR, ".card.h-100")

    def __init__(self, driver):
        self.driver = driver

    def getitems(self):
        return self.driver.find_elements(*Checkout.selectItem)

    cartCheckout = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def cartCheck(self):
        return self.driver.find_element(*Checkout.cartCheckout)

    finalCheckout = (By.XPATH, "//*[contains(@class,'btn-success')]")

    def finalCheck(self):
        self.driver.find_element(*Checkout.finalCheckout).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page