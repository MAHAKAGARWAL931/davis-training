# Take input from user
num = int(input("Enter a number: "))

# Initialize counter
count = 0

# Handle case when number is 0
if num == 0:
    count = 1
else:
    # Loop until number becomes 0
    while num > 0:
        count += 1        # Increase digit count
        num = num // 10   # Remove last digit

# Display result
print("Number of digits =", count)