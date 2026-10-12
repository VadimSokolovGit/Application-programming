"""Тесты валидатора IPv4-адресов."""

from ip_validator import is_valid_ipv4


def test_all_valid_fixture_ips(valid_ips):
    """Проверяет, что все корректные адреса из фикстуры возвращают True."""
    for ip in valid_ips:
        assert is_valid_ipv4(ip) is True, f"Ожидался True для корректного адреса: {ip!r}"


def test_all_invalid_fixture_ips(invalid_ips):
    """Проверяет, что все некорректные адреса из фикстуры возвращают False."""
    for ip in invalid_ips:
        assert is_valid_ipv4(ip) is False, f"Ожидался False для некорректного адреса: {ip!r}"
