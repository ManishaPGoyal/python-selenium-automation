from  selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



#part 1
# @given('Open target main page')
# def open_main(context):
#     context.driver.get("https://www.target.com/")
# sleep(5)

@when('Click on cart icon')
def click_cart(context):
    #$$("[data-test='@web/CartIcon']")
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartIcon']").click()
sleep(5)

@then('Verify "Your cart is empty" message is shown')
def verify_cart_empty(context):
     # verification $x("//div[@data-test='boxEmptyMsg']")
    actual_result = context.driver.find_element(By.XPATH,"//div[@data-test='boxEmptyMsg']" ).text
    expected_result = 'Your cart is empty'
    assert expected_result == actual_result, f'Expected {expected_result} but got {actual_result}'

#part2
@when('Click on Sign In')
def click_sign_in(context):
    #$$("[class*='kwbrXj h-margin-r']")
    context.driver.find_element(By.CSS_SELECTOR,"[class*='kwbrXj h-margin-r']" ).click()
sleep(10)


@when('from right side navigation menu , click Sign In')
def click_navigation_menu_sign_in(context):
    #$$("#listaccountNav-signIn")
    context.driver.find_element(By.CSS_SELECTOR,"#listaccountNav-signIn").click()
sleep(10)

@then('Verify Sign In form opened')
def verify_sign_in(context):
    context.driver.get("https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_signin")
sleep(10)