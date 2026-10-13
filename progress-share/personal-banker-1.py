# Naming and comments reviewed on 2026-10-22; original stage behaviour kept.


# keep expense records
expenses = []


def addexpense():
    print("Personal Banker Project")
    print("Hi, choose a category for your expense:")
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
    money = float(input("Enter how much you spent in AUD: $"))

    # category and money for this expense
    record = {"category": category, "amount": money}

    # add the record
    expenses.append(record)


def showexpenses():
    # this version only shows the first record
    first = expenses[0]

    print("Here is my expense:")
    print("Category:", first["category"])
    print("Amount: $", first["amount"])

    # only the first record is counted here
    print("Total spent: $", first["amount"])


addexpense()
showexpenses()
