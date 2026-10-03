maths = float(input("Enter Mathematics marks: "))
physics = float(input("Enter Physics marks: "))
chemistry = float(input("Enter Chemistry marks: "))

total = maths + physics + chemistry
percentage = total / 3

if maths >= 50 and physics >= 50 and chemistry >= 50 and percentage >= 60:
    print("Student is eligible for admission")
else:
    print("Student is not eligible for admission")



Enter Mathematics marks: 70
Enter Physics marks: 65
Enter Chemistry marks: 75

