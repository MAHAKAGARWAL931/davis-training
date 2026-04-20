<<<<<<< HEAD
# electrcity bill based on unit
units = int(input("Enter units: "))

def calculate_bill(u):
    rates = [(100, 5), (100, 7), (float('inf'), 10)]
    bill = 0
    for limit, rate in rates:
        used = min(u, limit)
        bill += used * rate
        u -= used
        if u <= 0:
            break
    return bill

=======
# electrcity bill based on unit
units = int(input("Enter units: "))

def calculate_bill(u):
    rates = [(100, 5), (100, 7), (float('inf'), 10)]
    bill = 0
    for limit, rate in rates:
        used = min(u, limit)
        bill += used * rate
        u -= used
        if u <= 0:
            break
    return bill

>>>>>>> 7ec5fbbffc0cd5a14d753d3044fda9e8e0f41ac7
print("Total bill amount:", calculate_bill(units))