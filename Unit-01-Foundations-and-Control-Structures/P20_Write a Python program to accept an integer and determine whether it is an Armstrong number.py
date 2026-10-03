number = int(input("Enter an integer: "))

original = number
digits = 0
sum = 0

# Count the number of digits
temp = number

while temp > 0:
    digits = digits + 1
    temp = temp // 10

# Calculate the sum of powers of digits
temp = number

while temp > 0:
    digit = temp % 10
    sum = sum + digit ** digits
    temp = temp // 10

if sum == original:
    print("The number is an Armstrong number")
else:
    print("The number is not an Armstrong number")
