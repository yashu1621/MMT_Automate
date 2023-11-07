Feature: One-way Flight 

    Scenario: User books a one-way flight from Delhi to Bangalore
        
        Given User is on the MMT website 
        When the user selects the one-way radio option
        And the user selects "Delhi" as the from city
        And the user selects "Bangalore" as the to city
        And the user selects the departure date
        And the user clicks on the Search button
        Then the user captures the flight names
