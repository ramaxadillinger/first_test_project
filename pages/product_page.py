import math
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def can_add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.PRODUCT_BUTTON)
        button.click()


