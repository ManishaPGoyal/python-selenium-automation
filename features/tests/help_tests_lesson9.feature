# Created by parve at 10/16/2024
#lesson 9 dropdown practice
Feature: Tests for help page

  Scenario: User can select help topic promotions and coupons
    Given Open help page for Returns
    Then Verify help Returns page opened
    When Select Help topic promotions & coupons
    Then Verify help Current promotions page opened