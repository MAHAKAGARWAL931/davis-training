# Define list
numbers = [1, 2, 2, 3]

# Create empty dictionary
freq = {}

# Loop through list
for num in numbers:
    
    # Update frequency
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

# Display result
print(freq)