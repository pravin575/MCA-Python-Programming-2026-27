# 1. Math Library

import math

num = int(input("Enter a number: "))

# Square root
print("Square Root:", math.sqrt(num))

# Factorial
print("Factorial:", math.factorial(num))

# Power
print("Power:", math.pow(num, 2))

# Ceiling
print("Ceiling:", math.ceil(5.3))

# Floor
print("Floor:", math.floor(5.3))




# Sample Output
Enter a number: 5

Square Root: 2.23606797749979
Factorial: 120
Power: 25.0
Ceiling: 6
Floor: 5




# 2. Random Library

import random

# Generate random integer
print("Random Integer:", random.randint(1, 100))

# Create a list
students = ["Pravin", "Rahul", "Amit", "Rohit", "Sagar"]

# Select random element
print("Random Student:", random.choice(students))

# Shuffle list elements
random.shuffle(students)

print("Shuffled List:", students)

# Sample Output
# Random Integer: 45
# Random Student: Amit
# Shuffled List: ['Sagar', 'Pravin', 'Rohit', 'Amit', 'Rahul']



# 3. DateTime Library

from datetime import datetime, date

# Display current date and time
current = datetime.now()

print("Current Date and Time:", current)

# Extract day, month and year
print("Day:", current.day)
print("Month:", current.month)
print("Year:", current.year)

# Accept two dates
date1 = date(2026, 11, 18)
date2 = date(2026, 12, 25)

# Calculate difference
difference = date2 - date1

print("First Date:", date1)
print("Second Date:", date2)
print("Difference Between Dates:", difference.days, "days")

# Sample Output
# Current Date and Time: 2026-11-18 12:50:00
# Day: 18
# Month: 11
# Year: 2026
# First Date: 2026-11-18
# Second Date: 2026-12-25
# Difference Between Dates: 37 days
