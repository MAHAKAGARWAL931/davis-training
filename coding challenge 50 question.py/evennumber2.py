# print even number (1 to N)
n = int(input("Enter N: "))

even_numbers = [x for x in range(1, n+1) if x % 2 == 0]

print("Even numbers:", even_numbers)