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
print("Longest word =", longest)