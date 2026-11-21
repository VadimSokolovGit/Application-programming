import pytest

from inn_validator import is_valid_inn


@pytest.mark.parametrize("inn", ["7830002293", "500100732259", "0100000090"])
def test_valid_inn(inn):
    assert is_valid_inn(inn)


@pytest.mark.parametrize(
    "inn",
    [
        "7830002294",
        "500100732258",
        "500100732266",  # 12-я цифра совпадает, 11-я ошибочна.
        "783000229",
        "50010073225",
        "78300А2293",
        "78300 2293",
        "７８３０００２２９３",
        "7830002293 ",
        "0000000000",
        "000000000000",
        7830002293,
        None,
    ],
)
def test_invalid_inn(inn):
    assert not is_valid_inn(inn)
