# Take input string
text = input("Enter a string: ")

# Take character to count
char = input("Enter character to count: ")

# Initialize counter
count = 0

# Loop through string
for ch in text:
    
    # Check if character matches
    if ch == char:
        count += 1

# Display result
print("Count =", count)