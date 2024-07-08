package main

import (
	"context"
	"fmt"
	"github.com/cucumber/godog"
	"testing"
)

type calculatorFeature struct {
	calc *Calculator
}

func (c *calculatorFeature) calculatorIsCleared() error {
	c.calc.Clear()
	return nil
}

func (c *calculatorFeature) iAdd(arg1 int) error {
	c.calc.Add(arg1)
	return nil
}

func (c *calculatorFeature) iPress(arg1 int) error {
	c.calc.Press(arg1)
	return nil
}

func (c *calculatorFeature) iSubtract(arg1 int) error {
	c.calc.Sub(arg1)
	return nil
}

func (c *calculatorFeature) theResultShouldBe(expectedResult int) error {
	actualResult := c.calc.Result()

	if actualResult == expectedResult {
		return nil
	}

	return fmt.Errorf("expected %d, but got %d", expectedResult, actualResult)
}

func InitializeScenario(ctx *godog.ScenarioContext) {
	calcFeature := &calculatorFeature{
		calc: &Calculator{},
	}

	ctx.Before(func(ctx context.Context, sc *godog.Scenario) (context.Context, error) {
		calcFeature.calc.Clear()
		return ctx, nil
	})

	ctx.Step(`^calculator is cleared$`, calcFeature.calculatorIsCleared)
	ctx.Step(`^I add (\d+)$`, calcFeature.iAdd)
	ctx.Step(`^I press (\d+)$`, calcFeature.iPress)
	ctx.Step(`^I subtract (\d+)$`, calcFeature.iSubtract)
	ctx.Step(`^the result should be (\d+)$`, calcFeature.theResultShouldBe)
}

func TestFeatures(t *testing.T) {
	suite := godog.TestSuite{
		ScenarioInitializer: InitializeScenario,
		Options: &godog.Options{
			Format:   "pretty",
			Paths:    []string{"tests/features"},
			TestingT: t, // Testing instance that will run subtests
		},
	}

	if suite.Run() != 0 {
		t.Fatal("non-zero status returned, failed to run feature tests")
	}
}
