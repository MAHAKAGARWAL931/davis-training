<<<<<<< HEAD
# Initialize variable to store total weekly sales
total_sales = 0

# Loop runs 7 times (for 7 days in a week)
for day in range(1, 8):
    
    # Take input for each day's sales from user
    sale = float(input(f"Enter sales for day {day}: "))
    
    # Add the current day's sale to total_sales
    total_sales = total_sales + sale

# After loop ends, display total weekly sales
=======
# Initialize variable to store total weekly sales
total_sales = 0

# Loop runs 7 times (for 7 days in a week)
for day in range(1, 8):
    
    # Take input for each day's sales from user
    sale = float(input(f"Enter sales for day {day}: "))
    
    # Add the current day's sale to total_sales
    total_sales = total_sales + sale

# After loop ends, display total weekly sales
>>>>>>> 7ec5fbbffc0cd5a14d753d3044fda9e8e0f41ac7
print("Total Weekly Sales =", total_sales)