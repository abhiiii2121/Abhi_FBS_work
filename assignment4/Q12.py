start = int(input("Enter start: "))
end = int(input("Enter end: "))

print("Armstrong numbers in range:")
for num in range(start, end+1):
    order = len(str(num))
    sum_pow = sum(int(digit)**order for digit in str(num))
    if num == sum_pow:
        print(num, end=" ")
