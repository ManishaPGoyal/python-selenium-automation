from behave.model import Scenario
from  selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


#part1
@given('Open the target main page')
def open_main_page(context):
    context.driver.get("https://www.target.com/")
sleep(5)

#part2
@given('Open the target circle page')
def open_main_page(context):
    context.driver.get("https://www.target.com/circle")
sleep(5)

#part4
@given('Open the target help page')
def open_target_help_page(context):
    context.driver.get("https://help.target.com/help")
sleep(5)

#part1
@when('Search for the {product}')
def search_for_product(context,product):
    #console command $x("//input[@id='search']")
    context.driver.find_element(By.ID, 'search').send_keys(product)
    # USED EXPLICIT WAIT
    context.driver.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@data-test='@web/Search/SearchButton']"))
                              ,message='search button not clickable').click()

    #context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    #sleep(5)

#part3 corrected
@when('Click on Add to Cart Button')
def click_add_to_cart(context):
    #$$("[id*='addToCartButton']")
    #USED EXPLICIT WAIT
    context.deriver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id*='addToCartButton']")),
                               message='add to cart button not clickable').click()
    #context.driver.find_element(By.CSS_SELECTOR, "[id*='addToCartButton']").click()
    #sleep(5)

@when('Store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(By.CSS_SELECTOR, "[data-test='content-wrapper'] h4").text
    print(f'Product stored: {context.product_name}')
    sleep(5)


@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']").click()
    sleep(5)


#part1
@then('Verify that correct search result display for {product}')
def verify_search_result(context,product):
    #$x("//div[@data-test='resultsHeading']")
    actual_result=context.driver.find_element(By.XPATH,"//div[@data-test='resultsHeading']").text
    #print(actual_result)
    assert product in actual_result,f'Expected result{product} but got {actual_result}'
sleep(5)


#part2
@then('Verify the correct amount of benefits cells')
def search_for_benefits(context):
    #console command $$(".cell-item-content")
    benefits_cells=context.driver.find_elements(By.CSS_SELECTOR,".cell-item-content")
    len(benefits_cells)
    print(benefits_cells)
    print(len(benefits_cells))

#part 3
# command console $$("[data-test='@web/CartIcon']")
# command for  item name $$("[aria-label*='AriZona Arnold Palmer Half & Half Iced Tea']")
#$$("[href='/p/arizona-arnold-palmer-lite-half-iced-tea-half-lemonade-128-fl-oz-jug/-/A-13388793#lnk=sametab']")
#$$("[href*='/p/arizona-arnold-palmer-lite-half-iced-tea-half-lemonade-128-fl-oz-jug/']")
#$$("[class*='fLytdP bRxnjG h-display-block h-text-bold h-text-bs'][aria-label='AriZona Arnold Palmer Lite Half Iced Tea & Half Lemonade - 128 fl oz Jug']")
#command for Add to cart button $$("#addToCartButtonOrTextIdFor85259420")
#$$("button[id='addToCartButtonOrTextIdFor13388793']")
#command for view cart button $$("[href='/cart']")
#$$("[class*='jKTcnK hhYRAp'][href='/cart']")
# cart page url https://www.target.com/cart
# cart summary box  $$("[data-test*='cart-summary']")
#cart total $$("[data-test='cart-summary-total']")

## @when('Search the Target product to Add to cart')
## def search_the_product(context):
##    context.driver.find_element(By.ID, 'search').send_keys('arizona tea')
##     context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
##    sleep(5)
##    #context.driver.find_element(By.CSS_SELECTOR,"[href='/p/arizona-arnold-palmer-lite-half-iced-tea-half-lemonade-128-fl-oz-jug/-/A-13388793#lnk=sametab']")
##    context.driver.find_element(By.CSS_SELECTOR,"[class*='fLytdP bRxnjG h-display-block h-text-bold h-text-bs'][aria-label='AriZona Arnold Palmer Lite Half Iced Tea & Half Lemonade - 128 fl oz Jug']")
##     sleep(5)
##     context.driver.find_element(By.CSS_SELECTOR, "[id*='addToCartButton']").click()
##     sleep(5)
##     context.driver.find_element(By.CSS_SELECTOR,"[class*='hYRAp'][href='/cart']").click()
##     sleep(5)
##    #context.driver.get("https://www.target.com/cart")
##    #sleep(5)



@then('Verify that cart has that product')
def verify_cart(context):
    #actual_name= context.driver.find_element(By.CSS_SELECTOR,"[data-test='cart-summary-total']")
    actual_name = context.driver.find_element(By.CSS_SELECTOR, "[data-test='cartItem-title']").text
    print(f'Actual product in cart name:{actual_name}')
    assert context.product_name in actual_name,f"Expected{context.product_name} but got {actual_name}"
    sleep(5)


#part4
#for target help $$("h2[class='custom-h2']")
#for search box $$(".search-input")
#for search button $$(".btn-sm.search-btn")
#for 6 box $$("[class*='boxSmall txtAC']")
# for 2 boxes $$("[class*='boxSmallr txtAC bigbox2']")
#for browse all pages $$(".home-container#divID1")
@then('Verify the UI components')
def verify_ui(context):
    context.driver.find_element(By.CSS_SELECTOR,"h2[class='custom-h2']")
    context.driver.find_element(By.CSS_SELECTOR,".search-input")
    context.driver.find_element(By.CSS_SELECTOR,".btn-sm.search-btn")
    link=context.driver.find_elements(By.CSS_SELECTOR,"[class*='boxSmall txtAC']")
    print(link)
    print(len(link))
    link2=context.driver.find_elements(By.CSS_SELECTOR,"[class*='boxSmallr txtAC bigbox2']")
    print(link2)
    print(len(link2))
    context.driver.find_element(By.CSS_SELECTOR,".home-container#divID1")
