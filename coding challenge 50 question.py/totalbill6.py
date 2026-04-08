price = float(input("Enter price: "))
discount = float(input("Enter discount %: "))

final_price = round(price - (price * discount / 100), 2)

print(f"Final price after discount: {final_price}")