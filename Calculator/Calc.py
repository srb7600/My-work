from Calculator import art

# Addition function
def add(num1, num2):
    return num1 + num2

# Subtraction sunction
def subtract(num1, num2):
    return num1 - num2

# Multiplication function
def multiply(num1, num2):
    return num1 * num2

# Division function
def divide(num1, num2):
    return num1 / num2

# Define dictionary for all mathematical operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Calculator function
def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("Enter first number: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("What do you want to do? ")
        num2 = float(input("Enter next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit the calculator.")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\nThank you for using the calculator. See you again.")

calculator()


