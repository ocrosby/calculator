from pytest_bdd import scenario, given, when, then, parsers

# Given Steps

@given(parsers.parse('I have entered "{input_value:s}" into the calculator'))
def enter_input(world, input_value: str):
    world.input_value = input_value


# When Steps

@when("I press add")
def add(world):
    try:
        raise NotImplementedError(u'STEP: When I press evaluate')
    except Exception as err:
        world.errors.append(err)


@when("I press subtract")
def subtract(world):
    try:
        raise NotImplementedError(u'STEP: When I press evaluate')
    except Exception as err:
        world.errors.append(err)


@when("I press multiply")
def multiply(world):
    try:
        raise NotImplementedError(u'STEP: When I press evaluate')
    except Exception as err:
        world.errors.append(err)


@when("I press divide")
def divide(world):
    try:
        raise NotImplementedError(u'STEP: When I press evaluate')
    except Exception as err:
        world.errors.append(err)


@when("I press sine")
def sine(world):
    try:
        raise NotImplementedError(u'STEP: When I press evaluate')
    except Exception as err:
        world.errors.append(err)


@when("I press cosine")
def cosine(world):
    try:
        raise NotImplementedError(u'STEP: When I press evaluate')
    except Exception as err:
        world.errors.append(err)


@when("I press tangent")
def tangent(world):
    try:
        raise NotImplementedError(u'STEP: When I press evaluate')
    except Exception as err:
        world.errors.append(err)


@when("I press log")
def log(world):
    try:
        raise NotImplementedError(u'STEP: When I press evaluate')
    except Exception as err:
        world.errors.append(err)


@when("I press evaluate")
def evaluate(world):
    try:
        raise NotImplementedError(u'STEP: When I press evaluate')
    except Exception as err:
        world.errors.append(err)


# Then Steps

@then(parsers.parse('the result should be "{expected_value:s}" on the screen'))
def screen_result_should_be(world, expected_value: str):
    assert world.result == expected_value

