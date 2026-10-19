import sys
import handlers

def parse_flags(args):
    flags = {}
    for i in range(0, len(args), 2):
        key = args[i]
        if not key.startswith("--") or i + 1 >= len(args):
            return None
        flags[key[2:]] = args[i + 1]
    return flags

def parse_month(value):
    try:
        month = int(value)
    except ValueError:
        month = 0
    if not 1 <= month <= 12:
        print("Month must be a number from 1 to 12")
        sys.exit(1)
    return month

def main():
    args = sys.argv[1:]
    if not args:
        print_usage()
        return

    command, rest = args[0], args[1:]
    flags = parse_flags(rest)

    if flags is None:
        print_usage()
        return

    if command == "list" and not flags:
        handlers.list_expenses()
    elif command == "add" and set(flags) == {"description", "amount"}:
        handlers.add_expense(flags["description"], flags["amount"])
    elif command == "delete" and set(flags) == {"id"}:
        handlers.delete_expense(handlers.parse_id(flags["id"]))
    elif command == "summary" and set(flags) <= {"month"}:
        month = parse_month(flags["month"]) if "month" in flags else None
        handlers.summary(month)
    else:
        print_usage()


def print_usage():
    print("Welcome to expense tracker:")
    print("")
    print("./expense_tracker <command> --<field> <value> --<field> <value>")
    print("./expense_tracker add --description 'your value' --amount <your value>")
    print("")
    print("./expense_tracker list")
    print("./expense_tracker summary")
    print("./expense_tracker summary --month <month value>")
    print("")
    print("./expense_tracker delete --id <id>")

if __name__ == "__main__":
    main()