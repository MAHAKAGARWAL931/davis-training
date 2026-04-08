while True:
    age = int(input("Enter age: "))
    if age > 0:
        break
    print("Please enter a valid age!")

print("Eligible" if age >= 18 else "Not Eligible")