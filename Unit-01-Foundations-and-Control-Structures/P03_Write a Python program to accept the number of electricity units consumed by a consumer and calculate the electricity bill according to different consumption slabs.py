# Accept electricity units
units = float(input("Enter electricity units consumed: "))

# Calculate bill according to slabs
if units <= 100:
    bill = units * 5

elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)

elif units <= 300:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

else:
    bill = (100 * 5) + (100 * 7) + (100 * 10) + ((units - 300) * 12)

# Display bill
print("Electricity Units:", units)
print("Electricity Bill: Rs.", bill)


Enter electricity units consumed: 250
Electricity Units: 250.0
Electricity Bill: Rs. 1650.0
