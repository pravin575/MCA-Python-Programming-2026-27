# Create a list of n numbers
n = int(input("Enter number of elements: "))

numbers = []

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

print("\nOriginal List:", numbers)


# Insert element at specified position
pos = int(input("Enter position to insert: "))
value = int(input("Enter value to insert: "))

numbers.insert(pos, value)
print("After Insertion:", numbers)


# Remove element at specified position
pos = int(input("Enter position to remove: "))

numbers.pop(pos)
print("After Removal:", numbers)


# Sort ascending and descending
numbers.sort()
print("Ascending Order:", numbers)

numbers.sort(reverse=True)
print("Descending Order:", numbers)


# Maximum, minimum and sum
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))


# List concatenation
list2 = [100, 200, 300]
print("Concatenation:", numbers + list2)


# List repetition
print("Repetition:", numbers * 2)


# Indexing
print("First Element:", numbers[0])
print("Last Element:", numbers[-1])


# Membership
search = int(input("Enter number to search: "))

print("Number exists:", search in numbers)
print("Number does not exist:", search not in numbers)


# List comprehension
even = [x for x in numbers if x % 2 == 0]
odd = [x for x in numbers if x % 2 != 0]
squares = [x * x for x in numbers]

print("Even Numbers:", even)
print("Odd Numbers:", odd)
print("Squares:", squares)


# Demonstrating list methods
numbers.append(50)
print("After append():", numbers)

numbers.extend([60, 70])
print("After extend():", numbers)

numbers.insert(0, 10)
print("After insert():", numbers)

numbers.remove(50)
print("After remove():", numbers)

numbers.pop()
print("After pop():", numbers)

numbers.sort()
print("After sort():", numbers)

numbers.reverse()
print("After reverse():", numbers)




# Enter number of elements: 5
# Enter number: 10
# Enter number: 25
# Enter number: 30
# Enter number: 15
# Enter number: 20

# Original List: [10, 25, 30, 15, 20]

# Enter position to insert: 2
# Enter value to insert: 40

# After Insertion: [10, 25, 40, 30, 15, 20]

# Enter position to remove: 1

# After Removal: [10, 40, 30, 15, 20]

# Ascending Order: [10, 15, 20, 30, 40]
# Descending Order: [40, 30, 20, 15, 10]

# Maximum: 40
# Minimum: 10
# Sum: 115

# Concatenation: [40, 30, 20, 15, 10, 100, 200, 300]
# Repetition: [40, 30, 20, 15, 10, 40, 30, 20, 15, 10]

# First Element: 40
# Last Element: 10

# Enter number to search: 20
# Number exists: True
# Number does not exist: False

# Even Numbers: [40, 30, 20, 10]
# Odd Numbers: [15]
# Squares: [1600, 900, 400, 225, 100]

# After append(): [40, 30, 20, 15, 10, 50]
# After extend(): [40, 30, 20, 15, 10, 50, 60, 70]
# After insert(): [10, 40, 30, 20, 15, 10, 50, 60, 70]
# After remove(): [10, 40, 30, 20, 15, 10, 60, 70]
# After pop(): [10, 40, 30, 20, 15, 10, 60]
# After sort(): [10, 10, 15, 20, 30, 40, 60]
# After reverse(): [60, 40, 30, 20, 15, 10, 10]
