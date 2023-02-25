import pytest

from pytest_bdd import parsers, given, when, then, scenarios


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')

def pytest_bdd_apply_tag(tag, function):
    if tag == 'todo':
        marker = pytest.mark.skip(reason="Not implemented yet")
        marker(function)
        return True
    elif tag == 'skip':
        marker = pytest.mark.skip(reason="Skipped")
        marker(function)
        return True
    elif tag == 'ignore':
        marker = pytest.mark.skip(reason="Ignored")
        marker(function)
        return True
    else:
        # Fall back to the default behavior of pytest-bdd
        return None

class World:
    errors: list
    expression: str
    result: str

    def __init__(self):
        self.errors = []
        self.input_value = ''
        self.result = ''

@pytest.fixture(scope='function')
def world():
    return World()


@then('there should be no errors')
def no_errors(world):
    if len(world.errors) > 0:
        for error in world.errors:
            print(error)

    assert len(world.errors) == 0

@then('there should be an error')
def error(world):
    assert len(world.errors) > 0


@then(parsers.parse('I should see the error "{expected_value}"'))
def error_message(world, expected_value: str):
    assert len(world.errors) > 0

    found = False
    for error in world.errors:
        if expected_value in str(error):
            found = True
            break

    assert found
