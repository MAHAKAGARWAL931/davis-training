# Take input from user
text = input("Enter a string: ")

# Reverse the string using slicing
reverse = text[::-1]

# Check if original and reversed are same
if text == reverse:
    print("Yes")   # Palindrome
else:
    print("No")    # Not palindrome