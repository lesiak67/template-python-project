import pytest
from main import calculate

@pytest.mark.parametrize(
    "expr, expected",
    [
        ("1+2", 3),
        ("2*3+4", 10),
        ("2*(3+4)", 14),
        ("-5+3", -2),
        ("2**3", 8),
        ("7%3", 1),
        ("7//3", 2),
        ("3.5+2.1", pytest.approx(5.6)),
    ],
)
def test_basic_operations(expr, expected):
    assert calculate(expr) == expected