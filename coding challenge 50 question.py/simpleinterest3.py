def si(p, r, t):
    si_value = (p * r * t) / 100
    return si_value

p = float(input("Enter P: "))
r = float(input("Enter R: "))
t = float(input("Enter T: "))

result = si(p, r, t)
print("Simple Interest:", result)