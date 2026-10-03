number = int(input("Enter an integer: "))

sum = 0
product = 1

while number > 0:
    digit = number % 10
    sum = sum + digit
    product = product * digit
    number = number // 10

print("Sum of digits:", sum)
print("Product of digits:", product)
