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
print(get_even([1, 2, 3, 4]))