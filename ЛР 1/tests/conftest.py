"""Фикстуры для тестирования трекера расходов."""

import pytest
from expense_tracker import ExpenseManager


@pytest.fixture
def temp_manager(tmp_path):
    """Создаёт чистый ExpenseManager с временным файлом."""
    test_file = tmp_path / "test_expenses.json"
    return ExpenseManager(filepath=test_file)


@pytest.fixture
def populated_manager(temp_manager):
    """Менеджер, в котором уже есть 3 тестовые записи трат."""
    temp_manager.add_expense(250.0, "Еда", "Кофе и круассан", "2026-10-18")
    temp_manager.add_expense(50.0, "Транспорт", "Метро", "2026-10-18")
    temp_manager.add_expense(1200.0, "Еда", "Продукты на неделю", "2026-10-18")
    return temp_manager
