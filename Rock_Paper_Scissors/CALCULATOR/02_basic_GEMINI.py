import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Error: Cannot divide by zero.")
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        raise ValueError("Error: Cannot calculate square root of a negative number.")
    return math.sqrt(x)

def get_number_input(prompt):
    """Helper function to safely get float numbers from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def display_menu():
    print("\n" + "=" * 30)
    print("      PYTHON CALCULATOR      ")
    print("=" * 30)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Square Root (√)")
    print("7. Exit")
    print("=" * 30)

def main():
    while True:
        display_menu()
        choice = input("Select an operation (1-7): ").strip()

        if choice == '7':
            print("\nThank you for using Python Calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5']:
            num1 = get_number_input("Enter first number: ")
            num2 = get_number_input("Enter second number: ")

            try:
                if choice == '1':
                    result = add(num1, num2)
                    op_symbol = "+"
                elif choice == '2':
                    result = subtract(num1, num2)
                    op_symbol = "-"
                elif choice == '3':
                    result = multiply(num1, num2)
                    op_symbol = "*"
                elif choice == '4':
                    result = divide(num1, num2)
                    op_symbol = "/"
                elif choice == '5':
                    result = power(num1, num2)
                    op_symbol = "^"

                print(f"\nResult: {num1} {op_symbol} {num2} = {result}")

            except ValueError as e:
                print(f"\n{e}")

        elif choice == '6':
            num = get_number_input("Enter number: ")
            try:
                result = square_root(num)
                print(f"\nResult: √{num} = {result}")
            except ValueError as e:
                print(f"\n{e}")

        else:
            print("\nInvalid choice! Please select a valid option from 1 to 7.")

        # Pause before displaying the menu again
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()