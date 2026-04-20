<<<<<<< HEAD
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
=======
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
>>>>>>> 7ec5fbbffc0cd5a14d753d3044fda9e8e0f41ac7
print(result)