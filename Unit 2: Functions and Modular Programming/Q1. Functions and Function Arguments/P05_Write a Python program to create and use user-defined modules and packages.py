
# arithmetic.py

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b


# student/details.py

def student_details():
    name = input("Enter student name: ")
    roll_no = int(input("Enter roll number: "))
    student_class = input("Enter class: ")

    print("\nStudent Details")
    print("Name:", name)
    print("Roll Number:", roll_no)
    print("Class:", student_class)



# student/results.py

def student_result(m1, m2, m3):
    total = m1 + m2 + m3
    average = total / 3
    highest = max(m1, m2, m3)

    print("\nStudent Result")
    print("Total Marks:", total)
    print("Average Marks:", average)
    print("Highest Marks:", highest)


# student/__init__.py

from .details import student_details
from .results import student_result



# main.py

# Import entire module
import arithmetic

# Import selected functions
from arithmetic import addition, multiplication

# Import student package functions
from student import student_details, student_result


# Access entire arithmetic module
print("Addition:", arithmetic.addition(10, 5))
print("Subtraction:", arithmetic.subtraction(10, 5))
print("Multiplication:", arithmetic.multiplication(10, 5))
print("Division:", arithmetic.division(10, 5))


# Access selected functions
print("\nUsing Selected Functions")
print("Addition:", addition(20, 10))
print("Multiplication:", multiplication(20, 10))


# Execute student package functions
student_details()

student_result(80, 90, 85)


# Output

# Addition: 15
# Subtraction: 5
# Multiplication: 50
# Division: 2.0

# Using Selected Functions
# Addition: 30
# Multiplication: 200

# Enter student name: Pravin
# Enter roll number: 21
# Enter class: MCA

# Student Details
# Name: Pravin
# Roll Number: 21
# Class: MCA

# Student Result
# Total Marks: 255
# Average Marks: 85.0
# Highest Marks: 90
