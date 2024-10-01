from  selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


#$$("div[aria-label='Carousel'] li img")
#("div[aria-label='Carousel'] li img")
#COLOR_OPTIONS=(By.CSS_SELECTOR,"div[aria-label='Carousel'] li img") # this commmand not working
#COLOR_OPTIONS=(By.CSS_SELECTOR,"[class*='gDiaXS'] img" ) #command giving size
#COLOR_OPTIONS = (By.CSS_SELECTOR, " [class*='ButtonWrapper'] img")
COLOR_OPTIONS = (By.CSS_SELECTOR, "div[aria-label='Carousel'] li img")
#COLOR_OPTIONS=(By.CSS_SELECTOR,"[class*='gDiaXS'] ul li")
#COLOR_OPTIONS=(By.CSS_SELECTOR,"[data-test='@web/VariationComponent'] div") #
#$$("[data-test='@web/VariationComponent'] div")
#$$("div[data-test='@web/VariationComponent']")
#$$("[class*='gDiaXS'] li img")
#SELECTED_COLOR=(By.CSS_SELECTOR,"[class*='gDiaXS'] li")
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent']:nth-child(3) div")
#SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='Cell']")
#SELECTED_COLOR=(By.CSS_SELECTOR,"[data-test='@web/VariationComponent'] div") #running
#SElECTED_COLOR=(By.CSS_SELECTOR,"div[data-test='@web/VariationComponent']")
#SElECTED_COLOR=(By.CSS_SELECTOR,"[class*='gDiaXS'] li img")
SELECTED_COLOR1 = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")

#part1
@given('Open the target product {product_id} page')
def open_main_page(context,product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(15)

@then('Verify user can click colors tab')
def click_and_verify_color_tab(context):
    expected_colors = ['grey','dark khaki','navy/tan','stone/grey','white/gum','white/navy/red','white/sand/tan','black/gum - Out of Stock']
    actual_colors = []
    colors=context.driver.find_elements(*COLOR_OPTIONS)
    print('colors',colors)
    for color in colors:
        print('color in for loop',color)
        color.click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        print('Curent color text',selected_color)
        selected_color = selected_color.split('\n')[1]

        actual_colors.append(selected_color)
        print('actual_color_list',actual_colors)

    assert expected_colors == actual_colors,f'Expected{expected_colors} did not match actual{actual_colors}'

@then('Verify user can click the colors tab')
def click_and_verify_color_tab(context):
    expected_colors = ['Blue Tint', 'Denim Blue', 'Marine', 'Raven']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    print(colors)

    for color in colors:
        print(color)
        color.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR1).text
        print('Current color text', selected_color)

        selected_color = selected_color.split('\n')[1]
        actual_colors.append(selected_color)
        print('actual_colors list: ', actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'