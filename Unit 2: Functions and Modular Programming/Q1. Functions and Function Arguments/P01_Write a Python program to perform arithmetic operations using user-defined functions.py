# Write a Python program to perform arithmetic operations using user-defined functions.
# •	Define separate functions for addition, subtraction, multiplication and division.
# •	Pass numbers using positional arguments.
# •	Demonstrate keyword arguments while calling the functions.
# •	Use default arguments to assign a default operation value.
# •	Return the calculated result from each function


def addition(a, b, operation="Addition"):
    result = a + b
    return result

def subtraction(a, b, operation="Subtraction"):
    result = a - b
    return result

def multiplication(a, b, operation="Multiplication"):
    result = a * b
    return result

def division(a, b, operation="Division"):
    if b == 0:
        return "Division by zero is not possible"
    result = a / b
    return result


# Taking input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Positional arguments
print("Addition:", addition(num1, num2))

# Keyword arguments
print("Subtraction:", subtraction(a=num1, b=num2))

# Default arguments
print("Multiplication:", multiplication(num1, num2))

# Keyword arguments with default argument
print("Division:", division(a=num1, b=num2, operation="Division"))



Enter first number: 20
Enter second number: 10

Addition: 30
Subtraction: 10
Multiplication: 200
Division: 2.0
