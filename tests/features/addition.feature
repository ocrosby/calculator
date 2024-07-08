Feature: Subtraction happens with addition
  In order to be able to do arithmetic
  As a user
  I need to be able to perform multiple calculations

  Scenario:
    Given calculator is cleared
    When I press 2
    And I add 5
    And I subtract 3
    Then the result should be 4


