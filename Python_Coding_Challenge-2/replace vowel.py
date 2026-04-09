# Take input from user
text = input("Enter a string: ")

# Initialize empty string
result = ""

# Convert to lowercase for checking vowels
for ch in text:
    
    # Check if character is vowel
    if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
        result += "*"   # Replace vowel with *
    else:
        result += ch    # Keep character

# Display result
print(result)