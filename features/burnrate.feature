# Created by philip at 2/25/18
Feature: Calculate burn rate for each month for which we have data

  I'm tired of not knowing how much we're spending!

  Scenario: From inputs in conf.yaml, calculate burn rate for relevant months

    Given all input files are in the right place
    #Moved to a unit test.
    And we know the formats

    #Too implementation specific.
    #It also seems to dislike my use of parenthesis. Maybe re's work differently than expected?
    When I run the run function

    Then some output should appear somewhere--I don't care where--with the correct amount spent for each month.

  Scenario: Code base is solid at the unit-test level

    Then Unit tests pass
