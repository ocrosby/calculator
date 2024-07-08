Feature: Calculation
  In order to be able to do arithmetic
  As a user
  I need to be able to perform multiple calculations

  Scenario: 0+0=0
    Given calculator is cleared
    When I press 0
    And I add 0
    Then the result should be 0

  Scenario: 0-0=0
    Given calculator is cleared
    When I press 0
    And I subtract 0
    Then the result should be 0

  Scenario: 2-2=0
    Given calculator is cleared
    When I press 2
    And I subtract 2
    Then the result should be 0

  Scenario: 2+5-3=4
    Given calculator is cleared
    When I press 2
    And I add 5
    And I subtract 3
    Then the result should be 4


