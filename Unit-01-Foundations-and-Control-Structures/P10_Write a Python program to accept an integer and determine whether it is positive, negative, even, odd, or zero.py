# Accept an integer
num = int(input("Enter an integer: "))

# Check positive, negative or zero
if num == 0:
    print("Zero")
elif num > 0:
    print("Positive Number")
else:
    print("Negative Number")

# Check even or odd
if num != 0:
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")


Enter an integer: 25
Positive Number
Odd Number
