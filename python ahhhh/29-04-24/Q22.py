# Take input from the user
input_string = input("Enter a string with special characters: ")

# Remove special characters using a list comprehension and isalnum()
cleaned_string = ''.join(char for char in input_string if char.isalnum() or char.isspace())

# Print the result
print(f"String after removing special characters: {cleaned_string}")




# Take input from the user
input_string = input("Enter a string with special characters: ")

# Initialize an empty string to store the cleaned result
cleaned_string = ""

# Iterate through each character in the input string
for char in input_string:
    # Check if the character is alphanumeric or a space
    if char.isalnum() or char.isspace():
        cleaned_string += char  # Add the character to the cleaned string

# Print the result
print(f"String after removing special characters: {cleaned_string}")


# Take input from the user
input_string = input("Enter a string with special characters: ")

# Initialize an empty string to store the cleaned result
cleaned_string = ""

# Iterate through each character in the input string
for char in input_string:
    # Check if the character is a letter (a-z, A-Z) or a digit (0-9) or a space
    if ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9') or char == ' ':
        cleaned_string += char  # Add the character to the cleaned string

# Print the result
print(f"String after removing special characters: {cleaned_string}")