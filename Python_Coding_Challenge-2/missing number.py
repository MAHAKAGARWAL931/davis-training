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
print("Missing number =", missing)