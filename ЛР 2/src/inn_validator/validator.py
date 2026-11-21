"""Проверка формата и контрольных цифр ИНН."""

ORGANIZATION_WEIGHTS = (2, 4, 10, 3, 5, 9, 4, 6, 8)
PERSON_FIRST_WEIGHTS = (7, 2, 4, 10, 3, 5, 9, 4, 6, 8)
PERSON_SECOND_WEIGHTS = (3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8)


def _check_digit(digits: str, weights: tuple[int, ...]) -> int:
    total = 0
    for digit, weight in zip(digits, weights):
        total += int(digit) * weight
    return (total % 11) % 10


def is_valid_inn(inn: str) -> bool:
    """Возвращает True, если строка проходит проверку ИНН."""
    if not isinstance(inn, str) or len(inn) not in (10, 12):
        return False

    if not inn.isascii() or not inn.isdigit():
        return False

    if inn == "0" * len(inn):
        return False

    if len(inn) == 10:
        return _check_digit(inn[:9], ORGANIZATION_WEIGHTS) == int(inn[9])

    first_digit = _check_digit(inn[:10], PERSON_FIRST_WEIGHTS)
    second_digit = _check_digit(inn[:11], PERSON_SECOND_WEIGHTS)
    return first_digit == int(inn[10]) and second_digit == int(inn[11])


if __name__ == "__main__":
    inn = input("Введите ИНН: ")
    if is_valid_inn(inn):
        print("ИНН прошёл проверку.")
    else:
        print("Ошибка в формате или контрольных цифрах ИНН.")
