feet = float(input("Enter feet: "))
inches = float(input("Enter inches: "))

# 1 foot = 0.3048 m, 1 inch = 0.0254 m
meters = feet * 0.3048 + inches * 0.0254
centimeters = meters * 100

print("Distance in meters:", meters)
print("Distance in centimeters:", centimeters)
