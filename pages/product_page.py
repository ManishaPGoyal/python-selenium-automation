from selenium.webdriver.common.by import By

from pages.base_page import Page


class Product(Page):

    PRODUCT_NAME=(By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
    CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

     #lesson 7 Homework part 2
    def store_the_product(self):
        #product=self.text_check(*self.PRODUCT_NAME)
        #print('product is',product)
        self.product = self.text_check(*self.PRODUCT_NAME)

    def verify_product(self):
        actual_name = self.text_check(*self.CART_ITEM_TITLE)
        print(f'Actual product in cart name:{actual_name}')
        #assert self.product in actual_name, f"Expected{self.product} but got {actual_name}"
        self.verify_partial_text(self.product, *self.CART_ITEM_TITLE)




