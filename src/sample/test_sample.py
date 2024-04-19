import pytest

import sample


def test_version():
    assert isinstance(sample.__version__, str)


def test_some_function():
    res = sample.some_function()
    assert res is not None
