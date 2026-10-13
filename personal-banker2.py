
"""Personal Banker: my first working version."""
from openpyxl import Workbook
from datetime import datetime, date

# I use a list because later I want to keep more than one expense.
expenses = []

def add_expense():
    print("Personal Banker Project")
    print("Hi user, you can choose a category to record your money:")
    print("1. Food")
    print("2. Transport")
    print("3. Study")
    print("4. Other")

    category_choice = input("Choose 1 to 4: ")

    if category_choice == "1":
        category = "Food"
    elif category_choice == "2":
        category = "Transport"
    elif category_choice == "3":
        category = "Study"
    else:
        category = "Other"

    # input() gives me text. float() changes it into a decimal number.
    amount = float(input("Enter amount spent in AUD: $"))
    date_text = input("Enter date (YYYY-MM-DD): ")
    expense_date = datetime.strptime(date_text, "%Y-%m-%d").date()


    one_expense = {
    "date": expense_date,
    "category": category,
    "amount": amount
    }

    # I put my first expense inside the list.
    expenses.append(one_expense)


def show_expense():
    # This first version only has one expense, so I use position 0.
    first_expense = expenses[0]

    print("My expense is here:")
    print("Category:", first_expense["category"])
    print("Amount: $", first_expense["amount"])
    print("Total spent: $", first_expense["amount"])


def save_to_excel():
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Weekly Expenses"

    sheet.append(["Date", "Category", "Amount (AUD)"])

    for expense in expenses:
        sheet.append([
            expense["date"].strftime("%Y-%m-%d"),
            expense["category"],
            expense["amount"]
        ])

    workbook.save("/Users/wendyyyl/Desktop/weekly_expenses.xlsx")
    print("Your expenses were saved to Excel.")
    today = date.today()
    current_week = today.isocalendar().week
    weekly_total = 0

    for expense in expenses:
        expense_week = expense["date"].isocalendar().week

        if expense_week == current_week:
            weekly_total = weekly_total + expense["amount"]

    print(f"This week's total: ${weekly_total:.2f}")
def show_this_week_total():
    today = date.today()
    current_week = today.isocalendar().week
    weekly_total = 0

    for expense in expenses:
        expense_week = expense["date"].isocalendar().week

        if expense_week == current_week:
            weekly_total = weekly_total + expense["amount"]

    print(f"This week's total: ${weekly_total:.2f}")
while True:
    print("\nPersonal Banker")
    print("1. Add expense")
    print("2. Show expenses and total")
    print("3. Save to Excel and exit")

    choice = input("Choose 1 to 3: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        show_expense()
        show_this_week_total()

    elif choice == "3":
        save_to_excel()
        print("Goodbye!")
        break

    else:
        print("Choose 1, 2 or 3.")
