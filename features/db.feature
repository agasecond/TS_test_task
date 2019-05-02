Feature: Get users from db and compare with list on page

    Scenario: Get users from db

        Given I get users from database
        And I get userlist from webpage
        Then I compare userlists