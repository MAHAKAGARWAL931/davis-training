# Take a character input from user
ch = input("Enter a character: ").lower()   # convert to lowercase

# Check if character is a vowel
if ch in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
else:
    print("Not a Vowel")