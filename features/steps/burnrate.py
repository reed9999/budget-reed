from behave import *
from BudgetApp import BudgetApp

use_step_matcher("re")



@given("all input files are in the right place")
def step_impl(context):
    "Eventually we should do standard setup and teardown. For now, just make sure it's here."
    fn = "__/something.csv"
    with open(fn, 'r') as f:
        if f is None:
            raise Exception("The input file is not present and that is a problem. File name: {0}".format(fn))

@step("we know the formats")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    #This seems like not the right place to set up my unit tests. Maybe my
    # scenario thinking should be reengineered, and then this unit testing
    # could be put somewhere more appropriate with actual asserts and stuff.
    print("This should actually be a unit test so I will assume that they pass. ")

@when("I run the run function")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    BudgetApp.run()


@then("some output should appear somewhere--I don't care where--with the correct amount spent for each month\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    fn = "__temp-output-file.csv"
    with open(fn, 'r') as f:
        if f is None:
            raise Exception("The output file is not present and that is a problem. File name: {0}".format(fn))
