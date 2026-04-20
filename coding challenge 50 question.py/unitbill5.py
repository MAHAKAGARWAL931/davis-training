<<<<<<< HEAD
units = int(input("Enter units: "))

bill = 0
if units > 200:
    bill += (units - 200) * 10
    units = 200
if units > 100:
    bill += (units - 100) * 7
    units = 100
bill += units * 5

=======
units = int(input("Enter units: "))

bill = 0
if units > 200:
    bill += (units - 200) * 10
    units = 200
if units > 100:
    bill += (units - 100) * 7
    units = 100
bill += units * 5

>>>>>>> 7ec5fbbffc0cd5a14d753d3044fda9e8e0f41ac7
print("Total bill amount:", bill)