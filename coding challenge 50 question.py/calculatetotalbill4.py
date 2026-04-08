price = float(input("Enter price: "))
discount = float(input("Enter discount %: "))

discount_amount = (price * discount) / 100
final_price = price - discount_amount

print("Final price:", final_price)