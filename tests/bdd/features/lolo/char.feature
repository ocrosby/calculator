Feature: Char
  As a developer
  I would like to be able to recognize a single specific character or a single arbitrary character
  So that I can do something with it

  Scenario: Check if the Char scan matches a single arbitrary character 1
    Given a Char matching anything
    When the next character is 1
    Then there should be no errors
    And the state object should indicate more is False
    And the state object should indicate found is True

  Scenario: Check if the Char scan matches a single arbitrary character [
    Given a Char matching anything
    When the next character is [
    Then there should be no errors
    And the state object should indicate more is False
    And the state object should indicate found is True

  Scenario: Check if the Char scan matching P matches a single specific character P
    Given a Char matching the character P
    When the next character is P
    Then there should be no errors
    And the state object should indicate more is False
    And the state object should indicate found is True

  Scenario: Check if the Char scan matching P matches a single specific character Q
    Given a Char matching the character P
    When the next character is Q
    Then there should be no errors
    And the state object should indicate more is False
    And the state object should indicate found is False
