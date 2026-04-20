<<<<<<< HEAD
# Define list (sequence with one missing number)
numbers = [1, 2, 4, 5]

# Find expected sum of sequence from 1 to n
n = len(numbers) + 1
expected_sum = n * (n + 1) // 2

# Find actual sum
actual_sum = sum(numbers)

# Missing number
missing = expected_sum - actual_sum

# Display result
=======
# Define list (sequence with one missing number)
numbers = [1, 2, 4, 5]

# Find expected sum of sequence from 1 to n
n = len(numbers) + 1
expected_sum = n * (n + 1) // 2

# Find actual sum
actual_sum = sum(numbers)

# Missing number
missing = expected_sum - actual_sum

# Display result
>>>>>>> 7ec5fbbffc0cd5a14d753d3044fda9e8e0f41ac7
print("Missing number =", missing)