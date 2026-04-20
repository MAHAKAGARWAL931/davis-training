<<<<<<< HEAD
# Define list
numbers = [10, 20, 5, 15]

# Remove duplicates by converting to set, then back to list
numbers = list(set(numbers))

# Assume first element as largest and second largest
largest = second = numbers[0]

# Find largest value
for num in numbers:
    if num > largest:
        largest = num

# Find second largest value
second = None
for num in numbers:
    if num != largest:
        if second is None or num > second:
            second = num

# Display result
=======
# Define list
numbers = [10, 20, 5, 15]

# Remove duplicates by converting to set, then back to list
numbers = list(set(numbers))

# Assume first element as largest and second largest
largest = second = numbers[0]

# Find largest value
for num in numbers:
    if num > largest:
        largest = num

# Find second largest value
second = None
for num in numbers:
    if num != largest:
        if second is None or num > second:
            second = num

# Display result
>>>>>>> 7ec5fbbffc0cd5a14d753d3044fda9e8e0f41ac7
print("Second largest =", second)