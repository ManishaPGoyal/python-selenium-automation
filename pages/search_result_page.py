from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import Page

class SearchResultPage(Page):
    SEARCH_RESULT_HEADER=(By.XPATH, "//div[@data-test='resultsHeading']")

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