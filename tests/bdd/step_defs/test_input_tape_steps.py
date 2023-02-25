import pytest
from pytest_bdd import scenarios, given, when, then, parsers

from calc.lex import Reader

scenarios('../features/input-tape.feature')

# Given Steps

@given('an empty input tape')
def an_empty_input_tape(world):
    world.input_tape = Reader()

@given(parsers.parse('an input tape with the string "{expression}"'))
def an_input_tape_with_the_expression(world, expression: str):
    world.input_tape = Reader(expression)


@given(parsers.parse('the tape head is at position {position:d}'))
def the_tape_head_is_at_position(world, position: int):
    world.input_tape._head = position


# When Steps

@when("I create a new input tape")
def i_create_a_new_input_tape(world):
    try:
        world.input_tape = Reader()
    except Exception as err:
        world.errors.append(err)

@when(parsers.parse('I create a new input tape with the string "{expression}"'))
def i_create_a_new_input_tape_with_the_expression(world, expression: str):
    try:
        world.input_tape = Reader(expression)
    except Exception as err:
        world.errors.append(err)

@when('I peek at the next character')
def i_peak_at_the_next_character(world):
    try:
        world.next_character = world.input_tape.peek()
    except Exception as err:
        world.errors.append(err)

@when('I determine if the tape is at the beginning')
def i_determine_if_the_tape_is_at_the_beginning(world):
    try:
        world.result = world.input_tape.bof()
    except Exception as err:
        world.errors.append(err)

@when('I determine if the tape is at the end')
def i_determine_if_the_tape_is_at_the_end(world):
    try:
        world.result = world.input_tape.eof()
    except Exception as err:
        world.errors.append(err)

@when('I read the next character')
def i_read_the_next_character(world):
    try:
        world.next_character = world.input_tape.read()
    except Exception as err:
        world.errors.append(err)

@when('I retract the tape head')
def i_retract_the_tape_head(world):
    try:
        world.input_tape.retract()
    except Exception as err:
        world.errors.append(err)

@when(parsers.parse('I retract the tape head {count:d} times'))
def i_retract_the_tape_head_count_times(world, count: int):
    try:
        world.input_tape.retract(count)
    except Exception as err:
        world.errors.append(err)

# Then Steps

@then("the tape should be empty")
def the_tape_should_be_empty(world):
    assert world.input_tape.is_empty()

@then(parsers.parse("the tape should have a size of {expected_size:d}"))
def the_tape_should_have_a_size_of(world, expected_size: int):
    assert world.input_tape.size == expected_size

@then(parsers.parse('the tape should contain "{expected_string}"'))
def the_tape_should_contain(world, expected_string: str):
    assert str(world.input_tape) == expected_string

@then(parsers.parse('the next character should be "{expected_character}"'))
def the_next_character_should_be(world, expected_character: str):
    assert world.next_character == expected_character

@then(parsers.parse('the tape head should be at position {expected_position:d}'))
def the_position_should_be(world, expected_position: int):
    assert world.input_tape.head == expected_position

@then('the result should be true')
def the_result_should_be_true(world):
    assert world.result

@then('the result should be false')
def the_result_should_be_false(world):
    assert not world.result
