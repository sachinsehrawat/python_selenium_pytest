from selenium.webdriver.common.by import By


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
        return self.driver.find_element(*Checkout.finalCheckout)