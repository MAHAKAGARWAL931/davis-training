<<<<<<< HEAD
# electricity bill
units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10

=======
# electricity bill
units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10

>>>>>>> 7ec5fbbffc0cd5a14d753d3044fda9e8e0f41ac7
print("Total bill amount:", bill)