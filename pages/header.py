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
    SIGNIN_BTN=(By.CSS_SELECTOR,"[class*='kwbrXj h-margin-r']")
    SIDENAV_SIGNIN=(By.CSS_SELECTOR,"#listaccountNav-signIn")

    #to make wait_to_be_clickable fail we, changed it
    #CART_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartIcon232424434343']")

    #lesson6
    def search_product(self,product):
        self.input_text(product,*self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(6)

     #lesson7 to use wait until vissibility
        #self.wait_for_element_to_appear(*self.SEARCH_BTN)

      #lesson 7 comment this to use wait until in
    # def click_cart_icon(self):
    #     self.click(*self.CART_BTN)
    #     sleep(6)

    #lesson7
    #we use wait until to getrid ods sleep in above same function
    # def click_cart_icon(self):
    #     self.wait_to_be_clickable_click(*self.CART_BTN)

       # showing the concept of staleexception element
    #one way
    # def click_cart_icon(self):
    #     #self.wait_to_be_clickable_click(*self.CART_BTN)
    #     cart_btn=self.driver.find_element(*self.CART_BTN)
    #     print(cart_btn)
    #     # first time run
    #     # session="8711dde9b98c96e468bcde3761a13506",
    #     # element="f.F3C3DA4556E71941091100951CEB018E.d.A24EFA6F9EA335DE8EC46383D8B083E3.e.375")>
    #     # second time run
    #     # session="290f761a95b898d7d1ff4506dd9cc4a2",
    #     # element="f.72819B90AB8C95DBF0C15B7A8290EB1B.d.0F1B8BE23725FB6247165502897D3BA7.e.374")>
    #     cart_btn.click()


      #with refresh command the session id same but element id deifferent
    #second way
    # def click_cart_icon(self):
    #     cart_btn = self.driver.find_element(*self.CART_BTN)
    #     print('before refresh',cart_btn)
    #      #session="1a7443ef80baba4e216dcb3624c738f3",
    #     # element="f.E1865BD225AA41A95C914FB5D3B02C96.d.8144898A763E5A858884F45C4BEC1E97.e.348")>
    #
    #
    #     self.driver.refresh()
    #
    #     cart_btn = self.driver.find_element(*self.CART_BTN)
    #     print('After refresh', cart_btn)
    #     #session="1a7443ef80baba4e216dcb3624c738f3"
    #     #element="f.E1865BD225AA41A95C914FB5D3B02C96.d.AC4EE29873B5E185CC31F87B0779B14D.e.4085")>
    #     cart_btn.click()

        #third way
    #this time give error because when run, cart button has id
      #if refresh it, the id will change ,and if you click ,it still having old id
       # so it give 'sate element reference 'error
    def click_cart_icon(self):
        cart_btn = self.driver.find_element(*self.CART_BTN)
        print('before refresh', cart_btn)

        self.driver.refresh()

        cart_btn.click()

     # to avoid 'staleelement exception' ,
    # do find element and do function on it ,no command like refresh in between.
    #you can give like this cart_btn = self.driver.find_element(*self.CART_BTN).clicl()


    #lesson 7 homework part1
    def click_signin(self):
        self.click(*self.SIGNIN_BTN)

    def click_sidenav_signin(self):
        self.click(*self.SIDENAV_SIGNIN)