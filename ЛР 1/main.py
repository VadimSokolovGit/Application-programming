"""Интерактивный интерфейс трекера расходов."""

from datetime import date
import sys
from pathlib import Path

# Говорим Python искать модули внутри папки src:
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from expense_tracker import ExpenseManager



def print_menu():
    print("\n" + "=" * 30)
    print("      ТРЕКЕР РАСХОДОВ")
    print("=" * 30)
    print("1. Добавить расход")
    print("2. Показать все расходы")
    print("3. Фильтровать по категории")
    print("4. Общая сумма трат")
    print("0. Выход")
    print("=" * 30)


def main():
    manager = ExpenseManager("expenses.json")

    while True:
        print_menu()
        choice = input("Выберите действие: ").strip()

        if choice == "0":
            print("До свидания!")
            break

        elif choice == "1":
            print("\n--- Добавление расхода ---")
            
            # 1. Запрашиваем сумму с защитой от ввода букв
            try:
                amount_input = input("Введите сумму (₽): ").strip().replace(",", ".")
                amount = float(amount_input)
            except ValueError:
                print("❌ Ошибка: сумма должна быть числом!")
                continue

            # 2. Запрашиваем категорию и описание
            category = input("Введите категорию (Еда, Транспорт и т.д.): ").strip()
            description = input("Введите описание: ").strip()

            # 3. Запрашиваем дату (с автоподстановкой сегодняшней)
            today_str = str(date.today())
            date_input = input(f"Введите дату (ГГГГ-ММ-ДД) [Enter для {today_str}]: ").strip()
            expense_date = date_input if date_input else today_str

            # 4. Вызываем метод нашего менеджера
            try:
                exp = manager.add_expense(amount, category, description, expense_date)
                print(f"✅ Расход успешно добавлен с ID #{exp.id}!")
            except ValueError as error:
                print(f"❌ Ошибка: {error}")

        elif choice == "2":
            print("\n--- Список всех расходов ---")
            if not manager.expenses:
                print("Расходов пока нет. Самое время что-нибудь добавить!")
            else:
                for exp in manager.expenses:
                    print(f"  [{exp.id}] {exp.date} | {exp.category:<12} | {exp.amount:>8.2f} ₽ | {exp.description}")

        elif choice == "3":
            category = input("\nВведите категорию для поиска: ").strip()
            filtered = manager.get_by_category(category)
            if not filtered:
                print(f"По категории '{category}' трат не найдено.")
            else:
                print(f"\n--- Расходы в категории '{category}' ---")
                for exp in filtered:
                    print(f"  [{exp.id}] {exp.date} | {exp.amount:>8.2f} ₽ | {exp.description}")

        elif choice == "4":
            total = manager.get_total_amount()
            print(f"\n💰 Всего потрачено за всё время: {total:.2f} ₽")

        else:
            print("⚠️ Неизвестная команда. Пожалуйста, введите цифру от 0 до 4.")







if __name__ == "__main__":
    main()
