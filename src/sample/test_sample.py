import pytest

import sample


def test_version():
    assert isinstance(sample.__version__, str)
