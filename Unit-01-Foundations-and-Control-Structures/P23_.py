start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

count = 0

print("Prime numbers are:")

for number in range(start, end + 1):

    if number > 1:
        is_prime = True

        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break

        if is_prime:
            print(number)
            count = count + 1

print("Total number of prime numbers:", count)
