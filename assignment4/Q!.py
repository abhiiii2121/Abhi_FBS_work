n = int(input("Enter the limit: "))
print("Even numbers up to", n, ":")
for i in range(2, n+1, 2):
    print(i, end=" ")
