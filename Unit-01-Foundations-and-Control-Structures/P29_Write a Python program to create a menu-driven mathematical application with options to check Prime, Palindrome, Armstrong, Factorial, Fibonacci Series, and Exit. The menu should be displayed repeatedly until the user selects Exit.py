while True:

    print("\n----- Mathematical Application -----")
    print("1. Check Prime")
    print("2. Check Palindrome")
    print("3. Check Armstrong")
    print("4. Find Factorial")
    print("5. Fibonacci Series")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        number = int(input("Enter an integer: "))

        is_prime = True

        if number <= 1:
            is_prime = False
        else:
            for i in range(2, number):
                if number % i == 0:
                    is_prime = False
                    break

        if is_prime:
            print("The number is Prime")
        else:
            print("The number is not Prime")

    elif choice == 2:
        number = int(input("Enter an integer: "))

        original = number
        reverse = 0

        while number > 0:
            digit = number % 10
            reverse = reverse * 10 + digit
            number = number // 10

        if original == reverse:
            print("The number is Palindrome")
        else:
            print("The number is not Palindrome")

    elif choice == 3:
        number = int(input("Enter an integer: "))

        original = number
        digits = 0
        total = 0

        temp = number

        while temp > 0:
            digits = digits + 1
            temp = temp // 10

        temp = number

        while temp > 0:
            digit = temp % 10
            total = total + digit ** digits
            temp = temp // 10

        if total == original:
            print("The number is Armstrong")
        else:
            print("The number is not Armstrong")

    elif choice == 4:
        number = int(input("Enter an integer: "))

        factorial = 1

        for i in range(1, number + 1):
            factorial = factorial * i

        print("Factorial:", factorial)

    elif choice == 5:
        n = int(input("Enter the number of terms: "))

        a = 0
        b = 1

        print("Fibonacci Series:")

        for i in range(n):
            print(a, end=" ")

            c = a + b
            a = b
            b = c

        print()

    elif choice == 6:
        print("Thank you! Program exited.")
        break

    else:
        print("Invalid choice! Please enter 1 to 6.")
