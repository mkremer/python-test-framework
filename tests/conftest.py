import pytest

from pages.heroku_app import Herokuapp


@pytest.fixture
def visit_the_internet(py):
    _visit = Herokuapp(py).visit_the_internet()
    return _visit


@pytest.fixture
def herokuapp(py):
    _herokuapp = Herokuapp(py)
    return _herokuapp
