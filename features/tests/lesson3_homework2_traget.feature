# Created by parve at 9/10/2024
Feature: User can see empty cart message
#part1
  Scenario: User can see empty cart message
    Given Open target main page
    When  Click on cart icon
    Then  Verify "Your cart is empty" message is shown

#part2
  Scenario: Logged out user can navigate to Sign In page
    Given Open target main page
    When  Click on Sign In
    When  from right side navigation menu , click Sign In
    Then  Verify Sign In form opened