# calculatesimple interest(using function)
p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))

simple_interest = lambda p, r, t: (p * r * t) / 100

print("Simple Interest:", simple_interest(p, r, t))