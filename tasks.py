from invoke import task


@task(aliases=["c"])
def clean(c):
    print("Cleaning up...")
    # Todo: Delete any temporary files


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


@task(aliases=["p"], pre=[lint, check_format], default=True)
def pre_check(c):
    print("Running precheck...")
