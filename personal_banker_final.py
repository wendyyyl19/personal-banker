# Naming and comments reviewed on 2026-10-22; original stage behaviour kept.

# Personal Banker stores the money spent by the user

# openpyxl is for Excel files, os is for the file location and date is for dates
from openpyxl import Workbook, load_workbook
import os
from datetime import date

# This list stores all the expense records
expenses = []

# The Excel file will stay in the same folder as this Python file
folder = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(folder, "weekly_expenses.xlsx")


# Each expense needs a category, an amount and a date
# There are five steps to make a new record
# 1 Show the message and the four category choices
# 2 Let the user choose a category
# 3 Ask how much was spent
# 4 Get the date and check that it is valid
# 5 Keep the details together in a dictionary, then add it to the list

def addexpense():
    # First the available categories are shown
    print("Personal Banker Project")
    print("Hi user, you can choose a category to record your money:")
    print("1. Food")
    print("2. Transport")
    print("3. Study")
    print("4. Other")

    # A number from 1 to 4 chooses the category
    # The user needs to enter again if the choice is not valid
    while True:
        choice = input("Choose 1 to 4: ")
        if choice in ["1", "2", "3", "4"]:
            break
        print("Please choose 1, 2, 3 or 4.")

    if choice == "1":
        category = "Food"
    elif choice == "2":
        category = "Transport"
    elif choice == "3":
        category = "Study"
    else:
        category = "Other"

    # After choosing the category, the user enters the amount in AUD
    # The amount must be greater than zero and have at most two decimal places
    # A number like .25 is also accepted because it means 0.25
    while True:
        amount_text = input("Enter amount spent in AUD: $").strip()
        amount_parts = amount_text.split(".")
        valid_amount = False

        if len(amount_parts) == 1:
            valid_amount = amount_parts[0].isascii() and amount_parts[0].isdigit()
        elif len(amount_parts) == 2:
            valid_amount = (
                (amount_parts[0] == "" or (amount_parts[0].isascii() and amount_parts[0].isdigit()))
                and amount_parts[1].isascii() and amount_parts[1].isdigit()
                and len(amount_parts[1]) <= 2
            )

        if valid_amount:
            money = float(amount_text)
            if money > 0 and money != float("inf"):
                break
        print("Enter a positive amount, like 20 or 12.50. Zero is not accepted.")

    # The date needs a year, month and day in this order
    # This loop continues until the date and its format are correct
    while True:
        mydate = input("Enter date (YYYY-MM-DD): ").strip()
        date_parts = mydate.split("-")
        valid_date = False

        if len(date_parts) == 3:
            year_text, month_text, day_text = date_parts
            if (
                len(year_text) == 4 and len(month_text) == 2 and len(day_text) == 2
                and year_text.isascii() and year_text.isdigit()
                and month_text.isascii() and month_text.isdigit()
                and day_text.isascii() and day_text.isdigit()
            ):
                year = int(year_text)
                month = int(month_text)
                day = int(day_text)

                # First check that the year and month are valid, then check the number of days
                if 1 <= year <= 9999 and 1 <= month <= 12:
                    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                    # February has 29 days in a leap year
                    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
                        days_in_month[1] = 29
                    if 1 <= day <= days_in_month[month - 1]:
                        valid_date = True

        # If all the checks are correct, use these numbers to create a date object
        if valid_date:
            dayspent = date(year, month, day)
            break
        # This message tells the user to enter the date again
        print("Enter a real date in YYYY-MM-DD format, like 2026-10-14.")

    # The dictionary stores these three details for one expense
    record = {
    "date": dayspent,
    "category": category,
    "amount": money
    }

    # append adds this record to the end of the expense list
    expenses.append(record)


# Show each expense and calculate the total amount
def showexpenses():
    # There is nothing to display when the list is empty
    if len(expenses) == 0:
        print("No expenses yet.")
        return

    # Set the total to zero before adding the expense amounts
    total = 0

    print("My expenses are here:")
    # Each loop shows the details of one expense
    for e in expenses:
        print("Date:", e["date"])
        print("Category:", e["category"])
        print("Amount: $", e["amount"])
        # Add this expense amount to the current total
        total = total + e["amount"]

    # Print the total after the loop finishes
    print("Total spent: $", total)


# This total includes only expenses from the current week
def showmyweek():
    today = date.today()
    # Different years can have the same week number, so also compare the ISO year
    thisyear, thisweek, weekday = today.isocalendar()
    weektotal = 0

    for e in expenses:
        year, week, weekday = e["date"].isocalendar()
        # Include this expense only if both the year and week are the same
        if year == thisyear and week == thisweek:
            weektotal = weektotal + e["amount"]

    print(f"This week's total: ${weektotal:.2f}")
    print(f"Rough estimate: RMB {weektotal * 5:.2f} (using 1 AUD = 5 RMB)")


# The category totals show the spending in each category
def showmycategories():
    # Set the amount to zero for each category
    totals = {"Food": 0, "Transport": 0, "Study": 0, "Other": 0}
    for e in expenses:
        category = e["category"]
        # Use the category name to add the amount to the correct category total
        totals[category] = totals[category] + e["amount"]

    print("Category totals for all saved expenses:")
    for category in totals:
        print(category, f"${totals[category]:.2f}")


# Save the records in Excel so the program can read them next time
def saveexcel():
    # Create a workbook and use its first sheet to store the records
    book = Workbook()
    sheet = book.active
    sheet.title = "Weekly Expenses"
    # The first row contains the names of the three columns
    sheet.append(["Date", "Category", "Amount (AUD)", "Amount (RMB estimate, 1 AUD = 5 RMB)"])

    # Save the previous records together with the new records
    for e in expenses:
        sheet.append([
            e["date"].strftime("%Y-%m-%d"),
            e["category"],
            e["amount"],
            round(e["amount"] * 5, 2)
        ])

    # Save the Excel file at the location defined above
    book.save(filename)
    book.close()
    print("Saved to:", filename)


# Read the previous expense records from the Excel file
def loadexcel():
    # The Excel file may not exist when the program runs for the first time
    if not os.path.exists(filename):
        print("No saved file yet. Start with a new list.")
        return

    # Open the workbook and use the Weekly Expenses sheet
    book = load_workbook(filename)
    sheet = book["Weekly Expenses"]

    # Row 1 has headings, so the expense records start at row 2
    for row in sheet.iter_rows(min_row=2, values_only=True):
        mydate = row[0]
        category = row[1]
        money = row[2]
        # If the row has a date, create an expense record from this row
        if mydate is not None:
            year_text, month_text, day_text = mydate.split("-")
            dayspent = date(int(year_text), int(month_text), int(day_text))
            expenses.append({"date": dayspent, "category": category, "amount": money})

    book.close()
    print("Loaded records:", len(expenses))


# Load the saved records before showing the menu
loadexcel()

# Keep showing this menu until option 5 is chosen
while True:
    print("\nPersonal Banker")
    print("1. Add expense")
    print("2. Show expenses and totals")
    print("3. Show category totals")
    print("4. Save to Excel")
    print("5. Save and exit")

    choice = input("Choose 1 to 5: ")
    if choice == "1":
        addexpense()
        # Save after adding an expense so it is available next time
        saveexcel()
    elif choice == "2":
        showexpenses()
        showmyweek()
    elif choice == "3":
        showmycategories()
    elif choice == "4":
        saveexcel()
    elif choice == "5":
        saveexcel()
        print("Goodbye!")
        # Use break to stop the menu loop after saving the records
        break
    else:
        print("Please choose 1, 2, 3, 4 or 5.")
