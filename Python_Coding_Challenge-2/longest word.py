<<<<<<< HEAD
# Take input from user
text = input("Enter a sentence: ")

# Split sentence into words
words = text.split()

# Assume first word is longest
longest = words[0]

# Loop through words
for word in words:
    
    # Compare length of each word
    if len(word) > len(longest):
        longest = word   # Update longest word

# Display result
=======
# Take input from user
text = input("Enter a sentence: ")

# Split sentence into words
words = text.split()

# Assume first word is longest
longest = words[0]

# Loop through words
for word in words:
    
    # Compare length of each word
    if len(word) > len(longest):
        longest = word   # Update longest word

# Display result
>>>>>>> 7ec5fbbffc0cd5a14d753d3044fda9e8e0f41ac7
print("Longest word =", longest)