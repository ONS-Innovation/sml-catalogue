# Tests for selective editing page.

Feature: Selective editing tests

    Scenario: Title check
        Given I'm an sml portal user
        When I am on the selective editing page
        Then The title of the page is "Method: Selective Editing"