from  selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open help page for Returns')
def click_cart(context):
    context.app.help_page.open_help_returns()


@when('Select Help topic promotions & coupons')
def select_topic_promotions(context):
    context.app.help_page.select_topic()


@then('Verify help Returns page opened')
def verify_help_returns_page(context):
    context.app.help_page.verify_returns_opened()


@then('Verify help Current promotions page opened')
def verify_current_promotions_page(context):
    context.app.help_page.verift_promotions_opened()