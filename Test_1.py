import pytest
from homework import calculate_square


@pytest.mark.parametrize("a, expected_result", [(2, ('Периметр:', 8)), (4, ('Периметр:', 16)), (6, ('Периметр:', 24))])

def test_calculate_square(a, expected_result):
    assert calculate_square(a) == expected_result