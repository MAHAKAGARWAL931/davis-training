<<<<<<< HEAD
# Define list
numbers = [3, 1, 2]

# Use simple Bubble Sort algorithm
for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):
        
        # Compare adjacent elements
        if numbers[j] > numbers[j + 1]:
            
            # Swap elements
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp

# Display sorted list
=======
# Define list
numbers = [3, 1, 2]

# Use simple Bubble Sort algorithm
for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):
        
        # Compare adjacent elements
        if numbers[j] > numbers[j + 1]:
            
            # Swap elements
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp

# Display sorted list
>>>>>>> 7ec5fbbffc0cd5a14d753d3044fda9e8e0f41ac7
print("Sorted list =", numbers)