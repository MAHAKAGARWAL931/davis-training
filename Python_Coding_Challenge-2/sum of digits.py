# Take input from user
num = int(input("Enter a number: "))

# Initialize sum variable
sum_digits = 0

# Loop until number becomes 0
while num > 0:
    
    # Get last digit
    digit = num % 10
    
    # Add digit to sum
    sum_digits += digit
    
    # Remove last digit from number
    num = num // 10

# Display result
print("Sum of digits =", sum_digits)