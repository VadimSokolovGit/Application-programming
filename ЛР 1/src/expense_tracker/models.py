"""Модели данных для трекера расходов."""

from dataclasses import dataclass, asdict


@dataclass
class Expense:
    """Представление одной траты."""
    id: int
    amount: float
    category: str
    description: str
    date: str

    def to_dict(self) -> dict:
        """Преобразует объект траты в словарь."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Expense":
        """Создаёт объект Expense из словаря, прочитанного из JSON."""
        return cls(
            id=data["id"],
            amount=float(data["amount"]),
            category=data["category"],
            description=data["description"],
            date=data["date"],
        )