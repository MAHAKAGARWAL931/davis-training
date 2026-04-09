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
print(result)