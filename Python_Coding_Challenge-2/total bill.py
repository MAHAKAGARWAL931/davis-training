<<<<<<< HEAD
# Define function to calculate total bill
def total_bill(items):
    
    total = 0  # Initialize total
    
    # Loop through list
    for price in items:
        total += price   # Add each price
    
    return total   # Return total amount

# Example usage
=======
# Define function to calculate total bill
def total_bill(items):
    
    total = 0  # Initialize total
    
    # Loop through list
    for price in items:
        total += price   # Add each price
    
    return total   # Return total amount

# Example usage
>>>>>>> 7ec5fbbffc0cd5a14d753d3044fda9e8e0f41ac7
print(total_bill([100, 200, 300]))