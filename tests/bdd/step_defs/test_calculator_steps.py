import pytest
from pytest_bdd import scenarios, given, when, then, parsers

from calc import app

scenarios("../features/calculator.feature")

# Given Steps


@given(parsers.parse('I have entered the expression "{expression}"'))
def expression_entry(world, expression: str):
    world.expression = expression


# When Steps


@when("I evaluate the expression")
def evaluate(world, application):
    try:
        world.result = application.evaluate(world.expression)
    except Exception as err:
        world.errors.append(err)


# Then Steps


@then(parsers.parse('the result should be "{expected_value}"'))
def compare_results(world, expected_value: str):
    assert str(world.result) == expected_value


@then(
    parsers.parse("the result should be within {epsilon} of {expected_value}")
)
def compare_results_almost(world, epsilon: str, expected_value: str):
    epsilon = float(epsilon)
    expected_value = float(expected_value)

    assert pytest.approx(world.result, epsilon) == expected_value
