from selenium.webdriver.common.by import By

from pages.base_page import Page


class TargetAppPage(Page):

    #privacy page link
    #by xpath $x("//a[text()='Privacy policy']")
    #by css $$("[aria-label*='privacy policy']")
    PP_LINk=(By.XPATH,"//a[text()='Privacy policy']")
    def open_target_app(self):
        self.open('https://www.target.com/c/target-app/-/N-4th2r')

    def click_pp_link(self):
        self.wait_to_be_clickable_click(*self.PP_LINk)

    def verify_pp_opened(self):
        self.verify_partial_url('/target-privacy-policy/')