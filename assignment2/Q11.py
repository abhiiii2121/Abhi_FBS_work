amount = int(input("Enter amount: "))

notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
print("Minimum notes needed:")

for note in notes:
    count = amount // note
    amount %= note
    if count > 0:
        print(f"{note} x {count}")
