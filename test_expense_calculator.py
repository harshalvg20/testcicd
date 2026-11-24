
import pytest

from expense_calculator import Expense, ExpenseCalculator


@pytest.fixture
def calculator():
    result = ExpenseCalculator(budget=1000)

    result.add_expense(Expense("Groceries", "Food", 250))
    result.add_expense(Expense("Electricity", "Utilities", 150))
    result.add_expense(Expense("Internet", "Utilities", 50))

    return result


def test_total_expenses(calculator):
    assert calculator.total_expenses() == 450


def test_average_expense(calculator):
    assert calculator.average_expense() == 150


def test_remaining_budget(calculator):
    assert calculator.remaining_budget() == 550


def test_expenses_by_category(calculator):
    assert calculator.expenses_by_category() == {
        "Food": 250,
        "Utilities": 200,
    }


def test_budget_not_exceeded(calculator):
    assert calculator.is_over_budget() is False


def test_budget_exceeded():
    calculator = ExpenseCalculator(budget=100)

    calculator.add_expense(Expense("Rent", "Housing", 150))

    assert calculator.is_over_budget() is True
    assert calculator.remaining_budget() == -50


def test_empty_calculator():
    calculator = ExpenseCalculator(budget=500)

    assert calculator.total_expenses() == 0
    assert calculator.average_expense() == 0


@pytest.mark.parametrize(
    "amount",
    [0, -10, -100],
)
def test_invalid_expense_amount(amount):
    with pytest.raises(ValueError):
        Expense("Invalid", "Testing", amount)


def test_invalid_budget():
    with pytest.raises(ValueError):
        ExpenseCalculator(budget=0)


def test_empty_expense_name():
    with pytest.raises(ValueError):
        Expense("", "Food", 100)
