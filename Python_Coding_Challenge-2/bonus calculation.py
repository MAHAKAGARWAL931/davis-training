salary = int(input("Enter salary: "))

if salary > 30000:
    bonus = salary * 0.07
else:
    bonus = salary * 0.05   # you can adjust rule if needed

print("Bonus =", int(bonus))