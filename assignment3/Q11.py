total_amount = 0
ticket_price = float(input("Enter ticket price per person: "))

for i in range(5):
    age = int(input(f"Enter age of person {i+1}: "))
    if age < 12:
        total_amount += ticket_price * 0.7
    elif age > 59:
        total_amount += ticket_price * 0.5
    else:
        total_amount += ticket_price

print("Total ticket amount =", total_amount)
