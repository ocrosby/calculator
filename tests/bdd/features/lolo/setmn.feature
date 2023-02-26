# Created by omarcrosby at 2/25/23
Feature: SetMN
  As a developer
  I would like to be able to recognize between m and n characters which do or do not belong to a set
  So I can recognize sets of characters

  Scenario: Recognize a set of characters from 2 to 3
    Given a set of characters "abc" from 2 to 3
    When the characters "ab" are scanned
    Then there should be no errors
    And the state object should indicate more is True
    And the state object should indicate found is True
