def is_eligible(age, limit=18):
    if age >= limit:
        return True
    return False

age = int(input("Enter age: "))

if is_eligible(age):
    print("Eligible")
else:
    print("Not Eligible")