# Exception Handling Program

try:
    # Division by zero
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Division:", result)

    # Invalid list index
    numbers = [10, 20, 30, 40]

    index = int(input("\nEnter list index: "))
    print("List Element:", numbers[index])

    # Age validation using raise
    age = int(input("\nEnter your age: "))

    if age < 18:
        raise ValueError("Age must be 18 or above")

    print("You are eligible.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError as e:
    print("Value Error:", e)

except IndexError:
    print("Error: Invalid list index.")

else:
    print("\nNo exception occurred.")

finally:
    print("\nFinally block executed.")




# 2. Sample Output
# Case 1: Division by zero

# Enter first number: 10
# Enter second number: 0

# Error: Cannot divide by zero.
# Finally block executed.

  
# Case 2: Invalid numerical input
# Enter first number: abc

# Value Error: invalid literal for int()
# Finally block executed.


# Case 3: Invalid list index
# Enter first number: 10
# Enter second number: 2
# Division: 5.0

# Enter list index: 10
# Error: Invalid list index.
# Finally block executed.



# Case 4: Age less than 18
# Enter first number: 10
# Enter second number: 2
# Division: 5.0

# Enter list index: 1
# List Element: 20

# Enter your age: 16
# Value Error: Age must be 18 or above
# Finally block executed



# Case 5: No exception
# Enter first number: 10
# Enter second number: 2
# Division: 5.0

# Enter list index: 1
# List Element: 20

# Enter your age: 21
# You are eligible.
# No exception occurred.
Finally block executed.
