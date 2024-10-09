from  selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

# @given('Open target main page')
# def open_main(context):
#     context.driver.get("https://www.target.com/")
# give 2 lines after this to start with when
sleep(5)

#lesson 6 to use page object , comment above given


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

#  # this following will showing the concept of parameter 09/11/24 we made dynamic
@when('Search for {item}')
def search_product(context,item):
    print(item)
    # Search filed =>items include both cpffee and tea
    context.driver.find_element(By.ID, 'search').send_keys(item)
    # Search button=> click
    # command type on console $x("//button[@data-test='@web/Search/SearchButton']")
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(5)


@then('Verify that correct search result shown for {product}')
def verify_result1(context,product):
    # Verification  $x("//div[@data-test='resultsHeading']")
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    #expected_result = product
    assert product in actual_result, f'Expected {product} but got {actual_result}'

#one way
@then('Verify header has 6 links')
def verify_header_link(context):
    links=context.driver.find_elements(By.CSS_SELECTOR,"[data-test*='@web/GlobalHeader/UtilityHeader']")
    print(links)
    len(links)
    assert len(links)==6,f'Expected 6 links but got {len(links)}'




#another way by using variable
## used the above then using variable so commented the above
# when run it give error "Assertion Failed: Expected 6 links but got 6" becoz it take expected link as string
# and len(links) return value as number  ,how to compare them
@then('Verify header has {expected_links} links')
def verify_header_link(context,expected_links):
    #take expected_link as string i.e expected_link='6'
    #convert it to integer
    expected_links=int(expected_links) #'6'=> 6
    links=context.driver.find_elements(By.CSS_SELECTOR,"[data-test*='@web/GlobalHeader/UtilityHeader']")
    print(links)
    len(links)
    #take len(links) as integer len(links)=6
    #comparing 6=='6'
    assert len(links)==expected_links,f'Expected {expected_links} links but got {len(links)}'
    #or you can convert here also assert len(links)==int(expected_links),f'Expected {expected_links} links but got {len(links)}'


@then('Verify header is shown')
def verify_header(context):
    #command used $$("[class*='styles_utilityHeaderContainer']")
    context.driver.find_element(By.CSS_SELECTOR,"[class*='styles_utilityHeaderContainer']")
# the below will run and pass
# @then('Verify header has links')
# def verify_header_link_shown(context):
#     context.driver.find_elements(By.CSS_SELECTOR,"[data-test*='@web/GlobalHeader/UtilityHeader']")

#suppose we want above then to fail, we give some randon value in Css selector but when you run .it
#will not fail becoz find_elements function never fails ,either it returns list of elements or empty
#list[] if find nothing

@then('Verify header has links')
def verify_header_link_shown(context):
    link=context.driver.find_elements(By.CSS_SELECTOR,"[data-test*='href_qwee']")
    print(link)
    #below staement will make this test fail if nothing matches so be careful to add this stament or count links so you know that
    #find elements witll give you correct result, add below command to see test fails
    #assert len(link)>0

#lesson 6 part1
@given('Open target main page')
def open_main_page(context):
    context.app.main_page.open_page()
    sleep(5)


@when('Search the product {item}')
def search_product(context,item):
    print(item)
    context.app.header.search_product(item)



@then('Verify that the correct search result shown for {product}')
def verify_result1(context,product):
    context.app.search_result_page.verify_result(product)
    sleep(5)



#lesson 6 part2
@when('Click on the cart icon')
def click_cart(context):
    context.app.header.click_cart_icon()
    sleep(5)


@then('Verify that "Your cart is empty" message is shown')
def verify_cart_empty(context):
    # verification $x("//div[@data-test='boxEmptyMsg']")
    # actual_result = context.driver.find_element(By.XPATH,"//div[@data-test='boxEmptyMsg']" ).text
    # expected_result = 'Your cart is empty'
    # assert expected_result == actual_result, f'Expected {expected_result} but got {actual_result}'
      context.app.cart_page.verify_cart_empty_message()
      sleep(6)

 #lesson7
@then('Verify product {product} in URL')
def verify_result_url(context,product):
    context.app.search_result_page.verify_result_url(product)

#lesson 7 Homework
#part 1
@when('Click on the Sign In')
def click_sign_in(context):
    #$$("[class*='kwbrXj h-margin-r']")
    #context.driver.find_element(By.CSS_SELECTOR,"[class*='kwbrXj h-margin-r']" ).click()
     context.app.header.click_signin()


@when('Click Sign In from right navigation menu')
def click_navigation_menu_sign_in(context):
    #$$("#listaccountNav-signIn")
    #$$("[data-test='accountNav-signIn']")
    #context.driver.find_element(By.CSS_SELECTOR,"#listaccountNav-signIn").click()
    context.app.header.click_sidenav_signin()

@then('Verify that Sign In form opened')
def verify_sign_in(context):
   # context.driver.get("https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_signin")
   context.app.sign_in_page.signin_form()


#lesson 7 homework
# part2
@when('Click on the Add to Cart Button')
def click_add_to_cart(context):
    #$$("[id*='addToCartButton']")
    sleep(5)
    context.driver.execute_script("window.scrollTo(0, 1000);")
    #USED EXPLICIT WAIT
    # context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id*='addToCartButton']")),
    #                            message='add to cart button not clickable').click()
    # context.driver.find_element(By.CSS_SELECTOR, "[id*='addToCartButton']").click()
    sleep(3)
    context.app.cart_page.click_add_to_cart_btn()


@when('Store the product name')
def store_product_name(context):
    # context.product_name = context.driver.find_element(By.CSS_SELECTOR, "[data-test='content-wrapper'] h4").text
    context.app.product_page.store_the_product()
    #print(f'Product stored: {context.product_name}')
    sleep(5)


@when('Confirm the Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    #context.driver.find_element(By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']").click()
    context.app.cart_page.side_nav_click_add_to_cart_btn()

    sleep(4)

@when('Open the cart page')
def open_cart(context):
    #context.driver.get('https://www.target.com/cart')
    context.app.cart_page.open_cart()


@then('Verify that the cart has that product')
def verify_cart(context):
    #actual_name= context.driver.find_element(By.CSS_SELECTOR,"[data-test='cart-summary-total']")
    #actual_name = context.driver.find_element(By.CSS_SELECTOR,"[data-test='cartItem-title']").text
    # actual_name = context.driver.find_element(*CART_ITEM_TITLE).text
    # print(f'Actual product in cart name:{actual_name}')
    # assert context.product_name in actual_name,f"Expected{context.product_name} but got {actual_name}"
    context.app.product_page.verify_product()
    sleep(5)