# Calculator BDD Test Reference

Installing Dependencies

```shell
go install github.com/cucumber/godog/cmd/godog@latest

go get -v github.com/cucumber/godog/cmd/godog@latest
go get -v github.com/testcontainers/testcontainers-go
go get -v github.com/testcontainers/testcontainers-go/wait
```

Running godog via the CLI (depreciated)

```shell
godog tests/features
```

This will give you a message with some stub functions for implementing step definitions as shown below:

```go
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
        ctx.Step(`^calculator is cleared$`, calculatorIsCleared)
        ctx.Step(`^I add (\d+)$`, iAdd)
        ctx.Step(`^I press (\d+)$`, iPress)
        ctx.Step(`^I subtract (\d+)$`, iSubtract)
        ctx.Step(`^the result should be (\d+)$`, theResultShouldBe)
}
```