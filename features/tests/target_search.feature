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


    Scenario: User can search for tea
    # Enter steps here
   Given Open target main page
   When  Search for tea
   Then  Verify that correct search result shown for tea


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
