# Create employee dictionary
employees = {
    101: {"name": "Pravin", "department": "IT", "salary": 30000},
    102: {"name": "Rahul", "department": "HR", "salary": 25000},
    103: {"name": "Amit", "department": "Finance", "salary": 40000}
}

# Display employee information
print("Employee Information:")
print(employees)


# Add new employee
employees[104] = {
    "name": "Rohit",
    "department": "Sales",
    "salary": 35000
}

print("\nAfter Adding Employee:")
print(employees)


# Update employee information
employees[101]["salary"] = 45000

print("\nAfter Updating Salary:")
print(employees)


# Delete employee
del employees[102]

print("\nAfter Deleting Employee:")
print(employees)


# Display dictionary keys
print("\nEmployee IDs:", employees.keys())

# Display dictionary values
print("Employee Details:", employees.values())

# Display key-value pairs
print("Key-Value Pairs:", employees.items())


# Search employee using employee ID
emp_id = int(input("\nEnter Employee ID to search: "))

if emp_id in employees:
    print("Employee Found!")
    print("Employee ID:", emp_id)
    print("Name:", employees[emp_id]["name"])
    print("Department:", employees[emp_id]["department"])
    print("Salary:", employees[emp_id]["salary"])
else:
    print("Employee Not Found!")


# Dictionary comprehension
salary_limit = int(input("\nEnter minimum salary: "))

high_salary = {
    emp_id: details
    for emp_id, details in employees.items()
    if details["salary"] > salary_limit
}

print("\nEmployees Earning Above", salary_limit)
print(high_salary)



# Employee Information:
# {101: {'name': 'Pravin', 'department': 'IT', 'salary': 30000},
#  102: {'name': 'Rahul', 'department': 'HR', 'salary': 25000},
#  103: {'name': 'Amit', 'department': 'Finance', 'salary': 40000}}

# After Adding Employee:
# Employee 104 added successfully.

# After Updating Salary:
# Employee 101 salary updated successfully.

# After Deleting Employee:
# Employee 102 deleted successfully.

# Employee IDs: dict_keys([101, 103, 104])
# Employee Details: dict_values([...])
# Key-Value Pairs: dict_items([...])

# Enter Employee ID to search: 101

# Employee Found!
# Employee ID: 101
# Name: Pravin
# Department: IT
# Salary: 45000

# Enter minimum salary: 30000

# Employees Earning Above 30000:
# {
#   101: {'name': 'Pravin', 'department': 'IT', 'salary': 45000},
#   103: {'name': 'Amit', 'department': 'Finance', 'salary': 40000},
#   104: {'name': 'Rohit', 'department': 'Sales', 'salary': 35000}
# }
