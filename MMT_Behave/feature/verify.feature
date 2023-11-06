Feature: Verify logo,url,title

    Scenario: User launches the application
        Given User is on the MMT website
        Then User validates the URL is "https://www.makemytrip.com/"
        And User validates the presence of the MMT logo
        And the user validates the title is present
        And the user validates the Login button is present
   