# expense_tracker.py

import csv
from expense import Expense # <-- Importing our own module!

import csv

class ExpenseTracker:
    """
    Manages a collection of Expense objects.
    Handles adding expenses and persisting them to a CSV file.
    """
    def __init__(self, filename="expenses.csv"):
        self.filename = filename
        self.expenses = self._load_expenses()

    def add_expense(self, description, category, amount):
        """Creates and adds a validated Expense."""
        expense = Expense(description, category, float(amount))
        self.expenses.append(expense)

    def get_total_expense(self):
        """Returns the total of all expenses."""
        return sum(expense.amount for expense in self.expenses)

    def _load_expenses(self):
        """Loads expenses from CSV, skips invalid ones (e.g., bad category)."""
        expenses_list = []
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        expense = Expense(
                            row['description'],
                            row['category'],
                            float(row['amount'])
                        )
                        expenses_list.append(expense)
                    except (ValueError, KeyError):
                        # Skip rows with invalid data (e.g., old/invalid category)
                        continue
        except FileNotFoundError:
            pass  # Start fresh if file doesn’t exist
        return expenses_list

    def save_expenses(self):
        """Saves all expenses to CSV."""
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["description", "category", "amount"])
            writer.writeheader()
            for expense in self.expenses:
                writer.writerow(expense.to_dict())