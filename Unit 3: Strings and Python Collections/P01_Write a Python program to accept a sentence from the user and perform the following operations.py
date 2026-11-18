# Accept sentence from user
sentence = input("Enter a sentence: ")

# Find length
print("Length of string:", len(sentence))

# Convert into uppercase and lowercase
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())

# Remove leading and trailing spaces
print("After removing spaces:", sentence.strip())

# Replace a word
old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

print("After replacement:", sentence.replace(old_word, new_word))

# Count occurrences of a character
char = input("Enter character to count: ")

print("Character count:", sentence.count(char))

# Check startswith and endswith
start = input("Enter starting substring: ")
end = input("Enter ending substring: ")

print("Starts with:", sentence.startswith(start))
print("Ends with:", sentence.endswith(end))

# String concatenation
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

print("Concatenation:", str1 + str2)

# String repetition
print("Repetition:", str1 * 3)

# Membership operators
word = input("Enter word to search: ")

print("Word exists:", word in sentence)
print("Word does not exist:", word not in sentence)


# Enter a sentence: Python is easy to learn

# Length of string: 24
# Uppercase: PYTHON IS EASY TO LEARN
# Lowercase: python is easy to learn

# After removing spaces: Python is easy to learn

# Enter word to replace: easy
# Enter new word: simple

# After replacement: Python is simple to learn

# Enter character to count: a
# Character count: 1

# Enter starting substring: Python
# Starts with: True

# Enter ending substring: learn
# Ends with: True

# Enter first string: Hello
# Enter second string: World

# Concatenation: HelloWorld
# Repetition: HelloHelloHello

# Enter word to search: Python
# Word exists: True
# Word does not exist: False
