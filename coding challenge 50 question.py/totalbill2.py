#total bill after discount
def calculate_final_price(price, discount):
    return price * (1 - discount / 100)

price = float(input("Enter price: "))
discount = float(input("Enter discount percentage: "))

result = calculate_final_price(price, discount)
print("Final price after discount:", result)