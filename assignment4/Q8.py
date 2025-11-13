start = int(input("Enter start: "))
end = int(input("Enter end: "))
print("Numbers divisible by 7 and multiple of 5:")
for i in range(start, end+1):
    if i % 7 == 0 and i % 5 == 0:
        print(i, end=" ")
