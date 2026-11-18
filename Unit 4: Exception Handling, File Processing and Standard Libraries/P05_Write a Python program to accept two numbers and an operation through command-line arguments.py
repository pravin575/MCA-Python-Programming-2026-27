import sys

# Accept command-line arguments
num1 = float(sys.argv[1])
operator = sys.argv[2]
num2 = float(sys.argv[3])

# Perform arithmetic operations
if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        sys.exit()
    result = num1 / num2

else:
    print("Invalid operator")
    sys.exit()

# Display result
print("First Number:", num1)
print("Operator:", operator)
print("Second Number:", num2)
print("Result:", result)



# Output:
# First Number: 10.0
# Operator: +
# Second Number: 5.0

# Result: 15.0

# Subtraction:
# python calculator.py 10 - 5

# Output:
# Result: 5.0


# Multiplication:
# python calculator.py 10 "*" 5

# Output:
# Result: 50.0


# Division:
# python calculator.py 10 / 5

# Output:
# Result: 2.0
