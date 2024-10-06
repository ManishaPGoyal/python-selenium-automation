from selenium.webdriver.common.by import By

from pages.base_page import Page


class Cart(Page):
    CART_MESSAGE = (By.XPATH, "//div[@data-test='boxEmptyMsg']")

    def verify_cart_empty_message(self):
        actual_result =self.driver.find_element(*self.CART_MESSAGE).text
        expected_result = 'Your cart is empty'
        assert expected_result == actual_result, f'Expected {expected_result} but got {actual_result}'