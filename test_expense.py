# test_expense.py
from expense_tracker import Expense, ExpenseTracker
import os

def test_valid_expense():
    e = Expense("Lunch", "Food", 12.50)
    assert e.description == "Lunch"
    assert e.category == "Food"
    assert e.amount == 12.50
    print("✅ Valid expense test passed")

def test_invalid_category():
    try:
        Expense("Movie", "Space Travel", 20.0)
        assert False, "Should have raised ValueError"

        # Match the actual error message from your Expense class
        assert "Category must be one of" in str(e)
        print("✅ Invalid category test passed")

def test_tracker_saves_and_loads():
    tracker = ExpenseTracker("test_expenses.csv")
    tracker.add_expense("Bus", "Transport", 3.0)
    tracker.save_expenses()

    # Reload
    new_tracker = ExpenseTracker("test_expenses.csv")
    assert len(new_tracker.expenses) == 1
    assert new_tracker.expenses[0].category == "Transport"
    print("✅ Save/load test passed")

    # Clean up
    if os.path.exists("test_expenses.csv"):
        os.remove("test_expenses.csv")

if __name__ == "__main__":
    test_valid_expense()
    test_invalid_category()
    test_tracker_saves_and_loads()
    print("🎉 All tests passed!")