# Tests for all methods page.

Feature: Methods catalogue tests

    Scenario: Title check
        Given I'm an sml portal user
        When I am on the methods catalogue page
        Then The title of the page is "Method: All Methods"