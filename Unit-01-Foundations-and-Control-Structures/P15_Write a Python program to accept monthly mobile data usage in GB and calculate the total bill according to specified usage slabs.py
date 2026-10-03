data = float(input("Enter monthly data usage in GB: "))

if data <= 2:
    bill = 100
elif data <= 5:
    bill = 200
elif data <= 10:
    bill = 350
else:
    bill = 500

print("Monthly Data Usage:", data, "GB")
print("Total Bill: ₹", bill)


