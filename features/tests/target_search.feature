# Created by parve at 9/9/2024
  # Enter feature name here
Feature: Tests for Target Search functionality
  # Enter feature description here
  # Enter scenario name here
  Scenario: User can search for a product
    # Enter steps here
   Given Open target main page
   When  Search for a product
   Then  Verify that correct search result show

# we can make any number of scenario
  Scenario: User can search for a product
    # Enter steps here
   Given Open target main page
   When  Search for a product
   #When  Search for a product  #you can use 'And' keyword instead of 'When' in this line ,"And ' is duplication of word in the above line ,it mean the same
    And Search for product222
   Then  Verify that correct search result show
   #Then  Verify that correct search result show #you can use 'And' keyword instead of 'Then' in this line ,it mean the same
   #Then  Verify that correct search result show     #you can use 'And' keyword instead of 'Then' in this line ,it mean the same
  #lesson 4
  # 09/11/24 in below we are using concept of variables and parameter , the scenario is same except the name of search item
  # in step file we use {parameter} to write one step for both of them not different step with coffee and tea in send keys

 Scenario: User can search for coffee
    # Enter steps here
   Given Open target main page
   When  Search for coffee
   Then  Verify that correct search result shown for coffee

 Scenario: User can search for christmas light
    # Enter steps here
   Given Open target main page
   When  Search for chirstmas light
   Then  Verify that correct search result shown for chirstmas light

   Scenario Outline: User can search product
    Given Open target main page
    When  Search for <search_word>
    Then  Verify that correct search result shown for <search_result>
    Examples:
    |search_word |search_result |
    |coffee      |coffee        |
    |tea         |tea           |
    |sugar       |sugar         |
    |pencil      |pencil        |
    |marker      |marker        |
#or if search word and search result are same , you can use below also

 Scenario Outline: User can search product
    Given Open target main page
    When  Search for <search_word>
    Then  Verify that correct search result shown for <search_result>
    Examples:
    |search_word |search_result |
    |coffee      |coffee        |
    |tea         |tea           |
    |sugar       |sugar         |
    |pencil      |pencil        |
    |marker      |marker        |


Scenario: Verify header is shown
  Given Open target main page
  Then Verify header is shown
  And  Verify header has links

##check find_elements functions
 Scenario: Verify header has correct amount of links
  Given Open target main page
  Then Verify header has 6 links

# another way to do this using variable, everything same here , we changing then in step file
# Scenario: Verify header has correct amount of links
#  Given Open target main page
#  Then Verify header has 6 links

 # we just want to verify header is shown , not wnat to count the link

  # LESSON 6 HOMEWORK
 #PART1
Scenario: User can search for tea
    # Enter steps here
   Given Open target main page
   When  Search the product tea
   Then  Verify that the correct search result shown for tea
   #lesson 7
   Then  Verify product tea in URL

#PART2
Scenario: User can see empty cart message
    Given Open target main page
    When  Click on the cart icon
    Then  Verify that "Your cart is empty" message is shown


#Lesson 7 homework
#part 1
#1. Update the test case to verify that logged out user can access Sign In, add Page Object pattern:
#Open target.com  # main page
#Click Sign In  # header
#From right side navigation menu, click Sign In # header or create PO for menu
#Verify Sign In form opened # sign in page

Scenario: Logged out user can navigate to Sign In page
    Given Open target main page
    When  Click on the Sign In
    When  Click Sign In from right navigation menu
    Then  Verify that Sign In form opened


#part 2
#2. Update “Add a product to cart” scenario, add Page Object pattern.

Scenario: User can add Target product in cart and check it's in the cart
    # Enter steps here
   Given Open target main page
   #When  Search the Target product to Add to cart
   When Search the product mug
   And Click on the Add to Cart Button
   And Store the product name
   And Confirm the Add to Cart button from side navigation
   And Open the cart page
   Then Verify that the cart has that product


#lesson 9 practice ActionChains
Scenario: User can see favorites tooltip for search results
  Given  Open target main page
  When   Search for tea
  And    Hover favorites icon
  #Then   favorites tooltip is shown

#getting error

#Step failed:  <when "Hover favorites icon">
#
#Traceback (most recent call last):
#  File "C:\Users\parve\OneDrive\Desktop\python-selenium-automation\venv\Lib\site-packages\behave\model.py", line 1329, in run
#    match.run(runner.context)
#  File "C:\Users\parve\OneDrive\Desktop\python-selenium-automation\venv\Lib\site-packages\behave\matchers.py", line 98, in run
#    self.func(context, *args, **kwargs)
#  File "features\steps\target_steps.py", line 232, in hover_favorites
#    context.app.search_result_page.hover_favorites()
#  File "C:\Users\parve\OneDrive\Desktop\python-selenium-automation\pages\search_result_page.py", line 41, in hover_favorites
#    actions.move_to_element(heart_icon)
#  File "C:\Users\parve\OneDrive\Desktop\python-selenium-automation\venv\Lib\site-packages\selenium\webdriver\common\action_chains.py", line 253, in move_to_element
#    self.w3c_actions.pointer_action.move_to(to_element)
#  File "C:\Users\parve\OneDrive\Desktop\python-selenium-automation\venv\Lib\site-packages\selenium\webdriver\common\actions\pointer_actions.py", line 88, in move_to
#    raise AttributeError("move_to requires a WebElement")
#AttributeError: move_to requires a WebElement