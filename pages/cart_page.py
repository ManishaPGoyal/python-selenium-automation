from selenium.webdriver.common.by import By

from pages.base_page import Page


class Cart(Page):
    CART_MESSAGE = (By.XPATH, "//div[@data-test='boxEmptyMsg']")
    ADD_TO_CART_BTN=(By.CSS_SELECTOR, "[id*='addToCartButton']")
    SIDE_NAV_ADD_TO_CART_BTN=(By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")

     #lesson 6 hw
    # def verify_cart_empty_message(self):
    #     actual_result =self.driver.find_element(*self.CART_MESSAGE).text
    #     expected_result = 'Your cart is empty'
    #     assert expected_result == actual_result, f'Expected {expected_result} but got {actual_result}'
    #
 # commmented above for lesson 7
    def verify_cart_empty_message(self):
        self.verify_text('Your cart is empty',*self.CART_MESSAGE)


#lesson 7  homework part 2
    def open_cart(self):
        self.open("https://www.target.com/cart")

    def click_add_to_cart_btn(self):
        self.wait_to_be_clickable_click(*self.ADD_TO_CART_BTN)

    def side_nav_click_add_to_cart_btn(self):
        self.click(*self.SIDE_NAV_ADD_TO_CART_BTN)

    # def verify_cart_product(self):
    #     self.verify_partial_text()

