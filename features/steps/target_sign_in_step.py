from  selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

#homework 8 part 1
@given('Open sign in page')
def open_sign_in_page(context):
    context.app.target_sign_in_page.open_sign_in()

@when('Click on sign in icon')
def click_the_sign_in_button(context):
    context.app.target_sign_in_page.click_sign_in_button()


@when('Click on sidenav signin btn')
def click_the_sidenav_signin(context):
    context.app.target_sign_in_page.click_sidenav_sign_in()


@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.target_sign_in_page.get_current_window()
    print('Original Window(Sign in )',context.original_window)


@when('Click on Target terms and conditions link')
def click_on_target_terms_and_conditions_link(context):
    context.app.target_sign_in_page.click_terms_link()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.app.target_sign_in_page.switch_to_new_window()
    print('after switch terms window id ',context.app.target_sign_in_page.get_current_window())


@then('Verify Terms and Conditions page is opened')
def verify_tc_opened(context):
    context.app.target_sign_in_page.verify_terms_condition_opened()


@then('User can close new window and switch back to original')
def close_new_window(context):
    context.app.target_sign_in_page.close()
    sleep(4)

def switch_to_original_window(context):
    context.app.target_sign_in_page.switch_to_window_by_id(context.original_window)
    #print('Original Window(Sign in)',context.app.target_sign_in_page.switch_to_window_by_id(context.original_window))
    sleep(2)