<<<<<<< HEAD
# Define two lists
list1 = [1, 2, 3]
list2 = [2, 3, 4]

# Create empty list to store common elements
common = []

# Loop through first list
for num in list1:
    
    # Check if element exists in second list
    if num in list2:
        common.append(num)   # Add to result list

# Display result
=======
# Define two lists
list1 = [1, 2, 3]
list2 = [2, 3, 4]

# Create empty list to store common elements
common = []

# Loop through first list
for num in list1:
    
    # Check if element exists in second list
    if num in list2:
        common.append(num)   # Add to result list

# Display result
>>>>>>> 7ec5fbbffc0cd5a14d753d3044fda9e8e0f41ac7
print("Common elements =", common)