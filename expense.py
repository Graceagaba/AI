# expense.py

class Expense:
    VALID_CATEGORIES = {"Food", "Transport", "Housing", "Entertainment", "Utilities", "Other"}

    def __init__(self, description, category, amount):
        if not description.strip():
            raise ValueError("Description can't be empty.")
        if category not in self.VALID_CATEGORIES:
            raise ValueError(f"Category must be one of: {list(self.VALID_CATEGORIES)}")
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        
        self.description = description.strip()
        self.category = category
        self.amount = amount

    def __repr__(self):
        return f"Expense('{self.description}', '{self.category}', {self.amount})"

    def to_dict(self):
        return {
            "description": self.description,
            "category": self.category,
            "amount": self.amount
        }