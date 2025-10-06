# Accept input from user
P = float(input("Enter the Principal amount: "))
R = float(input("Enter the Rate of interest: "))
T = float(input("Enter the Time (in years): "))

# Calculate Simple Interest
SI = (P * R * T) / 100

# Display the result
print("Simple Interest =", SI)