# Input marks for 5 subjects
sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))
sub4 = float(input("Enter marks for Subject 4: "))
sub5 = float(input("Enter marks for Subject 5: "))

# Calculate total and percentage
total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total / 500) * 100

# Display total and percentage
print("Total Marks =", total)
print("Percentage =", percentage, "%")

# Determine grade using if-else
if percentage >= 90:
    print("Grade: A+")
elif percentage >= 80:
    print("Grade: A")
elif percentage >= 70:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 50:
    print("Grade: D")
else:
    print("Grade: Fail")
