def operations(a, b, operator: str):
    match operator:  # Match case to check the operator
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            if b == 0:
                return "Cannot divide by zero"  # Check for division by zero
            return a / b
        case _:
            return "Invalid operator"


if __name__ == "__main__":
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, *, /): ")

    result = operations(a, b, operator)
    print(f"The result is: {result}")
