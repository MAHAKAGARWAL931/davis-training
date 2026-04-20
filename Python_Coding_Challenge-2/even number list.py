<<<<<<< HEAD
# Function to return even numbers
def get_even(numbers):
    
    even_list = []   # Store even numbers
    
    # Loop through list
    for num in numbers:
        
        # Check even condition
        if num % 2 == 0:
            even_list.append(num)
    
    return even_list   # Return result

# Example usage
=======
# Function to return even numbers
def get_even(numbers):
    
    even_list = []   # Store even numbers
    
    # Loop through list
    for num in numbers:
        
        # Check even condition
        if num % 2 == 0:
            even_list.append(num)
    
    return even_list   # Return result

# Example usage
>>>>>>> 7ec5fbbffc0cd5a14d753d3044fda9e8e0f41ac7
print(get_even([1, 2, 3, 4]))