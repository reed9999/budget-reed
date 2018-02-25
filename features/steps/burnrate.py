from behave import *

use_step_matcher("re")



@given("all input files are in the right place")
def step_impl(context):
    print("Hello world put_input_files_in_right_place\n")
    context.scenario.skip()

@step("we know the formats")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print("Hello world we know the formats\n")
    context.scenario.skip()


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