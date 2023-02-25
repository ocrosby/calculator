# Created by omarcrosby at 2/25/23
Feature: Input Tape
  As a developer
  I want to be able to use an input tape
  So that I can build a Turing Machine

  Scenario: Initialization
    When I create a new input tape
    Then there should be no errors
    And the tape should be empty

  Scenario: Initialization with a string
    When I create a new input tape with the string "Hello World"
    Then there should be no errors
    And the tape should contain "Hello World"

  Scenario: Initial Peek
    Given an input tape with the string "Hello World"
    When I peek at the next character
    Then there should be no errors
    And the next character should be "H"
    And the tape head should be at position 0

  Scenario: Read Operation
    Given an input tape with the string "Hello World"
    When I read the next character
    Then there should be no errors
    And the next character should be "H"
    And the tape head should be at position 1

  Scenario: End of file operation with an empty tape
    Given an empty input tape
    When I determine if the tape is at the end
    Then there should be no errors
    And the result should be true

  Scenario: End of file operation with a non-empty tape
    Given an input tape with the string "Hello World"
    When I determine if the tape is at the end
    Then there should be no errors
    And the result should be false

  Scenario: Beginning of file operation with empty tape
    Given an empty input tape
    When I determine if the tape is at the beginning
    Then there should be no errors
    And the result should be true

  Scenario: Retract from the beginning of the tape
    Given an input tape with the string "Hello World"
    When I retract the tape head
    Then I should see the error "Cannot retract the tape head past the beginning of the tape"
    And the tape head should be at position 0

  Scenario: Retract from the middle of the tape
    Given an input tape with the string "Hello World"
    And the tape head is at position 4
    When I retract the tape head
    Then there should be no errors
    And the tape head should be at position 3

  Scenario: Retract multiple from the middle of the tape
    Given an input tape with the string "Hello World"
    And the tape head is at position 4
    When I retract the tape head 2 times
    Then there should be no errors
    And the tape head should be at position 2
