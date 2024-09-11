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


  Scenario: User can search for a product
    # Enter steps here
   Given Open target main page
   When  Search for a product
   #When  Search for a product  #you can use 'And' keyword instead of 'When' in this line ,"And ' is duplication of word in the above line ,it mean the same
    And Search for product222
   Then  Verify that correct search result show
   #Then  Verify that correct search result show #you can use 'And' keyword instead of 'Then' in this line ,it mean the same
   #Then  Verify that correct search result show     #you can use 'And' keyword instead of 'Then' in this line ,it mean the same