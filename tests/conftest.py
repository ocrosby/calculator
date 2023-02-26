import mock
import pytest

from calc import app

@pytest.fixture
def root():
    return mock.Mock()

@pytest.fixture
def entry_box():
    return mock.Mock()

@pytest.fixture
def application(root, entry_box):
    return app.App(root, entry_box)