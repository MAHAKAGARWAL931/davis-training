# eligible to vote or not
def check_eligibility(age):
    return "Eligible" if age >= 18 else "Not Eligible"

age = int(input("Enter age: "))

result = check_eligibility(age)
print(result)