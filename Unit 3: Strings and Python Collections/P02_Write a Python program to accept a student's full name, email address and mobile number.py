# Accept student information
name = input("Enter student's full name: ")
email = input("Enter email address: ")
mobile = input("Enter mobile number: ")

# Extract first name and last name using slicing
first_name = name[:name.find(" ")]
last_name = name[name.rfind(" ") + 1:]

# Reverse student's name
reverse_name = name[::-1]

# Extract username and domain from email
username = email[:email.find("@")]
domain = email[email.find("@") + 1:]

# Extract last four digits of mobile number
last_four = mobile[-4:]

# Positive indexing
print("\nPositive Indexing:")
print("First character:", name[0])
print("Second character:", name[1])

# Negative indexing
print("\nNegative Indexing:")
print("Last character:", name[-1])
print("Second last character:", name[-2])

# Display using f-string
print("\n------ STUDENT INFORMATION ------")
print(f"Full Name: {name}")
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"Reversed Name: {reverse_name}")
print(f"Email Username: {username}")
print(f"Email Domain: {domain}")
print(f"Mobile Last Four Digits: {last_four}")

# Other string formatting techniques
print("\nUsing format() method:")
print("Student Name: {}".format(name))
print("Email: {}".format(email))

print("\nUsing % formatting:")
print("Mobile Number: %s" % mobile)



# Enter student's full name: Pravin Gidde
# Enter email address: pravin@gmail.com
# Enter mobile number: 9876543210

# Positive Indexing:
# First character: P
# Second character: r

# Negative Indexing:
# Last character: e
# Second last character: d

# ------ STUDENT INFORMATION ------
# Full Name: Pravin Gidde
# First Name: Pravin
# Last Name: Gidde
# Reversed Name: eddiG nivarP
# Email Username: pravin
# Email Domain: gmail.com
# Mobile Last Four Digits: 3210

# Using format() method:
# Student Name: Pravin Gidde
# Email: pravin@gmail.com

# Using % formatting:
# Mobile Number: 9876543210
