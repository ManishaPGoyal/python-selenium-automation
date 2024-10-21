from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import Page


class HelpPage(Page):

     #command for console $x("//h1[text()=' Returns']")
    HEADER_RETURNS=(By.XPATH,"//h1[text()=' Returns']")
     #command for dropdown'choose a topic' $$("select[id*='ViewHelpTopics']")
     #$$("select")
    TOPIC_SELECTION=(By.CSS_SELECTOR,"select[id*='ViewHelpTopics']")
    #TOPIC_SELECTION = (By.CSS_SELECTOR,"select")
    #command for 'current promotions'after clicking dropdown  value promotions & coupons $x("//h1[text()=' Current promotions']")
    HEADER_PROMOTIONS=(By.CSS_SELECTOR,"//h1[text()=' Current promotions']")

    def open_help_returns(self):
        self.open('https://help.target.com/help/subcategoryarticle?childcat=Returns&parentcat=Returns+%26+Exchanges&searchQuery=')

    def select_topic(self):
        dd = self.find_element(*self.TOPIC_SELECTION)
        print(dd)
        select = Select(dd)
        select.select_by_value('Promotions & Coupons')
        sleep(5)

    def verify_returns_opened(self):
         self.wait_for_element_to_appear(*self.HEADER_RETURNS)


    def verify_promotions_opened(self):
        self.wait_for_element_to_appear(*self.HEADER_PROMOTIONS)

 # pass
     # dd used for dropdown
     # select=Select(self.find_element(*self.TOPIC_SELECTION)) #this you can give in one line
     # #we got value from console in incognito for 'choose a topic' value
    #File "C:\Users\parve\OneDrive\Desktop\python-selenium-automation\pages\help_page.py", line 23, in select_topic
#     select = Select(dd)
#              ^^^^^^^^^^
#   File "C:\Users\parve\OneDrive\Desktop\python-selenium-automation\venv\Lib\site-packages\selenium\webdriver\support\select.py", line 38, in __init__
#     if webelement.tag_name.lower() != "select":
#        ^^^^^^^^^^^^^^^^^^^
# AttributeError: 'NoneType' object has no attribute 'tag_name'