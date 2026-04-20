<<<<<<< HEAD
# Function to check prime number
def is_prime(num):
    
    # Prime numbers are greater than 1
    if num <= 1:
        return "Not Prime"
    
    # Check divisibility
    for i in range(2, num):
        if num % i == 0:
            return "Not Prime"
    
    return "Prime"

# Example usage
=======
# Function to check prime number
def is_prime(num):
    
    # Prime numbers are greater than 1
    if num <= 1:
        return "Not Prime"
    
    # Check divisibility
    for i in range(2, num):
        if num % i == 0:
            return "Not Prime"
    
    return "Prime"

# Example usage
>>>>>>> 7ec5fbbffc0cd5a14d753d3044fda9e8e0f41ac7
print(is_prime(7))