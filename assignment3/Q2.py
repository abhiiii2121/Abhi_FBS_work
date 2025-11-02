ch = input("Enter an alphabet: ").lower()

if ch in 'aeiou':
    print("Vowel")
elif ch.isalpha():
    print("Consonant")
else:
    print("Not an alphabet")
