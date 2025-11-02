a = float(input("Enter first angle: "))
b = float(input("Enter second angle: "))
c = float(input("Enter third angle: "))

if a + b + c == 180 and a > 0 and b > 0 and c > 0:
    print("Valid triangle")
else:
    print("Invalid triangle")
