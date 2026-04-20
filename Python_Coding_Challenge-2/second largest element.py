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
print("Second largest =", second)