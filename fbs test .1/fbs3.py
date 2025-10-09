# Program to convert distance from kilometers to meters and centimeters

# Accept input from user
km = float(input("Enter distance in kilometers: "))

# Conversions
meters = km * 1000
centimeters = km * 100000

# Display the results
print("Distance in meters =", meters)
print("Distance in centimeters =", centimeters)