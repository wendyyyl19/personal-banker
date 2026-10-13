# This is my first progress file shared in the class

# I use a list because I want to save more expenses later.
expenses = []


def add_expense():
    print("Personal Banker Project")
    print("Hi, choose a category for your expense:")
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

    # input() gives me text, so I use float() to change it into a number.
    amount = float(input("Enter how much you spent in AUD: $"))

    # I save the category and amount in one dictionary.
    one_expense = {"category": category, "amount": amount}

    # I add this expense to my list.
    expenses.append(one_expense)


def show_expense():
    # I only have one expense in this version, so I use position 0.
    first_expense = expenses[0]

    print("Here is my expense:")
    print("Category:", first_expense["category"])
    print("Amount: $", first_expense["amount"])

    # My total is the same as the amount because I only have one expense.
    print("Total spent: $", first_expense["amount"])


add_expense()
show_expense()
