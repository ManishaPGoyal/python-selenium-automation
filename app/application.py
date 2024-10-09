from tkinter.constants import PAGES

from pages.base_page import Page
from pages.cart_page import Cart
from pages.header import Header
from pages.main_page import MainPage
from pages.product_page import Product
from pages.search_result_page import SearchResultPage
from pages.sign_in_page import SignInPage


class Application:
    def __init__(self,driver):
        self.base_page=Page(driver)
        self.main_page = MainPage(driver)
        self.header=Header(driver)
        self.search_result_page=SearchResultPage(driver)
        self.cart_page=Cart(driver)
        self.sign_in_page=SignInPage(driver)
        self.product_page=Product(driver)