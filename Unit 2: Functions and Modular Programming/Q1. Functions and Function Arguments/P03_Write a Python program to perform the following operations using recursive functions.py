# Recursive function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Recursive function to generate Fibonacci series
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Accept input from user
num = int(input("Enter a number for factorial: "))

terms = int(input("Enter number of terms for Fibonacci: "))


# Display factorial
print("Factorial:", factorial(num))


# Display Fibonacci series
print("Fibonacci Series:")
for i in range(terms):
    print(fibonacci(i), end=" ")

  
# Enter a number for factorial: 5
# Enter number of terms for Fibonacci: 7

# Factorial: 120
# Fibonacci Series:
# 0 1 1 2 3 5 8
