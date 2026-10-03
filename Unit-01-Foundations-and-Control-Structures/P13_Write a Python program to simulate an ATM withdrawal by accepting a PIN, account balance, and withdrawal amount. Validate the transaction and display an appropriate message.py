pin = int(input("Enter your PIN: "))
balance = float(input("Enter account balance: "))
amount = float(input("Enter withdrawal amount: "))

correct_pin = 1234

if pin != correct_pin:
    print("Invalid PIN")
elif amount <= 0:
    print("Invalid withdrawal amount")
elif amount > balance:
    print("Insufficient balance")
else:
    balance = balance - amount
    print("Withdrawal successful")
    print("Remaining balance:", balance)



Enter your PIN: 1234
Enter account balance: 10000
Enter withdrawal amount: 3000
