# Calculator
A Python program implementing a calculator

## Setup

Setup a virtual environment for the project:

> python3 -m venv venv

Activate the virtual environment:

> source venv/bin/activate

Once activated you will notice the virtual environment indicator ```(venv)``` in your terminal.  To deactivate the virtual environment simply enter ```deactivate``` from the terminal and you will notice that virtual environment indicator goes away, essentially that tells you that you are no longer in your virtual environment.

```bash
(venv) username:calculator name$
```

Install the dependencies:

> pip install -r requirements.txt

Install the development dependencies:

> pip install -r requirements-dev.txt



## Usage

Executing Lint Checking

> invoke lint

or

> inv l

Executing Tests

> invoke test

or

> inv t


## References

* [Testing with Pytest](https://docs.pytest.org/en/7.2.x/)
* [Mocking dependencies during testing with pytest-mock](https://pytest-mock.readthedocs.io/en/latest/index.html)
* [Behavioral Testing Plugin for Pytest](https://pytest-bdd.readthedocs.io/en/stable/#)
* [Behavioral Testing with pytest-bdd](https://automationpanda.com/2018/10/22/python-testing-101-pytest-bdd/)
* [Code Coverage with pytest-cov](https://pytest-cov.readthedocs.io/en/latest/reporting.html)
* [Measuring Code Coverage with coverage.py](https://coverage.readthedocs.io/en/7.2.0/)
* [Formatting Python Code with Black](https://black.readthedocs.io/en/stable/)
* [Managing shell-oriented subprocesses via the Invoke CLI](https://www.pyinvoke.org/)
* [Static Analysis with pycodestyle](https://pycodestyle.pycqa.org/en/latest/)
