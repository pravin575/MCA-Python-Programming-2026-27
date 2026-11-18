try:
    # Open existing file in read mode
    file = open("student.txt", "r")

    # Display file name and mode
    print("File Name:", file.name)
    print("File Mode:", file.mode)

    # Demonstrate read()
    print("\n----- Using read() -----")
    file.seek(0)
    print(file.read())

    # Demonstrate readline()
    print("\n----- Using readline() -----")
    file.seek(0)
    print(file.readline())

    # Demonstrate readlines()
    print("\n----- Using readlines() -----")
    file.seek(0)
    print(file.readlines())

    # Demonstrate tell()
    print("\n----- Using tell() -----")
    file.seek(0)
    print("Current Position:", file.tell())

    file.read(10)
    print("Position after reading 10 characters:", file.tell())

    # Demonstrate seek()
    print("\n----- Using seek() -----")
    file.seek(0)
    print("Position after seek(0):", file.tell())
    print("File Content:", file.read())

except FileNotFoundError:
    print("Error: File does not exist.")

except PermissionError:
    print("Error: Permission denied to access the file.")

except Exception as e:
    print("An error occurred:", e)

else:
    print("\nFile operations completed successfully.")

finally:
    try:
        file.close()
        print("File closed successfully.")
    except NameError:
        print("File was not opened.")



# File Name: student.txt
# File Mode: r

# ----- Using read() -----
# Name: Pravin
# Roll No: 21
# Course: MCA
# Marks: 85

# ----- Using readline() -----
# Name: Pravin

# ----- Using readlines() -----
# ['Name: Pravin\n', 'Roll No: 21\n', 'Course: MCA\n', 'Marks: 85']

# ----- Using tell() -----
# Current Position: 0
# Position after reading 10 characters: 10

# ----- Using seek() -----
# Position after seek(0): 0
# File Content: Name: Pravin
# Roll No: 21
# Course: MCA
# Marks: 85

# File operations completed successfully.
# File closed successfully.
