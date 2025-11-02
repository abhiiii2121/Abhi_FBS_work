num = int(input("Enter a 3-digit number: "))

if 100 <= num <= 999:
    if str(num) == str(num)[::-1]:
        print("Palindrome number")
    else:
        print("Not a palindrome")
else:
    print("Not a 3-digit number")
