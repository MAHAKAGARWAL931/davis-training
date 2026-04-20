<<<<<<< HEAD
# Take input from user
text = input("Enter a string: ")

# Initialize empty string
result = ""

# Loop through each character
for ch in text:
    
    # Check if character is lowercase letter
    if 'a' <= ch <= 'z':
        # Convert to uppercase using ASCII
        result += chr(ord(ch) - 32)
    else:
        # Keep character as it is
        result += ch

# Display result
=======
# Take input from user
text = input("Enter a string: ")

# Initialize empty string
result = ""

# Loop through each character
for ch in text:
    
    # Check if character is lowercase letter
    if 'a' <= ch <= 'z':
        # Convert to uppercase using ASCII
        result += chr(ord(ch) - 32)
    else:
        # Keep character as it is
        result += ch

# Display result
>>>>>>> 7ec5fbbffc0cd5a14d753d3044fda9e8e0f41ac7
print(result)