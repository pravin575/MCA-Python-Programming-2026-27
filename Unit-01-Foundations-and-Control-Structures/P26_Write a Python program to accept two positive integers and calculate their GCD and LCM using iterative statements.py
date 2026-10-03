a = int(input("Enter first positive integer: "))
b = int(input("Enter second positive integer: "))

# Calculate GCD
x = a
y = b

while y != 0:
    remainder = x % y
    x = y
    y = remainder

gcd = x

# Calculate LCM
lcm = (a * b) // gcd

print("GCD:", gcd)
print("LCM:", lcm)
