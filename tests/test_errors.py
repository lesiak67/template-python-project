import pytest
from main import calculate


def test_empty_expression_raises():
    with pytest.raises(ValueError):
        calculate("")


def test_invalid_syntax_raises():
    with pytest.raises(ValueError):
        calculate("2+*3")


def test_division_by_zero_raises():
    with pytest.raises(ValueError):
        calculate("1/0")


def test_disallowed_names_or_calls_are_blocked():
    # attempts to execute names/calls should be rejected
    with pytest.raises(ValueError):
        calculate("__import__('os').system('echo unsafe')")

    with pytest.raises(ValueError):
        calculate("open('file.txt','w')")
