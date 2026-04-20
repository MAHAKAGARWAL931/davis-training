<<<<<<< HEAD
# Define list
numbers = [1, 1, 2, 3, 3]

# Create empty list to store unique elements
unique = []

# Loop through list
for num in numbers:
    
    # Add only if not already present
    if num not in unique:
        unique.append(num)

# Count unique elements
count = len(unique)

# Display result
=======
# Define list
numbers = [1, 1, 2, 3, 3]

# Create empty list to store unique elements
unique = []

# Loop through list
for num in numbers:
    
    # Add only if not already present
    if num not in unique:
        unique.append(num)

# Count unique elements
count = len(unique)

# Display result
>>>>>>> 7ec5fbbffc0cd5a14d753d3044fda9e8e0f41ac7
print("Number of unique elements =", count)