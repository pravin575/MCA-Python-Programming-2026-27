# Write a Python program to calculate the total marks, average marks and highest marks of a student.
# •	Accept student name and subject details.
# •	Use *args to accept marks of multiple subjects.
# •	Use **kwargs to accept additional student information such as roll number and class.
# •	Return total, average and highest marks from a function.
# •	Display the student result using formatted output.


def student_result(name, *marks, **info):

    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)

    return total, average, highest


# Accept student details
name = input("Enter student name: ")

roll_no = int(input("Enter roll number: "))
student_class = input("Enter class: ")

# Accept subject marks
m1 = int(input("Enter English marks: "))
m2 = int(input("Enter Maths marks: "))
m3 = int(input("Enter Science marks: "))
m4 = int(input("Enter Computer marks: "))

# Calling function using *args and **kwargs
total, average, highest = student_result(
    name, m1, m2, m3, m4,
    roll_no=roll_no,
    student_class=student_class
)

# Display student result
print("\n------ STUDENT RESULT ------")
print("Student Name:", name)
print("Roll Number:", roll_no)
print("Class:", student_class)
print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Marks:", highest)



# Enter student name: Pravin
# Enter roll number: 21
# Enter class: MCA

# Enter English marks: 80
# Enter Maths marks: 90
# Enter Science marks: 85
# Enter Computer marks: 95

# ------ STUDENT RESULT ------
# Student Name: Pravin
# Roll Number: 21
# Class: MCA
# Total Marks: 350
# Average Marks: 87.5
# Highest Marks: 95
