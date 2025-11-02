marks = [float(input(f"Enter marks for subject {i+1}: ")) for i in range(5)]
avg = sum(marks) / 5

if avg >= 60:
    print("First Class")
elif avg >= 45:
    print("Second Class")
elif avg >= 35:
    print("Pass Class")
else:
    print("Fail")
