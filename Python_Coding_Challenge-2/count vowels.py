# Take input from user
text = input("Enter a string: ")

# Initialize vowel counter
count = 0

# Convert string to lowercase for easy comparison
text = text.lower()

# Loop through each character in string
for ch in text:
    
    # Check if character is a vowel
    if ch in ['a', 'e', 'i', 'o', 'u']:
        count += 1   # Increase count