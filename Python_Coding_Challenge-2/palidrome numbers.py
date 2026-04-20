<<<<<<< HEAD
# Take input from user
num = int(input("Enter a number: "))

# Store original number for comparison
original = num

# Initialize reverse variable
reverse = 0

# Reverse the number
while num > 0:
    
    # Get last digit
    digit = num % 10
    
    # Build reversed number
    reverse = reverse * 10 + digit
    
    # Remove last digit
    num = num // 10

# Check if original and reversed numbers are same
if original == reverse:
    print("Palindrome Number")
else:
=======
# Take input from user
num = int(input("Enter a number: "))

# Store original number for comparison
original = num

# Initialize reverse variable
reverse = 0

# Reverse the number
while num > 0:
    
    # Get last digit
    digit = num % 10
    
    # Build reversed number
    reverse = reverse * 10 + digit
    
    # Remove last digit
    num = num // 10

# Check if original and reversed numbers are same
if original == reverse:
    print("Palindrome Number")
else:
>>>>>>> 7ec5fbbffc0cd5a14d753d3044fda9e8e0f41ac7
    print("Not a Palindrome")