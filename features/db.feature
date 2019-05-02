Feature: Get users from db and compare with list on page

    Scenario: Get users from db, webpage and compare them

        Given I get users from database
        And I get userlist from webpage
        Then I compare userlists