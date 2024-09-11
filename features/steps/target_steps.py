from  selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




# @given('Open target main page')
# def open_main(context):
#     context.driver.get("https://www.target.com/")
# give 2 lines after this to start with when
sleep(5)
@when('Search for a product')
def search_product(context):
    # Search filed =>tea
    context.driver.find_element(By.ID, 'search').send_keys('tea')
    # Search button=> click
    # command type on console $x("//button[@data-test='@web/Search/SearchButton']")
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(5)

@when('Search for product222')
def search_product(context):
    # Search filed =>tea
    context.driver.find_element(By.ID, 'search').send_keys('tea')
    # Search button=> click
    # command type on console $x("//button[@data-test='@web/Search/SearchButton']")
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(5)

@then('Verify that correct search result show')
def verify_result(context):
    # Verification  $x("//div[@data-test='resultsHeading']")
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    expected_result = 'tea'
    assert expected_result in actual_result, f'Expected {expected_result} but got {actual_result}'
    # print('Test case passed') we dont need this command as behave will handle this