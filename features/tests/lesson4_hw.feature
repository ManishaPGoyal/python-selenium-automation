# Created by parve at 9/14/2024
# 1. Update Target product search test case and add Behave variables.
#2. Create a test case that will open the Target Circle page https://www.target.com/circle,
# and verify there are 10 benefit cells:
#3. Create a test case to add any Target’s product into the cart, and
# make sure it’s there (check that your cart has individual cart items OR the total price, up to you!)

#4* [Not required]. Create a test case to verify Target Help UI:
#Open https://help.target.com/help
#Then Verify these UI elements are present of the page (feel free to just use find_element / find_elements ) ⇒

Feature: Tests for Target Search functionality using Behave variable

##part 1
  Scenario: User can search the Target for marker
    # Enter steps here
   Given Open the target main page
   When  Search for the marker
   Then  Verify that correct search result display for marker


Scenario: User can search the Target site for mug
    # Enter steps here
   Given Open the target main page
   When  Search for the mug
   Then  Verify that correct search result display for mug


Scenario: User can search the Target for printer
    # Enter steps here
   Given Open the target main page
   When  Search for the printer
   Then  Verify that correct search result display for printer

  Scenario: User can search the Target for lettuce
    # Enter steps here
   Given Open the target main page
   When  Search for the lettuce
   Then  Verify that correct search result display for lettuce

#part 2
Scenario: Verify Target circle page has correct amount of benefits cells
    # Enter steps here
   Given Open the target circle page
   Then  Verify the correct amount of benefits cells

#part 3

Scenario: User can add Target product in cart and check it's in cart
    # Enter steps here
   Given Open the target main page
   #When  Search the Target product to Add to cart
   When Search for the mug
   And Click on Add to Cart Button
   And Store product name
   And Confirm Add to Cart button from side navigation
   Then Verify that cart has that product

 #part 4
Scenario: Verify Target Help U
  Given Open the target help page
  Then  Verify the UI components