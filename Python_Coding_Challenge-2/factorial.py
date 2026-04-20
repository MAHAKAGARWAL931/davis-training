<<<<<<< HEAD
# Take input from user
num = int(input("Enter a number: "))

# Initialize factorial variable
factorial = 1

# Check if number is negative
if num < 0:
    print("Factorial not defined for negative numbers")

# Calculate factorial using loop
else:
    for i in range(1, num + 1):
        factorial = factorial * i   # multiply each number

    # Display result
=======
# Take input from user
num = int(input("Enter a number: "))

# Initialize factorial variable
factorial = 1

# Check if number is negative
if num < 0:
    print("Factorial not defined for negative numbers")

# Calculate factorial using loop
else:
    for i in range(1, num + 1):
        factorial = factorial * i   # multiply each number

    # Display result
>>>>>>> 7ec5fbbffc0cd5a14d753d3044fda9e8e0f41ac7
    print("Factorial =", factorial)