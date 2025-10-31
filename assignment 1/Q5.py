# Input values
P = float(input("Enter Principal: "))
T = float(input("Enter Time (in years): "))
R = float(input("Enter Rate of Interest: "))

# Calculate Compound Interest
CI = P * ( (1 + R/100)**T ) - P

# Display result
print("Compound Interest =", CI)
