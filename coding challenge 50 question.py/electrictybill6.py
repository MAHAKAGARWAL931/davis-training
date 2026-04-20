<<<<<<< HEAD
units = int(input("Enter units: "))

slabs = {
    "first": (100, 5),
    "second": (100, 7),
    "third": (float('inf'), 10)
}

bill = 0

for slab in slabs.values():
    limit, rate = slab
    if units > 0:
        used = min(units, limit)
        bill += used * rate
        units -= used

=======
units = int(input("Enter units: "))

slabs = {
    "first": (100, 5),
    "second": (100, 7),
    "third": (float('inf'), 10)
}

bill = 0

for slab in slabs.values():
    limit, rate = slab
    if units > 0:
        used = min(units, limit)
        bill += used * rate
        units -= used

>>>>>>> 7ec5fbbffc0cd5a14d753d3044fda9e8e0f41ac7
print("Total bill amount:", bill)