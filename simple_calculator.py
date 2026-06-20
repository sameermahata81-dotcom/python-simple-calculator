print("SIMPLE CALCULATOR")

num1 = float(input("Enter first number: "))
operation = input("Choose one (+, -, /, *): ")
num2 = float(input("Enter second number: "))

if operation == "+":
    print("Result:", num1 + num2)

elif operation == "-":
    print("Result:", num1 - num2)

elif operation == "/":
    if num2 == 0:
         print("Cannot divide by zero")
    else:
        print("Result:", num1 / num2)

elif operation == "*":
    print("Result:", num1 * num2)

else:
    print("Invalid Operation")