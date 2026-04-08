n = int(input("Enter N: "))
even = []

for i in range(1, n+1):
    if i % 2 == 0:
        even.append(i)

print("Even numbers list:", even)