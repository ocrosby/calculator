from pytest_bdd import scenario, given, when, then, parsers

from calc.lolo import Set, Char

SET_FEATURE = '../features/lolo/set.feature'
CHAR_FEATURE = '../features/lolo/char.feature'

@scenario(SET_FEATURE, 'Check if the character 1 belongs to the set of digits')
def test_check_if_the_character_1_belongs_to_the_set_of_digits():
    pass

@scenario(SET_FEATURE, 'Check if the character a belongs to the set of digits')
def test_check_if_the_character_a_belongs_to_the_set_of_digits():
    pass

@scenario(SET_FEATURE, 'Check if the character ( belongs to the compliment of the set of digits')
def test_check_if_the_character_left_paren_does_not_belong_to_the_set_of_digits():
    pass

@scenario(CHAR_FEATURE, 'Check if the Char scan matches a single arbitrary character 1')
def test_char_scan_arbitrary_matches_one():
    pass

@scenario(CHAR_FEATURE, 'Check if the Char scan matches a single arbitrary character [')
def test_char_scan_arbitrary_matches_left_bracket():
    pass

@scenario(CHAR_FEATURE, 'Check if the Char scan matching P matches a single specific character P')
def test_char_scan_specific_matches_p():
    pass

@scenario(CHAR_FEATURE, 'Check if the Char scan matching P matches a single specific character Q')
def test_char_scan_specific_matches_q():
    pass

@given("a set of digits")
def a_set_of_digits(world):
    world.scan = Set('0123456789')

@given('a Char matching anything')
def a_char_matching_anything(world):
    world.scan = Char('', False)

@given(parsers.parse('a Char matching the character {char}'))
def a_char_matching_the_character(world, char: str):
    world.scan = Char(char, True)

@given(parsers.parse('a Char matching the character {char}'))
def a_char_matching_the_character(world, char: str):
    world.scan = Char(char, True)

@given('inside is set to False on the scan')
def inside_is_set_to_false_on_the_scan(world):
    world.scan.inside = False

@given('inside is set to True on the scan')
def inside_is_set_to_true_on_the_scan(world):
    world.scan.inside = True

@when(parsers.parse('the next character is {char}'))
def the_next_character_is(world, char: str):
    try:
        world.result = world.scan.next_char(char)
    except Exception as err:
        world.errors.append(err)

@then("I should be told that it does")
def i_should_be_told_that_it_does(world):
    assert world.result.found

@then("I should be told that it does not")
def i_should_be_told_that_it_does_not(world):
    assert not world.result.found

@then('the state object should indicate more is False')
def the_state_object_should_indicate_more_is_false(world):
    assert not world.result.more

@then('the state object should indicate more is True')
def the_state_object_should_indicate_more_is_true(world):
    assert world.result.more

@then('the state object should indicate found is False')
def the_state_object_should_indicate_found_is_false(world):
    assert not world.result.found

@then('the state object should indicate found is True')
def the_state_object_should_indicate_found_is_true(world):
    assert world.result.found