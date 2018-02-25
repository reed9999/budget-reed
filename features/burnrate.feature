# Created by philip at 2/25/18
Feature: Calculate burn rate for each month for which we have data

  I'm tired of not knowing how much we're spending!

  Scenario: From inputs in conf.yaml, calculate burn rate for relevant months

    Given all input files are in the right place
    And we know the formats

    When I run the main() function

    Then some output should appear somewhere (I don't care where) with the correct amount spent for each month.

