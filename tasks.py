from invoke import task


@task(aliases=["c"])
def clean(c):
    print("Cleaning up...")
    c.run("rm -f *.png")
    c.run("rm -rf coverage")
    c.run("rm -rf dist")
    c.run("rm -f .coverage")
    c.run("rm -f coverage.xml")
    c.run("rm -rf htmlcov")
    c.run("rm -rf tests/htmlcov")
    c.run("rm -rf tests/.pytest_cache")
    c.run("rm -rf ./.pytest_cache")
    c.run("rm -f tests/coverage.xml")


@task(aliases="f", optional=["check"])
def format(c, check=False):
    print("Formatting...")

    cmd = "black . --line-length=79"

    if check:
        cmd += " --check"
        print("Checking formatting...")
    else:
        print("Formatting ...")

    return c.run(cmd)


@task(aliases=["cf", "fc"])
def check_format(c):
    return format(c, check=True)


@task(aliases=["l", "lp"])
def lint(c):
    print("Linting...")
    return c.run("pycodestyle .")


@task(aliases=["t"])
def test(c):
    print("Testing...")
    return c.run("pytest")

@task(aliases=["v"])
def coverage(c):
    """Runs PyTest unit and integration tests with coverage."""
    c.run("coverage run -m pytest")
    c.run("coverage lcov -o ./coverage/lcov.info")

@task(aliases=["p"], pre=[lint, check_format], default=True)
def pre_check(c):
    print("Running precheck...")
