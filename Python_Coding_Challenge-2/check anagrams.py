# Take two input strings
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Remove spaces and convert to lowercase
str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

# Sort and compare both strings
if sorted(str1) == sorted(str2):
    print("True")   # Anagram
else:
    print("False")  # Not anagram