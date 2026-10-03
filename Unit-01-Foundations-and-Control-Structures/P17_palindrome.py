number = int(input("Enter an integer: "))

original = number
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

if original == reverse:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
