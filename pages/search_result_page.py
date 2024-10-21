from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from pages.base_page import Page

class SearchResultPage(Page):

    SEARCH_RESULT_HEADER=(By.XPATH, "//div[@data-test='resultsHeading']")
    #command for heart icon.$$("[data-test='FavoritesButton']")
    HEART_ICON=(By.CSS_SELECTOR, "[data-test='FavoritesButton']")
    FAV_TOOLTIP=(By.XPATH, "//*[contains(text(),'Click to sign in and save')]")


#comment following to rewrite in lesson7
    # def verify_result(self,product):
    #     actual_result = self.driver.find_element(*self.SEARCH_RESULT_HEADER).text
    #     # print(actual_result)
    #     assert product in actual_result, f'Expected result{product} but got {actual_result}'
    #     sleep(6)

#lesson 7 modify verify_result also in base page
    def verify_result(self, product):
        self.verify_partial_text(product, *self.SEARCH_RESULT_HEADER)
         ## following if pass wrong product name to check error message
        #self.verify_partial_text('1223455565y',*self.SEARCH_RESULT_HEADER)
        sleep(6)

    def verify_result_url(self,product):
        self.verify_partial_url(product)
        #to make it fail use
        #self.verify_partial_url('1234565657h')

    #lesson 9 practice
    def hover_favorites(self):
        #pass
       heart_icon = self.find_element(*self.HEART_ICON)
       actions = ActionChains(self.driver)
       sleep(4)
       actions.move_to_element(heart_icon)
       #can also write like this
       #actions.move_to_element(self.find_element(*self.HEART_ICON))
       actions.perform()
        #also write in one line
        #actions.move_to_element(heart_icon).perform()
       sleep(5) #dont need it but to see


    def verify_favorites(self):
        #pass
        self.wait_for_element_to_appear(*self.FAV_TOOLTIP)