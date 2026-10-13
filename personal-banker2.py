# Naming and comments reviewed on 2026-10-22; original stage behaviour kept.

"""Personal Banker: my first working version."""
from openpyxl import Workbook
from datetime import datetime, date

# keep expense records
expenses = []

def addexpense():
    print("Personal Banker Project")
    print("Hi user, you can choose a category to record your money:")
    print("1. Food")
    print("2. Transport")
    print("3. Study")
    print("4. Other")

    choice = input("Choose 1 to 4: ")

    if choice == "1":
        category = "Food"
    elif choice == "2":
        category = "Transport"
    elif choice == "3":
        category = "Study"
    else:
        category = "Other"

    # change input to a number
    money = float(input("Enter amount spent in AUD: $"))
    mydate = input("Enter date (YYYY-MM-DD): ")
    dayspent = datetime.strptime(mydate, "%Y-%m-%d").date()


    record = {
    "date": dayspent,
    "category": category,
    "amount": money
    }

    # add the record
    expenses.append(record)


def showexpenses():
    # this version only shows the first record
    first = expenses[0]

    print("My expense is here:")
    print("Category:", first["category"])
    print("Amount: $", first["amount"])
    print("Total spent: $", first["amount"])


def saveexcel():
    book = Workbook()
    sheet = book.active
    sheet.title = "Weekly Expenses"

    sheet.append(["Date", "Category", "Amount (AUD)"])

    for e in expenses:
        sheet.append([
            e["date"].strftime("%Y-%m-%d"),
            e["category"],
            e["amount"]
        ])

    book.save("/Users/wendyyyl/Desktop/weekly_expenses.xlsx")
    print("Your expenses were saved to Excel.")
    today = date.today()
    thisweek = today.isocalendar().week
    weektotal = 0

    for e in expenses:
        week = e["date"].isocalendar().week

        if week == thisweek:
            weektotal = weektotal + e["amount"]

    print(f"This week's total: ${weektotal:.2f}")
def showmyweek():
    today = date.today()
    thisweek = today.isocalendar().week
    weektotal = 0

    for e in expenses:
        week = e["date"].isocalendar().week

        if week == thisweek:
            weektotal = weektotal + e["amount"]

    print(f"This week's total: ${weektotal:.2f}")
while True:
    print("\nPersonal Banker")
    print("1. Add expense")
    print("2. Show expenses and total")
    print("3. Save to Excel and exit")

    choice = input("Choose 1 to 3: ")

    if choice == "1":
        addexpense()

    elif choice == "2":
        showexpenses()
        showmyweek()

    elif choice == "3":
        saveexcel()
        print("Goodbye!")
        break

    else:
        print("Choose 1, 2 or 3.")
