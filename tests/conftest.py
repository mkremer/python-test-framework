import pytest

from pages.heroku_app import Herokuapp
from pages.dynamic_content import DynamicContent


@pytest.fixture
def visit_the_internet(py):
    _visit = Herokuapp(py).visit_the_internet()
    return _visit


@pytest.fixture
def herokuapp(py):
    _herokuapp = Herokuapp(py)
    return _herokuapp


@pytest.fixture
def link_list(py):
    _link_list = DynamicContent(py).test_links()
    return _link_list
