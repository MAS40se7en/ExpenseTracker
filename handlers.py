import sys
import json
from pathlib import Path
from datetime import date
import calendar

TASK_FILE = Path("expenses.json")

def now():
    return date.today().isoformat()

def load_expenses():
    if not TASK_FILE.exists():
        save_expenses()
        return[]

    try:
        with open(TASK_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Error: tasks.json is not valid JSON.")
        sys.exit(1)

def save_expenses(expenses=[]):
    with open(TASK_FILE, "w", encoding="utf-8") as f:
        json.dump(expenses, f, indent=2)

def parse_id(value):
    try:
        return int(value)
    except ValueError:
        print(f"Invalid ID: '{value}' (must be a number)")
        sys.exit(1)

def find_expense(expenses, expsnse_id):
    for e in expenses:
        if e["id"] == expsnse_id:
            return e
    return None

def list_expenses():
    expenses = load_expenses()

    if len(expenses) == 0:
        print("No expenses were found!")
        return

    desc_width = max(len("Description"), *(len(e["description"]) for e in expenses))

    print(f"{'ID':<4} {'Date':<12} {'Description':<{desc_width}} {'Amount':>10}")
    print("-" * (4 + 1 + 12 + 1 + desc_width + 1 + 10))

    for e in expenses:
        date = e["date"][:10]
        amount = f"${float(e['amount']):.2f}"
        print(f"{e['id']:<4} {date:12} {e['description']:<{desc_width}} {e['amount']:>10}")

def add_expense(description, amount):
    expenses = load_expenses()
    id = max((e["id"] for e in expenses), default=0) + 1
    try:
        exp_amount = int(amount)
        if exp_amount < 0:
            print("Invalid amount!")
            return
        expense = {
            "id": id,
            "date": now(),
            "description": description,
            "amount": exp_amount
        }
    except ValueError:
        print("Make sure to enter a number in for the month value")
        return
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Expense with id {id} saved to expenses.json file!")

def update_expense(expense_id, descripiton, amount):
    expenses = load_expenses()
    expense = find_expense(expenses, expense_id)
    if not expense:
        print(f"No expense with id {expense_id} found!")
        return
    
    expense["description"] = descripiton
    expense["amount"] = amount
    save_expenses(expenses)
    print(f"Expenses with id {expense_id} was updated!")

def summary(month=None):
    expenses = load_expenses()

    if month is not None:
        this_year = date.today().year
        expenses = [
            e for e in expenses
            if date.fromisoformat(e["date"]).month == month
            and date.fromisoformat(e["date"]).year == this_year
        ]

    total = sum(float(e["amount"]) for e in expenses)

    if month is not None:
        print(f"Total expenses for {calendar.month_name[month]}: ${total:.2f}")
    else:
        print(f"Total expenses: ${total:.2f}")

def delete_expense(expense_id):
    expenses = load_expenses()
    expense = find_expense(expenses, expense_id)
    if not expense:
        print(f"No expense has been found with id {expense_id}")
        return
    expenses.remove(expense)
    save_expenses(expenses)
    print(f"Expense with id {expense_id} was deleted!")