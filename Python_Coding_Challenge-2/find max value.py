# Create a list (you can also take input from user)
numbers = [10, 45, 67, 23, 89, 12]

# Assume first element is maximum
maximum = numbers[0]

# Loop through the list
for num in numbers:
    
    # Compare each element with current maximum
    if num > maximum:
        maximum = num   # Update maximum

# Display result
print("Maximum value =", maximum)