# Created by parve at 10/13/2024
Feature:Test for Target sign in page

 #Homework 8 part 1
 # 1. Create a window handling test case from the class and
 # verify that a user can open Terms and Conditions from sign in page (https://www.target.com/login)

Scenario: User can open and close Terms and Conditions from sign in page
 Given Open sign in page
 When  Click on sign in icon
 When  Click on sidenav signin btn
 When  Store original window
 And   Click on Target terms and conditions link
 And   Switch to the newly opened window
 Then  Verify Terms and Conditions page is opened
 And   User can close new window and switch back to original
