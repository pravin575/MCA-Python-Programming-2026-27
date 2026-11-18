# Global variable
x = 100

def display():
    # Local variable
    y = 50

    print("Global variable:", x)
    print("Local variable:", y)


def change():
    global x
    x = 200
    print("Modified global variable:", x)


# Calling functions
print("Before function call:")
print("Global variable:", x)

display()

change()

print("After function call:")
print("Global variable:", x)


# Lambda functions
square = lambda n: n * n
cube = lambda n: n * n * n
maximum = lambda a, b: a if a > b else b
addition = lambda a, b: a + b

# Taking input
num = int(input("\nEnter a number: "))
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Display results
print("Square:", square(num))
print("Cube:", cube(num))
print("Maximum:", maximum(a, b))
print("Addition:", addition(a, b))



# Before function call:
# Global variable: 100
# Global variable: 100
# Local variable: 50
# Modified global variable: 200
# After function call:
# Global variable: 200

# Enter a number: 5
# Enter first number: 10
# Enter second number: 20

# Square: 25
# Cube: 125
# Maximum: 20
# Addition: 30
