import pytest
from homework import discriminant, solution_quadratic_equation


class TestQuadraticEquation:
    @pytest.mark.parametrize("a, b, c, expected",
                             ((1, 8, 15, (-3.0, -5.0)),
                              (1, -13, 12, (12.0, 1.0)),
                              (-4, 28, -49, 3.5),
                              (1, 1, 1, "корней нет")))
    def test_positive(self, a, b, c, expected):
        assert solution_quadratic_equation(a, b, c) == expected

    def test_negative(self):
        assert solution_quadratic_equation(1, 3, 4.5) == "Аргументы должны быть целыми числами!"