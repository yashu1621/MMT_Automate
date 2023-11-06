Feature: User Login Functionality
    Background: the user is navigating to the login page of MMT
        Given User is on the MMT website   
   
    Scenario: User logs in with invalid credentials
        When the user enters invalid username and password       

    Scenario: User logs in with valid credentials
        When the user enters valid username and password
    

  