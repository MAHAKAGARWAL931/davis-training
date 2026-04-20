# Take input from user
text = input("Enter a string: ")

# Initialize empty string
result = ""

# Loop through each character
for ch in text:
    
    # Add only non-space characters
    if ch != " ":
        result += ch

# Display result
print(result)