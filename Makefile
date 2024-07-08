.PHONY: lint test

deps:
	go install github.com/golangci/golangci-lint/cmd/golangci-lint@latest

lint:
	golangci-lint run

test:
	go test ./... -v
