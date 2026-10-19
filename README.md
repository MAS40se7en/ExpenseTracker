# Expense Tracker CLI

A simple command line app to record and review your expenses. Expenses are stored in a local `expenses.json` file, and it only uses the Python standard library.

## Requirements

- Python 3.9 or newer

No external libraries are needed.

## Usage

Run commands from the project folder:

```bash
python expense_tracker.py <command> [--flag value ...]
```

On Windows you can also use `py expense_tracker.py ...`.

### Commands

| Command | Description |
|---|---|
| `add --description "text" --amount <number>` | Add a new expense |
| `list` | Show all expenses in a table |
| `delete --id <id>` | Delete an expense |
| `summary` | Show the total of all expenses |
| `summary --month <1-12>` | Show the total for a month of the current year |

Wrap descriptions containing spaces in quotes.

### Examples

```bash
python expense_tracker.py add --description "Lunch" --amount 12.50
# Expense added successfully (ID: 1)

python expense_tracker.py list
```

Output:

```
ID   Date         Description    Amount
-----------------------------------------
1    2026-10-19   Lunch            $12.50
```

```bash
python expense_tracker.py summary
# Total expenses: $12.50

python expense_tracker.py summary --month 10
# Total expenses for October: $12.50

python expense_tracker.py delete --id 1
# Expense deleted successfully
```

## Expense properties

Each expense in `expenses.json` has:

- `id`: unique number
- `date`: the date it was added (`YYYY-MM-DD`)
- `description`: what the expense was for
- `amount`: the cost

## Error handling

| Situation | Behavior |
|---|---|
| Missing or unknown command or flags | Usage message is shown |
| Amount is not a number | Error message |
| Month is not between 1 and 12 | `Month must be a number from 1 to 12` |
| ID doesn't exist | Error message |
| No expenses saved | `No expenses were found!` |

## Notes

- `expenses.json` is created automatically in the folder you run the command from.
- Monthly summaries only include expenses from the current year.

## PROJECT URL
https://roadmap.sh/projects/expense-tracker

## Roadmap PROJECT SUBMISSION
https://roadmap.sh/projects/expense-tracker/solutions?u=6ad52f26ef9e0ef6b527de0c
