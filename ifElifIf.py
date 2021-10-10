marks = int(input("Enter your marks:\n"))
if marks >= 90:
    print("Grade - Excellent")
elif marks < 90 and marks >= 75:
    print("Grade - First Class")
elif marks < 75 and marks >= 40:
    print("Grade - Average")
else:
    print("Grade - fail\n")