from  selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



#if you run the scenario in target_search.feature ,it will give error as this is already defined in target_steps.py
# @given('Open target main page')
# def open_main(context):
#     context.driver.get("https://www.target.com/")
# # give 2 lines after this to start with when
# sleep(5)