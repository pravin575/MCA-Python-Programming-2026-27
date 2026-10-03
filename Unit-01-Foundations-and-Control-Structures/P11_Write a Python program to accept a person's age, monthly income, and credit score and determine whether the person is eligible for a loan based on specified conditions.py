# Accept person's details
age = int(input("Enter age: "))
income = float(input("Enter monthly income: "))
credit_score = int(input("Enter credit score: "))

# Check loan eligibility
if age >= 21 and age <= 60 and income >= 25000 and credit_score >= 700:
    print("Person is eligible for loan")
else:
    print("Person is not eligible for loan")



Enter age: 30
Enter monthly income: 40000
Enter credit score: 750
Person is eligible for loan
