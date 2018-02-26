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
    #This seems like not the right place to set up my unit tests. Maybe my
    # scenario thinking should be reengineered, and then this unit testing
    # could be put somewhere more appropriate with actual asserts and stuff.
    """
    :type context: behave.runner.Context
    """
    test_app = BudgetApp()
    result = test_app.parse_gain_loss("(1234.45)")
    if result != -1234.45:
        raise Exception("Parsing method parse_gain_loss doesn't work. ")
    result = test_app.parse_gain_loss('"999,888.75"')
    if result != 999888.75:
        raise Exception("Parsing method parse_gain_loss doesn't work for gains with quotes. ")


@when("I run the main\(\) function")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.scenario.skip()
    pass


@then("some output should appear somewhere \(I don't care where\) with the correct amount spent for each month\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.scenario.skip()
    pass