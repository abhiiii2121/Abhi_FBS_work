# Input number of days
days = int(input("Enter total number of days: "))

# Conversion
years = days // 365
weeks = (days % 365) // 7
remaining_days = (days % 365) % 7

# Display result
print("Years:", years)
print("Weeks:", weeks)
print("Days:", remaining_days)
