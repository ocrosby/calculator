# Calculator
A Python program implementing a calculator

![Test](https://github.com/ocrosby/calculator/actions/workflows/ci.yml/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/ocrosby/calculator/badge.svg?branch=main)](https://coveralls.io/github/ocrosby/calculator?branch=main)

## Setup

Setup a virtual environment for the project:

> python3 -m venv venv

Activate the virtual environment:

> source venv/bin/activate

Once activated you will notice the virtual environment indicator ```(venv)``` in your terminal.  To deactivate the virtual environment simply enter ```deactivate``` from the terminal and you will notice that virtual environment indicator goes away, essentially that tells you that you are no longer in your virtual environment.

```bash
(venv) username:calculator name$
```

Upgrading the version of Pip

> pip install --upgrade pip

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
* [Tutorial for Behavioral Testing in Pytest](https://automationpanda.com/2018/10/22/python-testing-101-pytest-bdd/)
* [Code Coverage Plugin for Pytest](https://pytest-cov.readthedocs.io/en/latest/reporting.html)
* [A tool for measuring code coverage in Python tests](https://coverage.readthedocs.io/en/7.2.0/)
* [Formatting Python Code with Black](https://black.readthedocs.io/en/stable/)
* [Managing shell-oriented subprocesses via the Invoke CLI](https://www.pyinvoke.org/)
* [Static Analysis with pycodestyle](https://pycodestyle.pycqa.org/en/latest/)
* [Cognitive Complexity](https://www.sonarsource.com/docs/CognitiveComplexity.pdf)
* [Distributing Packages Using SetupTools](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/)
* [Research Paper on Object Oriented Lexical Analyzer](https://scholarworks.rit.edu/cgi/viewcontent.cgi?article=1662&context=article)
