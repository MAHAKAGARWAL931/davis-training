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
print(is_prime(7))