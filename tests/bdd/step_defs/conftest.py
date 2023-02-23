import pytest

from pytest_bdd import parsers, given, when, then, scenarios

from calc.engine import Computer

def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')

class World:
    errors: list
    expression: str
    result: str
    computer: Computer

    def __init__(self):
        self.errors = []
        self.input_value = ''
        self.result = ''
        self.computer = Computer()

@pytest.fixture(scope='function')
def world():
    return World()


@then('there should be no errors')
def no_errors(world):
    if len(world.errors) > 0:
        for error in world.errors:
            print(error)

    assert len(world.errors) == 0
