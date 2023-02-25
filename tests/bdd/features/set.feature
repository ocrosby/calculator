# Created by omarcrosby at 2/25/23
Feature: Set
  As a developer
  I would like to be able to recognize a single character
  So that I can determine if it does or does not belong to a set of characters

  Scenario: Check if the character 1 belongs to the set of digits
    Given a set of digits
    And inside is set to True on the scan
    When the next character is 1
    Then there should be no errors
    And the state object should indicate more is False
    And the state object should indicate found is True

  Scenario: Check if the character a belongs to the set of digits
    Given a set of digits
    And inside is set to True on the scan
    When the next character is a
    Then there should be no errors
    And the state object should indicate more is False
    And the state object should indicate found is False

  Scenario: Check if the character ( belongs to the compliment of the set of digits
    Given a set of digits
    And inside is set to False on the scan
    When the next character is (
    Then there should be no errors
    And the state object should indicate more is False
    And the state object should indicate found is True
