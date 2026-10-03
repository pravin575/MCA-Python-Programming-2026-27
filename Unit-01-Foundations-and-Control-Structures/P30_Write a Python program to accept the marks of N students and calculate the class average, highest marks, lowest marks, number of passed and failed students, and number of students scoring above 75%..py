n = int(input("Enter the number of students: "))

total = 0
passed = 0
failed = 0
above_75 = 0

highest = 0
lowest = 100

for i in range(1, n + 1):
    marks = float(input("Enter marks of student " + str(i) + ": "))

    total = total + marks

    if marks > highest:
        highest = marks

    if marks < lowest:
        lowest = marks

    if marks >= 40:
        passed = passed + 1
    else:
        failed = failed + 1

    if marks > 75:
        above_75 = above_75 + 1

average = total / n

print("\n----- Class Result -----")
print("Class Average:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Number of Passed Students:", passed)
print("Number of Failed Students:", failed)
print("Students Scoring Above 75%:", above_75)
