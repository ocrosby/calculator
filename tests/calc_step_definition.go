package tests

import (
	"github.com/cucumber/godog"
	calculator "github.com/ocrosby/calculator"
)

var calc calculator.Calculator

func calculatorIsCleared() error {
	return godog.ErrPending
}

func iAdd(arg1 int) error {
	return godog.ErrPending
}

func iPress(arg1 int) error {
	return godog.ErrPending
}

func iSubtract(arg1 int) error {
	return godog.ErrPending
}

func theResultShouldBe(arg1 int) error {
	return godog.ErrPending
}

func InitializeScenario(ctx *godog.ScenarioContext) {
	calc = new(calculator.Calculator)

	ctx.Step(`^calculator is cleared$`, calculatorIsCleared)
	ctx.Step(`^I add (\d+)$`, iAdd)
	ctx.Step(`^I press (\d+)$`, iPress)
	ctx.Step(`^I subtract (\d+)$`, iSubtract)
	ctx.Step(`^the result should be (\d+)$`, theResultShouldBe)
}
