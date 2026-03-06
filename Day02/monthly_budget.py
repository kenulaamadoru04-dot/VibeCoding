# Monthly Budget Program - Repeated until 'Exit'

while True:
    # Ask user if they want to start or exit
    user_choice = input("\nType 'Start' to enter a budget or 'Exit' to quit: ")
    if user_choice.lower() == "exit":
        print("Exiting the program. Goodbye!")
        break
    elif user_choice.lower() != "start":
        print("Invalid choice. Please type 'Start' or 'Exit'.")
        continue

    # Ask user for total monthly budget
    try:
        total_budget = float(input("Enter your total monthly budget: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    # Initialize total expenses
    total_expenses = 0.0

    # Loop to enter multiple expenses
    while True:
        expense_input = input("Enter an expense (or type 'done' to finish): ")
        if expense_input.lower() == "done":
            break
        try:
            expense = float(expense_input)
            total_expenses += expense
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")

    # Calculate remaining balance
    remaining_balance = total_budget - total_expenses

    # Display results
    print("\n---------------------------")
    print("Total Budget   :", total_budget)
    print("Total Expenses :", total_expenses)
    print("Remaining      :", remaining_balance)

    # Warning condition
    if remaining_balance < 500:
        print("Warning: Low Funds")
    print("---------------------------")