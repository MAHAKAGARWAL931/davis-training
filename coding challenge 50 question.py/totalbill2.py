<<<<<<< HEAD
#total bill after discount
def calculate_final_price(price, discount):
    return price * (1 - discount / 100)

price = float(input("Enter price: "))
discount = float(input("Enter discount percentage: "))

result = calculate_final_price(price, discount)
=======
#total bill after discount
def calculate_final_price(price, discount):
    return price * (1 - discount / 100)

price = float(input("Enter price: "))
discount = float(input("Enter discount percentage: "))

result = calculate_final_price(price, discount)
>>>>>>> 7ec5fbbffc0cd5a14d753d3044fda9e8e0f41ac7
print("Final price after discount:", result)