<<<<<<< HEAD
# Take input from user
text = input("Enter a string: ")

# Create empty dictionary to store frequency
freq = {}

# Count frequency of each character
for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

# Print duplicate characters
print("Duplicate characters:")
for ch in freq:
    if freq[ch] > 1:
=======
# Take input from user
text = input("Enter a string: ")

# Create empty dictionary to store frequency
freq = {}

# Count frequency of each character
for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

# Print duplicate characters
print("Duplicate characters:")
for ch in freq:
    if freq[ch] > 1:
>>>>>>> 7ec5fbbffc0cd5a14d753d3044fda9e8e0f41ac7
        print(ch)