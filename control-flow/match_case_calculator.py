num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
user_operation = input("Choose the operation (+, -, *, /):")

match user_operation:
    case "+":
        output = num1 + num2
        print(f"The result is {output}")
    case "-":
        output = num1 - num2
        print(f"The result is {output}")
    case "*":
        output = num1 * num2
        print(f"The result is {output}")
    case "/":
        if num2 > 0:
            output = int(num1 / num2)
            print(f"The result is {output}")
        else:
            print("Cannot divide by zero.")
    case _:
        print("Invalid input")