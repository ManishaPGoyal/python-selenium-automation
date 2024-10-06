from time import sleep

from selenium.webdriver.common.by import By

#there should be gap between libraries import and import from package
from pages.base_page import Page
     # IF write here then only write SEARCH_FIELD
class Header(Page):
    #we write this inside the th class so used *self.SEARCH_FIELD
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN=(By.XPATH, "//button[@data-test='@web/Search/SearchButton']")

    CART_BTN=(By.CSS_SELECTOR, "[data-test='@web/CartIcon']")


    def search_product(self,product):
        self.input_text(product,*self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(6)

    def click_cart_icon(self):
        self.click(*self.CART_BTN)
        sleep(6)


