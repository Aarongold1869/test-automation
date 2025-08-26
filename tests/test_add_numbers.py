import pytest
from adding.add_numbers import add_two_numbers


@pytest.mark.parametrize("test_input,expected", [
    ((2, 2), 4),
    ((50, 51), 101),
    ((1234, 4321), 5555),
    pytest.param((20, 21), 42, marks=pytest.mark.xfail)
])
def test_add_numbers(test_input, expected):
    assert add_two_numbers(*test_input) == expected
