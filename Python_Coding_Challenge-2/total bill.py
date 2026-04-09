# Define function to calculate total bill
def total_bill(items):
    
    total = 0  # Initialize total
    
    # Loop through list
    for price in items:
        total += price   # Add each price
    
    return total   # Return total amount

# Example usage
print(total_bill([100, 200, 300]))