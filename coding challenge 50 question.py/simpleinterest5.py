<<<<<<< HEAD
class Interest:
    def __init__(self, p, r, t):
        self.p = p
        self.r = r
        self.t = t

    def calculate(self):
        return (self.p * self.r * self.t) / 100

p = float(input("Enter P: "))
r = float(input("Enter R: "))
t = float(input("Enter T: "))

obj = Interest(p, r, t)
=======
class Interest:
    def __init__(self, p, r, t):
        self.p = p
        self.r = r
        self.t = t

    def calculate(self):
        return (self.p * self.r * self.t) / 100

p = float(input("Enter P: "))
r = float(input("Enter R: "))
t = float(input("Enter T: "))

obj = Interest(p, r, t)
>>>>>>> 7ec5fbbffc0cd5a14d753d3044fda9e8e0f41ac7
print("Simple Interest:", obj.calculate())