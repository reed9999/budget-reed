#So what's the best practice to set up an OO Python application? Turns out this
# is nontrivial to find. As in, have a wrapper .py with a main() that invokes
# an app singleton class?

#Interestingly searches with python and "application class" find tons of tkinter
# tips.
#Sometime this would be fun for GUI: https://stackoverflow.com/a/17470842/742573
from BudgetApp import BudgetApp


def main():
    """
    So this entire app is overkill. I have a few text files I want to process
    that probably calls for sed or something. I might write them to a budget
    spreadsheet, but that's a solved problem.

    The reason for the overkill is to learn Python better, and particularly
    to challenge myself to use BDD.

    :return: nothing
    """
    BudgetApp.run()


if __name__ == '__main__':
    main()





    """
    This will become my BDD
    
    Feature: Calculate burn rate for each month for which we have data
    
    I'm tired of not knowing how much we're spending!
    
    Scenario: From inputs in conf.yaml, calculate burn rate for relevant months
    
    Given that all input files are in the right place
    And that we know the formats
    
    When I run the main() function
    
    Then some output should appear somewhere (I don't care where) with the 
    correct amount spent for each month.
    
    """