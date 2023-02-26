#!/usr/bin/env python

import os
from setuptools import setup

from distutils.core import setup


def read(fname):
    """Utility function to read the README file."""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="Calculator",
    version="1.0",
    author="Hudson Collier",
    author_email="hudson.collier@gmail.com",
    description=("A Python module implementing a simple calculator"),
    license="BSD",
    url="https://hudson-collier.com/",
    packages=["calc", "tests/unit", "tests/bdd/step_defs"],
    long_description=read("README"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
