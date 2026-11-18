# Create and open file in write mode
file = open("student.txt", "w")

# Accept student details
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
student_class = input("Enter class: ")
marks = input("Enter marks: ")

# Write student details into file
file.write("Student Details\n")
file.write("Name: " + name + "\n")
file.write("Roll Number: " + roll_no + "\n")
file.write("Class: " + student_class + "\n")
file.write("Marks: " + marks + "\n")

# Close file
file.close()

print("\nStudent details written successfully.")


# Open file in read mode
file = open("student.txt", "r")

# Read complete file
print("\n----- Student File Contents -----")
print(file.read())

file.close()


# Open file in append mode
file = open("student.txt", "a")

# Accept additional student details
print("\nEnter additional student details:")

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
student_class = input("Enter class: ")
marks = input("Enter marks: ")

# Append details
file.write("\nStudent Details\n")
file.write("Name: " + name + "\n")
file.write("Roll Number: " + roll_no + "\n")
file.write("Class: " + student_class + "\n")
file.write("Marks: " + marks + "\n")

file.close()

print("\nAdditional student details appended successfully.")


# Read file line by line
file = open("student.txt", "r")

print("\n----- Reading File Line by Line -----")

for line in file:
    print(line, end="")

file.close()

print("\n\nFile closed successfully.")



# Enter student name: Pravin
# Enter roll number: 21
# Enter class: MCA
# Enter marks: 85

# Student details written successfully.

# ----- Student File Contents -----
# Student Details
# Name: Pravin
# Roll Number: 21
# Class: MCA
# Marks: 85

# Enter additional student details:
# Enter student name: Rahul
# Enter roll number: 22
# Enter class: MCA
# Enter marks: 90

# Additional student details appended successfully.

# ----- Reading File Line by Line -----
# Student Details
# Name: Pravin
# Roll Number: 21
# Class: MCA
# Marks: 85

# Student Details
# Name: Rahul
# Roll Number: 22
# Class: MCA
# Marks: 90

# File closed successfully.


