from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import Page

class SearchResultPage(Page):
    SEARCH_RESULT_HEADER=(By.XPATH, "//div[@data-test='resultsHeading']")

    def verify_result(self,product):
        actual_result = self.driver.find_element(*self.SEARCH_RESULT_HEADER).text
        # print(actual_result)
        assert product in actual_result, f'Expected result{product} but got {actual_result}'
        sleep(6)