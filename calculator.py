# Simple Calculator Program in Python

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))  # Accept a number input
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def main():
    print("Welcome to the Simple Calculator!")

    # Get user input for the two numbers
    num1 = get_number_input("Enter the first number: ")
    num2 = get_number_input("Enter the second number: ")

    # Show the available operations
    print("\nSelect an operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    while True:
        operation = input("\nChoose the operation (1/2/3/4): ")

        # Perform the operation
        if operation == '1':
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")
            break
        elif operation == '2':
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")
            break
        elif operation == '3':
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")
            break
        elif operation == '4':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
            break
        else:
            print("Invalid input! Please choose a valid operation.")

# Run the program
if __name__ == "__main__":
    main()
