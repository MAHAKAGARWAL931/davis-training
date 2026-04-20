# Take input from user
num = int(input("Enter a number: "))

# Initialize variable to store reversed number
reverse = 0

# Loop until number becomes 0
while num > 0:
    
    # Get last digit of number
    digit = num % 10
    
    # Add digit to reversed number
    reverse = reverse * 10 + digit
    
    # Remove last digit from original number
    num = num // 10

# Display reversed number
print("Reversed Number =", reverse)