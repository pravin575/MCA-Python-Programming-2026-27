number = int(input("Enter an integer: "))

count = 0

print("Factors of", number, "are:")

for i in range(1, number + 1):
    if number % i == 0:
        print(i)
        count = count + 1

print("Total number of factors:", count)
