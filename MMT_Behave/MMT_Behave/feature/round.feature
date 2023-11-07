Feature: Two-way Flight Booking

    Scenario: User books a two-way flight from Bangalore to London
        
        Given User is on the MMT website 
        When the user selects the round radio option
        And the user selects "Bangalore" as the from city
        And the user selects "London" as the to city
        And the user selects the departure date
        And the user selects the arrival date
        And the user selects passenger details
        And the user clicks on the Search button
        And the user selects Britsih Airways
        And the user clicks on the flight Details
        Then the user clicks on the view prices button