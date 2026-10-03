a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Check whether triangle is valid
if a <= 0 or b <= 0 or c <= 0:
    print("Invalid triangle")

elif a + b <= c or a + c <= b or b + c <= a:
    print("Invalid triangle")

# Classify the triangle
elif a == b and b == c:
    print("Equilateral Triangle")

elif a == b or b == c or a == c:
    print("Isosceles Triangle")

else:
    print("Scalene Triangle")

Enter first side: 5
Enter second side: 5
Enter third side: 5
Equilateral Triangle
