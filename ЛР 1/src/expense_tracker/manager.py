import json
from pathlib import Path
from expense_tracker.models import Expense


class ExpenseManager:

    def __init__(self, filepath: str = "expenses.json"):
        self.expenses = []
        self.filepath = Path(filepath)
        self.load()

    def save(self):
        """Сохраняет текущий список расходов в JSON-файл."""

        data = [expense.to_dict() for expense in self.expenses]

        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load(self):
        """Загружает расходы из файла, если он существует."""

        if not self.filepath.exists():
            return

        with open(self.filepath, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                self.expenses = [Expense.from_dict(item) for item in data]
            except json.JSONDecodeError:
                self.expenses = []
    
    
    def add_expense(self, amount, category, description, date):

        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number")
        elif not isinstance(category, str):
            raise TypeError("Category must be a string")
        elif not isinstance(description, str):
            raise TypeError("Description must be a string")
        elif not isinstance(date, str):
            raise TypeError("Date must be a string")
        elif amount <= 0:
            raise ValueError("Amount must be positive")


        
        new_id = len(self.expenses) + 1

        expense = Expense(id=new_id, amount=amount, category=category, description=description, date=date)
        self.expenses.append(expense)

        self.save()
        return expense

    
    def get_by_category(self, category):
        
        if not isinstance(category, str):
            raise TypeError("Category must be a string")

        result = []
        for expense in self.expenses:
            if expense.category == category:
                result.append(expense)
        return result

    
    def get_total_amount(self):
        sum = 0.0
        for i in self.expenses:
            sum += i.amount

        return sum
        

    


        


        
        
