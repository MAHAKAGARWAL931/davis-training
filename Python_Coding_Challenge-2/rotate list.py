<<<<<<< HEAD
# Define list
numbers = [1, 2, 3]

# Store last element
last = numbers[-1]

# Shift elements to right
for i in range(len(numbers) - 1, 0, -1):
    numbers[i] = numbers[i - 1]

# Place last element at first position
numbers[0] = last

# Display result
=======
# Define list
numbers = [1, 2, 3]

# Store last element
last = numbers[-1]

# Shift elements to right
for i in range(len(numbers) - 1, 0, -1):
    numbers[i] = numbers[i - 1]

# Place last element at first position
numbers[0] = last

# Display result
>>>>>>> 7ec5fbbffc0cd5a14d753d3044fda9e8e0f41ac7
print("Rotated list =", numbers)