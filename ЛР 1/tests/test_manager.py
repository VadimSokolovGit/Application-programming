"""Автотесты для трекера расходов."""

import pytest
from expense_tracker import ExpenseManager


def test_add_expense(temp_manager):
    """Проверяет корректное добавление одного расхода."""
    expense = temp_manager.add_expense(
        amount=350.0,
        category="Развлечения",
        description="Билет в кино",
        date="2026-10-18",
    )
    assert len(temp_manager.expenses) == 1
    assert expense.id == 1
    assert expense.amount == 350.0
    assert expense.category == "Развлечения"
    assert expense.description == "Билет в кино"


def test_add_multiple_expenses_increments_id(temp_manager):
    """Проверяет, что у каждой новой записи уникальный возрастающий ID."""
    e1 = temp_manager.add_expense(100.0, "Еда", "Кофе", "2026-10-18")
    e2 = temp_manager.add_expense(200.0, "Еда", "Обед", "2026-10-18")

    assert e1.id == 1
    assert e2.id == 2
    assert len(temp_manager.expenses) == 2


def test_invalid_amount_raises_value_error(temp_manager):
    """Проверяет, что отрицательная или нулевая сумма вызывает ValueError."""
    with pytest.raises(ValueError, match="Amount must be positive"):
        temp_manager.add_expense(0, "Еда", "Тест", "2026-10-18")

    with pytest.raises(ValueError, match="Amount must be positive"):
        temp_manager.add_expense(-50, "Еда", "Тест", "2026-10-18")


def test_invalid_types_raise_type_error(temp_manager):
    """Проверяет, что передача неверных типов вызывает TypeError."""
    with pytest.raises(TypeError, match="Amount must be a number"):
        temp_manager.add_expense("сто рублей", "Еда", "Тест", "2026-10-18")

    with pytest.raises(TypeError, match="Category must be a string"):
        temp_manager.add_expense(100, 123, "Тест", "2026-10-18")


def test_get_by_category(populated_manager):
    """Проверяет фильтрацию расходов по категориям."""
    food_expenses = populated_manager.get_by_category("Еда")
    transport_expenses = populated_manager.get_by_category("Транспорт")
    empty_expenses = populated_manager.get_by_category("Одежда")

    assert len(food_expenses) == 2
    assert len(transport_expenses) == 1
    assert len(empty_expenses) == 0


def test_get_total_amount(populated_manager):
    """Проверяет корректность подсчёта общей суммы трат."""
    # В populated_manager траты: 250.0 + 50.0 + 1200.0 = 1500.0
    assert populated_manager.get_total_amount() == 1500.0


def test_persistence_saving_and_loading(tmp_path):
    """Проверяет сохранение на диск и чтение новым экземпляром менеджера."""
    shared_file = tmp_path / "persistence_test.json"

    # 1. Первый менеджер создаёт файл и записывает расход:
    manager_one = ExpenseManager(filepath=shared_file)
    manager_one.add_expense(750.0, "Подарки", "Книга другу", "2026-10-18")

    # 2. Второй менеджер открывает тот же самый файл:
    manager_two = ExpenseManager(filepath=shared_file)

    # Проверяем, что менеджер_два успешно загрузил данные с диска:
    assert len(manager_two.expenses) == 1
    assert manager_two.expenses[0].id == 1
    assert manager_two.expenses[0].amount == 750.0
    assert manager_two.expenses[0].description == "Книга другу"
