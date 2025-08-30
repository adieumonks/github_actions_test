import pytest

from utils.arith import add


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (-1, 1, 0),
        (-5, -7, -12),
        (1.5, 2.5, pytest.approx(4.0)),
        (-0.1, 0.1, pytest.approx(0.0)),
        (2, 3.5, pytest.approx(5.5)),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected
