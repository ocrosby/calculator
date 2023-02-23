Feature: Calculator
  As a user
  I want to be able to use a calculator
  So I can calculate things

    Scenario: Add two numbers
        Given I have entered the expression "1+2"
        When I evaluate the expression
        Then the result should be "3"

    Scenario: Subtract two numbers
        Given I have entered the expression "9-2"
        When I evaluate the expression
        Then the result should be "7"

    Scenario: Multiply two numbers
        Given I have entered the expression "6*3"
        When I evaluate the expression
        Then the result should be "18"

    Scenario: Divide two numbers
        Given I have entered the expression "4/2"
        When I evaluate the expression
        Then the result should be "2"

    Scenario: Divide by zero
        Given I have entered the expression "1/0"
        When I evaluate the expression
        Then the result should be "Divide by zero error"

    Scenario: Sine of 0
        Given I have entered the expression "sin(0)"
        When I evaluate the expression
        Then the result should be "1"

    Scenario: Cosine of a number
        Given I have entered the expression "cos(0)"
        When I evaluate the expression
        Then the result should be "0"

    Scenario: Tangent of 50
        Given I have entered the expression "tan(50)"
        When I evaluate the expression
        Then the result should be "1.1917535925944938"

    Scenario: Log of a 50
      Given I have entered the expression "log(50)"
      When I evaluate the expression
      Then the result should be "1.6989700043360187"

    Scenario: Complex expression sin(4^8*(log(-1)))
      Given I have entered the expression "sin(4^8*(log(-1)))"
      When I evaluate the expression
      Then the result should be "-0.9999999999999999"


