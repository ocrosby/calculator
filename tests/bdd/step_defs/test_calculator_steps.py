from pytest_bdd import scenarios, given, when, then, parsers

from calc.engine import Computer

scenarios('../features/calculator.feature')

# Given Steps

@given(parsers.parse('I have entered the expression "{expression}"'))
def expression_entry(world, expression: str):
    world.expression = expression


# When Steps

@when("I evaluate the expression")
def evaluate(world):
    try:
        world.result = world.computer.evaluate(world.expression)
    except Exception as err:
        world.errors.append(err)


# Then Steps

@then(parsers.parse('the result should be "{expected_value}"'))
def compare_results(world, expected_value: str):
    assert world.result == expected_value

