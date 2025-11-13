import math
n = int(input("Enter a number: "))
temp = n
sum_fact = 0
while temp > 0:
    digit = temp % 10
    sum_fact += math.factorial(digit)
    temp //= 10
if sum_fact == n:
    print("Strong number")
else:
    print("Not a strong number")
