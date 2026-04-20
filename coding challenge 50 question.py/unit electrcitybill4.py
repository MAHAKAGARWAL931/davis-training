<<<<<<< HEAD
units = int(input("Enter units: "))
bill = 0

for i in range(1, units + 1):
    if i <= 100:
        bill += 5
    elif i <= 200:
        bill += 7
    else:
        bill += 10

=======
units = int(input("Enter units: "))
bill = 0

for i in range(1, units + 1):
    if i <= 100:
        bill += 5
    elif i <= 200:
        bill += 7
    else:
        bill += 10

>>>>>>> 7ec5fbbffc0cd5a14d753d3044fda9e8e0f41ac7
print("Total bill:", bill)