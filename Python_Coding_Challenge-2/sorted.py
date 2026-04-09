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
print("Sorted list =", numbers)