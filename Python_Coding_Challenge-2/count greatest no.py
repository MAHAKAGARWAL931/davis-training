# Take input from user
n = int(input("Enter a number: "))

# Loop from 1 to n
for i in range(1, n + 1):
    
    # Check if number is even
    if i % 2 == 0:
        print(i)   # Print even number