# Basic calculator
"""
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

# result = int(num1) + int(num2)
# By default, python makes the input str.
# Passing the input through int function will
# solve the problem for whole numbers but not decimals.

result = float(num1) + float(num2)
"""

# Advanced calculator
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")
