import pytest
from homework import vote


# Константы с сообщениями об ошибках
ERROR_EMPTY_LIST = "Входной аргумент должен быть заполненным списком!"
ERROR_INVALID_TYPE = "Список должен содержать только целые положительные числа!"
ERROR_NOT_UNIQUE = "Максимальное число всегда уникально."


class TestVote:
    @pytest.mark.parametrize("list_, expected", [
        ([1], 1),
        ([1, 1, 1, 2, 3], 1),
        ([1, 2, 3, 2, 2], 2)
    ])
    def test_positive(self, list_, expected):
        assert vote(list_) == expected

    def test_unique_max_num(self):
        assert vote([3, 1, 1, 2, 2]) == ERROR_NOT_UNIQUE

    @pytest.mark.parametrize("list_, expected", [
        ([], ERROR_EMPTY_LIST),
        ((5, 7), ERROR_EMPTY_LIST),
        ("1, 2, 3, 2, 2", ERROR_EMPTY_LIST)
    ])
    def test_arg_is_list(self, list_, expected):
        assert vote(list_) == expected

    @pytest.mark.parametrize("list_, expected", [
        ([1, 1, 2.3], ERROR_INVALID_TYPE),
        ([1, 1, -1], ERROR_INVALID_TYPE),
        ([1, 2, 3, 2, "2"], ERROR_INVALID_TYPE)
    ])
    def test_num_is_integer(self, list_, expected):
        assert vote(list_) == expected