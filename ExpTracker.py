# Welcome message for the user
def greet_name():
    name = input("Please Enter your name: ")  # Prompt user for their name
    print(f"Welcome, {name}! Thank you for budgeting with us.")

# Call the function
greet_name()

# To collect the monthly budget
def ask_income():
    global income  # Declare as global so it's accessible elsewhere
    income = float(input("Please type your monthly income: "))  # Convert input to float
    print(f"Your monthly income is £{income}")

ask_income()

expenses = {}  # Dictionary to store expenses

# To add an expense
def add_expense(expense, cost, category, description):
    expenses[expense] = {"cost": cost, "category": category, "description": description}

# Function to view how much money is left
def view_remaining():
    total_expenses = sum(expense["cost"] for expense in expenses.values())  # Sum all expenses
    remaining_balance = income - total_expenses
    print(f"Your remaining balance is £{remaining_balance}")

# Function to view the current expenses
def view_expenses():
    if expenses:
        print("Your current expenses are:")
        for expense, details in expenses.items():
            print(f"{expense}: £{details['cost']} in {details['category']} catagory to ({details['description']})")
    else:
        print("You have no expenses yet.")

# Function to delete an expense from the budget
def delete_expense():
    expense_to_delete = input("Enter the expense you want to delete: ")
    if expense_to_delete in expenses:
        del expenses[expense_to_delete]
        print(f"The expense '{expense_to_delete}' has been deleted from your budget.")
    else:
        print(f"The expense '{expense_to_delete}' is not found in your budget.")
    
    view_remaining()  # Show the updated balance after deletion

# Function to ask for expense details and manage expense actions
def ask_for_expense():
    while True:
        expense = input("Enter your expense (or type 'x' to stop): ")
        if expense.lower() == 'x':  # If 'x' is entered, stop the loop
            break
        
        try:
            cost = float(input("Enter the price of this expense: £"))  # Convert to float
        except ValueError:
            print("Please enter a valid number for cost.")
            continue
        
        category = input("What type of expense is this? ")
        description = input("Describe what this expense provides: ")

        # Add the expense to the dictionary
        add_expense(expense, cost, category, description)
        print(f"Your {expense} bill for £{cost}, has been added to your budget in the {category} section.")
        
        view_expenses()  # Display the current expenses

        get_expense = input("To stop adding expenses, type 'stop'; to delete an expense, type 'd': ")
        if get_expense.lower() == "stop":
            print("Your budget is complete, here it is:")
            view_expenses()
            print("After paying for all of your expenses, your remaining balance is: ")
            view_remaining()
            break  # Exit the loop
        elif get_expense.lower() == "d":
            delete_expense()
        else:
            print("Continuing to add expenses...")

# Start the function to add expenses
ask_for_expense()

