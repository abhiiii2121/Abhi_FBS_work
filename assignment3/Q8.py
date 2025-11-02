import random

userid = input("Enter user ID: ")
password = input("Enter password: ")

if userid == "admin" and password == "1234":
    captcha = random.randint(1000, 9999)
    print("Captcha:", captcha)
    user_input = int(input("Enter the captcha: "))
    
    if user_input == captcha:
        print("Login successful!")
    else:
        print("Captcha mismatch! Login failed.")
else:
    print("Invalid userid or password")
