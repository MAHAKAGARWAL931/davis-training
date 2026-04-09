# Initialize variable to store total weekly sales
total_sales = 0

# Loop runs 7 times (for 7 days in a week)
for day in range(1, 8):
    
    # Take input for each day's sales from user
    sale = float(input(f"Enter sales for day {day}: "))
    
    # Add the current day's sale to total_sales
    total_sales = total_sales + sale

# After loop ends, display total weekly sales
print("Total Weekly Sales =", total_sales)