from selenium.webdriver.common.by import By

from pageObjects.checkout import Checkout


class HomePage:

    shopItem = (By.LINK_TEXT, "Shop")
    #self.driver.find_element_by_link_text("Shop").click()

    def __init__(self, driver):
        self.driver = driver

    def homepageitems(self):
        self.driver.find_element(*HomePage.shopItem).click()
        checkout = Checkout(self.driver)
        return checkout

    password = (By.ID, "exampleInputPassword1")

    def get_passowrd(self):
        return self.driver.find_element(*HomePage.password)

    name = (By.NAME, "name")
    checkbox = (By.CLASS_NAME, "form-check-input")
    button = (By.XPATH, "//input[@type='submit']")
    email = (By.CSS_SELECTOR, "input[name='email']")
    success = (By.XPATH, "//*[contains(@class,'alert-success')]")

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_checkbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def get_button(self):
        return self.driver.find_element(*HomePage.button)

    def get_email(self):
        return self.driver.find_element(*HomePage.email)

    def get_success(self):
        return self.driver.find_element(*HomePage.success)
