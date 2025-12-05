# main.py

from expense_tracker import ExpenseTracker, Expense  # Also import Expense to access VALID_CATEGORIES

def print_menu():
    """Displays the main menu to the user."""
    print("\n--- Expense Tracker Menu ---")
    print("1. Add a new expense")
    print("2. View all expenses and total")
    print("3. Exit")

def main():
    """The main function to run the application."""
    tracker = ExpenseTracker()

    while True:
        print_menu()
        choice = input("Enter your choice (1-3): ").strip()

        if choice == '1':
            desc = input("Enter expense description: ").strip()
            if not desc:
                print("Description cannot be empty.")
                continue

            print(f"Valid categories: {', '.join(sorted(Expense.VALID_CATEGORIES))}")
            category = input("Enter expense category: ").strip()

            amount_input = input("Enter expense amount: $").strip()
            try:
                amount = float(amount_input)
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue

            try:
                tracker.add_expense(desc, category, amount)
                print("✅ Expense added successfully!")
            except ValueError as e:
                print(f"❌ Error: {e}")

        elif choice == '2':
            print("\n--- All Expenses ---")
            if not tracker.expenses:
                print("No expenses recorded yet.")
            else:
                for expense in tracker.expenses:
                    print(f"- {expense.description} ({expense.category}): ${expense.amount:.2f}")
            print("--------------------")
            print(f"Total Expense: ${tracker.get_total_expense():.2f}")

        elif choice == '3':
            tracker.save_expenses()
            print("Expenses saved. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()