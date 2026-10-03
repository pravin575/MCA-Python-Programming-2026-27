price1 = float(input("Enter price of product 1: "))
quantity1 = int(input("Enter quantity of product 1: "))

price2 = float(input("Enter price of product 2: "))
quantity2 = int(input("Enter quantity of product 2: "))

price3 = float(input("Enter price of product 3: "))
quantity3 = int(input("Enter quantity of product 3: "))

# Calculate subtotal
subtotal = (price1 * quantity1) + (price2 * quantity2) + (price3 * quantity3)

# Calculate discount (10%)
discount = subtotal * 0.10

# Amount after discount
amount = subtotal - discount

# Calculate GST (18%)
gst = amount * 0.18

# Calculate final payable amount
final_amount = amount + gst

print("Subtotal:", subtotal)
print("Discount:", discount)
print("GST:", gst)
print("Final Payable Amount:", final_amount)
