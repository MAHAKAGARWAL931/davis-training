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
        print(ch)