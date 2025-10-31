cost_price = float(input("Enter cost price of book: "))
discount_percent = float(input("Enter discount percentage: "))

selling_price = cost_price - (cost_price * discount_percent / 100)
print("Selling price of the book:", selling_price)
