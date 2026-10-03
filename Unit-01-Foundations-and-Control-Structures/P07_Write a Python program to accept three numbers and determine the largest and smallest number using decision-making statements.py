a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

if a <= b and a <= c:
    smallest = a
elif b <= a and b <= c:
    smallest = b
else:
    smallest = c

print("Largest number:", largest)
print("Smallest number:", smallest)


Enter first number: 25
Enter second number: 10
Enter third number: 40
Largest number: 40.0
Smallest number: 10.0
