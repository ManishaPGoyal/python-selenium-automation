from selenium.webdriver.common.by import By

from pages.base_page import Page



class TargetSignInPage(Page):

   # Homework 8 part 1
   #CSS_Selector=$$("[aria-label='terms & conditions - opens in a new window']")
   #XPATH=$x("//a[text()='Target terms and conditions']")
  #TERM_CONDITION_LINK = (By.XPATH,"//a[text()='Target terms and conditions']")
  TERM_CONDITION_LINK =(By.CSS_SELECTOR,"[aria-label='terms & conditions - opens in a new window']")
   #sign_in_btn= $$("[class*='sc-58ad44c0-3 kwbrXj h-margin-r-x3']")
  SIGN_IN_BTN=(By.CSS_SELECTOR,"[class*='sc-58ad44c0-3 kwbrXj h-margin-r-x3']")
  #sidenav_sign_in=$$("[data-test='accountNav-signIn']")
  SIDENAV_SIGNIN=(By.CSS_SELECTOR,"[data-test='accountNav-signIn']")

  def open_sign_in(self):
      self.open('https://www.target.com/login')
      #self.open('https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_signin')


  def click_sign_in_button(self):
      self.click(*self.SIGN_IN_BTN)

  def click_sidenav_sign_in(self):
      self.click(*self.SIDENAV_SIGNIN)

  def click_terms_link(self):
      self.wait_to_be_clickable_click(*self.TERM_CONDITION_LINK)

  def verify_terms_condition_opened(self):
      self.verify_partial_url('/terms-conditions/')