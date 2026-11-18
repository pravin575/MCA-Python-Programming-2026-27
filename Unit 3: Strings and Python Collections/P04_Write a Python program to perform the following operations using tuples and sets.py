# Create a tuple of student roll numbers
roll_numbers = (101, 102, 103, 104, 105)

print("Student Roll Numbers:", roll_numbers)

# Tuple indexing
print("First Element:", roll_numbers[0])
print("Last Element:", roll_numbers[-1])

# Tuple slicing
print("Slicing:", roll_numbers[1:4])

# Tuple concatenation
tuple2 = (106, 107, 108)
print("Concatenation:", roll_numbers + tuple2)


# Create two sets for different courses
python_students = {101, 102, 103, 104}
java_students = {103, 104, 105, 106}

print("\nPython Students:", python_students)
print("Java Students:", java_students)

# Union
print("Union:", python_students | java_students)

# Intersection
print("Intersection:", python_students & java_students)

# Difference
print("Difference:", python_students - java_students)

# Symmetric Difference
print("Symmetric Difference:", python_students ^ java_students)


# Subset and Superset
set1 = {103, 104}
set2 = {101, 102, 103, 104}

print("\nSubset:", set1.issubset(set2))
print("Superset:", set2.issuperset(set1))


# Add element to set
python_students.add(107)
print("\nAfter Adding:", python_students)

# Remove element from set
python_students.remove(102)
print("After Removing:", python_students)


# Set comprehension
squares = {x * x for x in range(1, 11) if x % 2 == 0}

print("\nSquares of Even Numbers:", squares)



# Student Roll Numbers: (101, 102, 103, 104, 105)
# First Element: 101
# Last Element: 105
# Slicing: (102, 103, 104)
# Concatenation: (101, 102, 103, 104, 105, 106, 107, 108)

# Python Students: {101, 102, 103, 104}
# Java Students: {103, 104, 105, 106}

# Union: {101, 102, 103, 104, 105, 106}
# Intersection: {103, 104}
# Difference: {101, 102}
# Symmetric Difference: {101, 102, 105, 106}

# Subset: True
# Superset: True

# After Adding: {101, 102, 103, 104, 107}
# After Removing: {101, 103, 104, 107}

Squares of Even Numbers: {4, 16, 36, 64, 100}
