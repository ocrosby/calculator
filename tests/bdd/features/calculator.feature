Feature: Calculator
  As a user
  I want to be able to use a calculator
  So I can calculate things

    Scenario: Add two numbers
        Given I have entered 50 into the calculator
        And I have entered 70 into the calculator
        When I press add
        Then the result should be 120 on the screen

    Scenario: Subtract two numbers
        Given I have entered 50 into the calculator
        And I have entered 70 into the calculator
        When I press subtract
        Then the result should be -20 on the screen

    Scenario: Multiply two numbers
        Given I have entered 50 into the calculator
        And I have entered 70 into the calculator
        When I press multiply
        Then the result should be 3500 on the screen

    Scenario: Divide two numbers
        Given I have entered 50 into the calculator
        And I have entered 70 into the calculator
        When I press divide
        Then the result should be 0.7142857142857143 on the screen

    Scenario: Divide by zero
        Given I have entered 50 into the calculator
        And I have entered 0 into the calculator
        When I press divide
        Then the result should be "Divide by zero error" on the screen

    Scenario: Sine of a number
        Given I have entered 50 into the calculator
        When I press sine
        Then the result should be 0.766044443118978 on the screen

    Scenario: Cosine of a number
        Given I have entered 50 into the calculator
        When I press cosine
        Then the result should be 0.6427876096865393 on the screen

    Scenario: Tangent of a number
        Given I have entered 50 into the calculator
        When I press tangent
        Then the result should be 1.1917535925944938 on the screen

    Scenario: Log of a number
      Given I have entered 50 into the calculator
      When I press log
      Then the result should be 1.6989700043360187 on the screen

    Scenario: Complex expression sin(4^8*(log(-1)))
      Given I have entered the expression "sin(4^8*(log(-1)))"
      When I press evaluate
      Then the result should be -0.9999999999999999 on the screen


