# Program to calculate cost of painting interior and exterior walls

# Accepting inputs from the user
interior_area = float(input("Enter total interior wall area (in sq.m): "))
exterior_area = float(input("Enter total exterior wall area (in sq.m): "))

interior_cost_per_sq_m = float(input("Enter cost of painting 1 sq.m of interior wall: "))
exterior_cost_per_sq_m = float(input("Enter cost of painting 1 sq.m of exterior wall: "))

# Calculating total costs
total_interior_cost = interior_area * interior_cost_per_sq_m
total_exterior_cost = exterior_area * exterior_cost_per_sq_m
total_cost = total_interior_cost + total_exterior_cost

# Displaying results
print("\n--- Painting Cost Details ---")
print(f"Total Interior Painting Cost: ₹{total_interior_cost:.2f}")
print(f"Total Exterior Painting Cost: ₹{total_exterior_cost:.2f}")
print(f"Overall Painting Cost: ₹{total_cost:.2f}")