Feature: One-way Flight with lowest fare

    Scenario: User books flight with cheapest price and time
        
        Given User is on the MMT website 
        When the user selects the one-way radio option
        And the user selects "Delhi" as the from city
        And the user selects "Bangalore" as the to city
        And the user selects the departure date
        And the user clicks on the Search button
        And the user selects flights with lowest price and time
        Then the user Validates the flight name and Fare Summary