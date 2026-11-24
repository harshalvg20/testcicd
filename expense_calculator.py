
from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Expense:
    name: str
    category: str
    amount: float

    def __post_init__(self):
        if not self.name.strip():
            raise ValueError("Expense name cannot be empty")

        if not self.category.strip():
            raise ValueError("Expense category cannot be empty")

        if self.amount <= 0:
            raise ValueError("Expense amount must be positive")


class ExpenseCalculator:
    def __init__(self, budget: float):
        if budget <= 0:
            raise ValueError("Budget must be positive")

        self.budget = budget
        self.expenses = []

    def add_expense(self, expense: Expense):
        self.expenses.append(expense)

    def total_expenses(self) -> float:
        return sum(expense.amount for expense in self.expenses)

    def average_expense(self) -> float:
        if not self.expenses:
            return 0.0

        return self.total_expenses() / len(self.expenses)

    def expenses_by_category(self) -> dict:
        totals = defaultdict(float)

        for expense in self.expenses:
            totals[expense.category] += expense.amount

        return dict(totals)

    def remaining_budget(self) -> float:
        return self.budget - self.total_expenses()

    def is_over_budget(self) -> bool:
        return self.total_expenses() > self.budget

    def generate_report(self) -> str:
        return (
            f"Total expenses: {self.total_expenses():.2f}\n"
            f"Average expense: {self.average_expense():.2f}\n"
            f"Remaining budget: {self.remaining_budget():.2f}\n"
            f"Over budget: {self.is_over_budget()}"
        )


if __name__ == "__main__":
    calculator = ExpenseCalculator(budget=1000)

    calculator.add_expense(Expense("Groceries", "Food", 250))
    calculator.add_expense(Expense("Electricity", "Utilities", 150))
    calculator.add_expense(Expense("Internet", "Utilities", 50))

    print("Expense Report")
    print("==============")
    print(calculator.generate_report())

    print("\nCategory Breakdown")
    print("==================")

    for category, amount in calculator.expenses_by_category().items():
        print(f"{category}: {amount:.2f}")
