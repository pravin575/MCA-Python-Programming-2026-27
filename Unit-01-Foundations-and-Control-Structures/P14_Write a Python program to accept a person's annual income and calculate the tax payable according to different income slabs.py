income = float(input("Enter your annual income: "))

if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = (income - 250000) * 0.05
elif income <= 1000000:
    tax = (250000 * 0.05) + (income - 500000) * 0.20
else:
    tax = (250000 * 0.05) + (500000 * 0.20) + (income - 1000000) * 0.30

print("Annual Income:", income)
print("Tax Payable:", tax)



First ₹2,50,000 → 0
Next ₹2,50,000 → 5% = ₹12,500
Remaining ₹3,00,000 → 20% = ₹60,000

Total Tax = ₹72,500
