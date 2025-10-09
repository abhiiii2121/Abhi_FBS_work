import math

# Accept values from user
length = float(input("Enter the length of rectangle: "))
breadth = float(input("Enter the breadth of rectangle: "))

# Radius of semicircle
radius = breadth / 2

# Area = area of rectangle + area of semicircle
area = (length * breadth) + (0.5 * math.pi * radius * radius)

# Perimeter = (2 * length) + breadth + semicircular arc
perimeter = (2 * length) + breadth + (math.pi * radius)

# Display results
print(f"\nArea of the figure = {area:.2f}")
print(f"Perimeter of the figure = {perimeter:.2f}")
