<<<<<<< HEAD
# calculatesimple interest(using function)
p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))

simple_interest = lambda p, r, t: (p * r * t) / 100

=======
# calculatesimple interest(using function)
p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))

simple_interest = lambda p, r, t: (p * r * t) / 100

>>>>>>> 7ec5fbbffc0cd5a14d753d3044fda9e8e0f41ac7
print("Simple Interest:", simple_interest(p, r, t))